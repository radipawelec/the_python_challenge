from bs4 import BeautifulSoup
import requests
import re


# 12345 --> then 16044 /2 --> 8022 afrter   --> 63579 --> (66831 --> peak.html)


#if not cyfry!!!

def vist_page(url_end):
    while(True):
        url_end=url_end
        link = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(url_end)
        page_response = requests.get( link, timeout=5 ).text
        page_content = BeautifulSoup( page_response, 'lxml' )
        result = re.findall('[0-9]', str(page_content))
        url_end = ""
        for i in result:
            url_end += i
        print(url_end)
        # print(page_content)
vist_page(63579)