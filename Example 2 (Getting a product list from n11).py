# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 14:18:08 2021

@author: User
"""

from lxml import html
import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/telefon-ve-aksesuarlari/cep-telefonu?pg=1"

r=requests.get(url)
#print(r.status_code)

soup = BeautifulSoup(r.content,"html.parser")
urunler= soup.find_all("li",attrs={"class":"column"})
for urun in urunler:
    urunAdı=urun.a.get("title")
    urunLink=urun.a.get("href")
    print("#"*30)
    print(urunAdı,sep=("\n"))
    print("#"*30)
    print(sep=("\n"))
    urun_r=requests.get(urunLink)
    urun_soup=BeautifulSoup(urun_r.content,"html.parser")
    ozellikler = urun_soup.find("div",attrs={"class":"unf-prop-context"}).ul.find_all("li")
    
    for ozellik in ozellikler:
        
        ozellikAdı =ozellik.find("p",attrs={"class":"unf-prop-list-title"}).text
        ozellikNe=ozellik.find("p",attrs={"class":"unf-prop-list-prop"}).text
        
        print("{} ===== {}".format(ozellikAdı,ozellikNe))
    