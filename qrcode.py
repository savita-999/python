#!/usr/bin/python3
import pyqrcode
urllist=[]
num=input("enter the number of url")
x=int(num)
for i in range(x):
        n=input("enter the url of which qr code u want to generate")
        urllist.append(n)
        print(urllist)
        for j in n:
                url=pyqrcode.create(n)
                url.svg(n+".svg",scale=3)

                                     
