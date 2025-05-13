import requests
from bs4 import BeautifulSoup
import os

#working 1 page ahead
for i in range(1,4):

    URL = f"https://www.teacheron.com/online-tutor-jobs?p={i}"
    # To sabotage bot restricted sites, header
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://google.com",
    }
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content,"html.parser")
    # print(soup.prettify())

    results = soup.find(id="tutorOrJobSearchItemList")
    # print(results)

    math_jobs = results.find_all("span", string=lambda text:"math" in text.lower())
    # print(math_jobs.text)

    math_job_cards = [span_element.parent.parent.parent.parent.parent for span_element in math_jobs]

    for job_card in math_job_cards:


        try:
            online_symbol = job_card.find("i", class_="fas fa-wifi")
            online_main = online_symbol.parent.parent.parent
            online_element = online_main.find_all("li")[1]
        except (IndexError,AttributeError):
            online_element = None
        try:
            title_element = job_card.find("span")
        except (IndexError,AttributeError):
            title_element = None
        try:
            price_element = job_card.find_all("li", attrs={"data-original-title": True})[3]
        except (IndexError, AttributeError):
            price_element = None  # or "N/A", or just skip
        try:
            url_link = job_card.find("a")["href"]
        except (IndexError,AttributeError):
            url_link = None


        width = os.get_terminal_size().columns 
        print('-' * width)
        if title_element != None:
            print("JOB       --> ",title_element.text.strip())
        if online_element != None:
            print("MODE      --> ",online_element["title"])    
        if price_element:
            print("PRICE     --> ",price_element["data-original-title"])
        if url_link != None:
            print("VISIT     --> ",url_link)

print()
print("<--SEARCH COMPLETE-->")