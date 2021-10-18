"""
Note:
The file is meant to fix the outliers when finding papers of Singapore universities.
If you've not tried to find papers of Singapore universities, please do not use this file.
"""
import csv
import time
from config import search_list, sg_universities
from utils import get_parser, csv_length, search_pdf_link, find_sg_university

def main():
    args = get_parser().parse_args()
    while(csv_length("results/outliers.csv")>0):
        with open(f'results/sg_{args.keyword}_papers.csv', 'a+', encoding='UTF8', newline='') as f1, open('results/outliers.csv', 'r', encoding='UTF8', newline='') as f2, open('results/outliers_bak.csv', 'w', encoding='UTF8', newline='') as f3:
            reader = csv.reader(f2)
            header = next(reader)
            writer1 = csv.writer(f1)
            writer2 = csv.writer(f3)
            writer2.writerow(header)
            for paper in reader:
                conf, year, author, title, booktitle, biburl, ee_link = paper
                try:
                    arxiv_pdf_link = search_pdf_link(title, conf, ee_link)
                    if arxiv_pdf_link: 
                        uni = find_sg_university(arxiv_pdf_link, search_list, sg_universities)
                        if uni:
                            info = author + title + booktitle 
                            writer1.writerow([uni, year, conf] + [info] + [biburl, ee_link])
                    else:
                        writer2.writerow(paper)
                except Exception as e:
                    print("search pdf failed:", e)
                    writer2.writerow(paper)
        with open('results/outliers.csv', 'w', encoding='UTF8', newline='') as f1, open('results/outliers_bak.csv', 'r', encoding='UTF8', newline='') as f2:
            reader = csv.reader(f2)
            writer = csv.writer(f1)
            for row in reader:
                writer.writerow(row)
        time.sleep(600)

if __name__ == '__main__':
    main()