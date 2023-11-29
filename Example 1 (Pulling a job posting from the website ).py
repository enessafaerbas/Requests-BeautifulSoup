# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 10:41:48 2021

@author: User
"""

from lxml import *
import requests
from bs4 import BeautifulSoup

url="https://www.python.org/jobs"
r=requests.get(url)
soup= BeautifulSoup(r.content,"html.parser")
pages=len(soup.find_all("ul",attrs={"class":"pagination"})[0].find_all("li"))-2
totaljobs=0
for pageNumber in range(1,pages+1):
    pageRequests= requests.get("https://www.python.org/jobs/?page="+str(pageNumber))
 #  print(pageRequests.url)
    pageSource=BeautifulSoup(pageRequests.content,"html.parser")
    jobs=pageSource.find("div",attrs={"class":"row"}).ol.find_all("li")
    # TÜM İŞLERİ ÇEKTİK, DÖNGÜ İLE İLAN DETAYLARINI ALALIM.
    for job in jobs:
        name=job.h2.find("a").text
        location=job.find("span",attrs={"class":"listing-location"}).text
        company=job.find("span",attrs={"class":"listing-company-name"}).br.next.strip()
        publish_time=job.find("time").text
        totaljobs+=1
        print(name,company,location,publish_time,sep="\n")
        print("-"*60)
print("Toplam {} adet iş bulundu.".format(totaljobs))