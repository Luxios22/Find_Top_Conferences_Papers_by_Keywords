import re
import csv
import requests
import collections
import bibtexparser
from bs4 import BeautifulSoup
from utils import get_parser, save_json, search_pdf_link, find_sg_university
from config import urls, names, header, header_sg, search_list, sg_universities


def scrape(urls, names):
    res = collections.defaultdict(dict)
    for url, name in zip(urls, names):
        print(f'name:{name}\turl:{url}')
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        conference, year=re.findall(r'[a-zA-Z]+|[0-9]+',name)
        res[conference][year] = []
        if soup.findAll(class_="entry article"):
            paper_list = soup.findAll(class_="entry article")
            info = ['booktitle']
        elif soup.findAll(class_='entry inproceedings'):
            paper_list = soup.findAll(class_='entry inproceedings')
            info = ['journal', 'volume']
        for paper_item in paper_list:
            try: 
                biburl=paper_item.find('a', href=re.compile("bibtex")).get('href').replace("html?view=bibtex", "bib?param=1")
                bib_data = bibtexparser.loads(re.sub(r'\s{2,}', ' ', requests.get(biburl).text.replace('\n','')))
                paper = [re.sub(r'\\+', '', bib_data.entries[0][x]) if x in bib_data.entries[0].keys() else '' for x in ['author', 'title'] + info + ['biburl', 'url']]
                if len(paper)>5:
                    paper = paper[:2] + [paper[2] + ' ' + paper[3]] + paper[-2:]
                res[conference][year].append(paper)
            except Exception as e:
                print("Exception:", e)
    return res

def main():
    args = get_parser().parse_args()
    res = scrape(urls, names)
    save_json(res, 'results/data.json')
    with open('results/all_papers.csv', 'w', encoding='UTF8', newline='') as f1, open(f'results/{args.keyword}_papers.csv', 'w', encoding='UTF8', newline='') as f2, open(f'results/sg_{args.keyword}_papers.csv', 'w', encoding='UTF8', newline='') as f3, open(f'results/outliers.csv', 'w', encoding='UTF8', newline='') as f4:
        writer1 = csv.writer(f1)
        writer2 = csv.writer(f2)
        writer3 = csv.writer(f3)
        writer4 = csv.writer(f4)
        # write the header
        writer1.writerow(header)
        writer2.writerow(header)
        writer3.writerow(header_sg)
        writer4.writerow(header)
        # write data
        for conf, years in res.items():
            for year, papers in years.items():
                for paper in papers:
                    author, title, booktitle, biburl, ee_link = paper
                    writer1.writerow([conf, year] + paper)
                    if args.keyword in title.lower():
                        writer2.writerow([conf, year] + paper)
                        if args.find_sg:
                            try:
                                arxiv_pdf_link = search_pdf_link(title, conf, ee_link)
                                if arxiv_pdf_link: 
                                    uni = find_sg_university(arxiv_pdf_link, search_list, sg_universities)
                                    if uni:
                                        info = author + title + booktitle 
                                        writer3.writerow([uni, year, conf] + [info] + [biburl, ee_link])
                                else:
                                    writer4.writerow([conf, year] + paper)
                            except Exception as e:
                                print("search pdf failed:", e)
                                writer4.writerow([conf, year] + paper)


if __name__ == '__main__':
    main()