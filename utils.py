import csv
import time
import json
import fitz
import argparse
import requests
from bs4 import BeautifulSoup
from googlesearch import search, get_random_user_agent
from difflib import SequenceMatcher


def get_parser():
    parser = argparse.ArgumentParser(description="Feature extraction with reid models")
    parser.add_argument(
        "--keyword",
        help="keyword to search papers",
    )
    parser.add_argument(
        "--find-sg",
        action='store_true',
        default=False,
        help="whether to find the papers of singapore universities"
    )
    return parser

def save_pdf(pdf_data, target_file):
    with open(target_file, 'wb') as f:
        f.write(pdf_data)

def save_json(json_data, target_file):
    with open(target_file, 'w') as f:
        json.dump(json_data, f)

def load_json(json_file):
    with open(json_file) as f:
        res = json.load(f)

def csv_length(csv_file):
    with open(csv_file, 'r') as f:
        csv_reader = csv.reader(f)
        csv_length = len(list(csv_reader))
        print("csv_length:", csv_length)
        return csv_length

def similarity(a, b):
    match = SequenceMatcher(None, a, b)
    return match.ratio()

def get_key (dict, value):
    return [k for k, v in dict.items() if value in v]

def parse_url(url, title):
    if ".pdf" in url.split('/')[-1]:
        return url
    if "proceedings.neurips.cc" in url and url.endswith(".html"):
        return url[:-13].replace('hash', 'file') + "Paper.pdf"
    if "doi.org" or 'ieeexplore.ieee.org' in url:
        try:
            thepage = requests.get("https://sci-hub.ee/" + url)
            soup = BeautifulSoup(thepage.text, "html.parser")
            pdf_link = soup.find(id='pdf').get("src") if soup.find('id=pdf') else 
            if "http" not in pdf_link:
                return "https:" + pdf_link
            else:
                return pdf_link
        except Exception as e:
            print("Sci-Hub Exception:", e)
            print(url)
            time.sleep(5)
    if "openaccess.thecvf.com" in url and url.endswith(".html"):
        try:
            soup = BeautifulSoup(requests.get(url).text, "html.parser")
            searched_title = soup.find(id="papertitle").text.strip().lower()
            if similarity(title, searched_title) > 0.6:
                return "https://openaccess.thecvf.com/" + soup.find('a', string='pdf').get('href').replace("../", "")
            else:
                print(f"OPENACCESS NOT MATCHED: {title} -- {searched_title}")
        except Exception as e:
            print("OPENACCESS Exception:", e)
            time.sleep(5)
    if 'arxiv.org/abs' in url:
        try:
            soup = BeautifulSoup(requests.get(url).text, "html.parser")
            searched_title = ' '.join(soup.title.text.lower().split()[1:])
            if similarity(title, searched_title) > 0.8:
                return url.replace('abs', 'pdf')+'.pdf'
            else:
                print(f"ARXIV NOT MATCHED: {title} -- {searched_title}")
        except Exception as e:
            print("ARXIV Exception:", e)
            time.sleep(5)
    if 'aaai.org' in url or 'index.php/AAAI' in url:
        try:
            soup = BeautifulSoup(requests.get(url).text, "html.parser")
            searched_title = soup.find(class_="page_title").text.strip().lower()
            if similarity(title, searched_title) > 0.6:
                return soup.find(class_="obj_galley_link pdf").get("href")
            else:
                print(f"AAAI NOT MATCHED: {title} -- {searched_title}")
        except AttributeError as e:
            thepage = requests.get(url.replace('view', 'viewPaper'))
            soup = BeautifulSoup(thepage.text, "html.parser")
            searched_title = soup.find(id="title").text.strip().lower()
            if similarity(title, searched_title) > 0.6:
                print("AAAI: find it again")
                return soup.find("meta", attrs= {'name': 'citation_pdf_url'}).get("content")
            else:
                print(f"AAAI NOT MATCHED: {title} -- {searched_title}")
        except Exception as e:
            print("AAAI Exception:", e)
            time.sleep(5)

def search_pdf_link(title, conf, url):
    time.sleep(1)
    pdf_link = None
    user_agent = get_random_user_agent()
    pdf_link = parse_url(url, title)
    if pdf_link:
        return pdf_link
    search_string = ' '.join([title, conf, "pdf"])
    for j in search(search_string, num=3, stop=3, pause=2.0, user_agent=user_agent):
        pdf_link = parse_url(j, title)
        if pdf_link:
            return pdf_link
                 
    print(f"NOT SEARCHED: {title}")
    print(conf, url)
    return pdf_link

def find_sg_university(path, search_list, universities):
    print("path:", path)
    uni = None
    for _ in range(3):
        try:
            data = requests.get(path).content
            doc = fitz.open(stream=data, filetype="pdf")
            break
        except RuntimeError:
            save_pdf(data, "pdfs/outlier.pdf")
            doc = fitz.open("pdfs/outlier.pdf")
            break
        except Exception as e:
            print(repr(e), "the pdf can not be parsed.")
    page = doc.loadPage(0)
    for word in search_list:
        x = page.search_for(word) #list
        hit = ''
        if len(x) > 0:
            for i in range(len(x)):
                hit_item = page.get_textbox(x[i])
                print("hit_item:", hit_item)
                hit += hit_item
                if hit in search_list:
                    print("hit:", hit)
                    uni = get_key(universities, hit)[0]
                    print("uni:", uni)
                    return uni