from tkinter import *
import webbrowser
win = Tk()
url = "https://finance.yahoo.com/quote/TSLA/"
url2 = "https://finance.yahoo.com/quote/%5EGSPC/"
def tsla():
    open(webbrowser.open_new(url))
def sp():
    open(webbrowser.open_new(url2))
win.title("Stonk!")
win.geometry("600x400")
win.resizable(width=False, height=False)
font ="Times New Roman"
canva = Canvas(win,height =400,width=600,bg='grey58')
canva.create_text(35,20,font=(font, 20,"underline"),text="TSLA")
canva.create_text(70,44,font=(font, 10),text="Tesla, CEO Elon Musk")
canva.create_text(68,120,font=(font, 20,"underline"),text="INX IDXSP")
canva.create_text(28,145,font=(font, 10),text="S&P 500")
but = Button(canva,text="TSLA info",command= tsla,bg="gray67")
but.place(x=70,y=7)
but2 = Button(canva,text="S&P info",command= sp,bg="grey67")
but2.place(x=132,y=108)

from bs4 import BeautifulSoup
import requests

res = requests.get(url)
res2 = requests.get(url2)
soup = BeautifulSoup(res.text,"lxml")
soup2 = BeautifulSoup(res2.text,"lxml")
s=soup.find('div',{"class":"My(6px) Pos(r) smartphone_Mt(6px)"}).find("span").text
z=soup.find('div',{"class":"My(6px) Pos(r) smartphone_Mt(6px)"}).find_all("span")[1].text
n=soup2.find('div',{"class":"My(6px) Pos(r) smartphone_Mt(6px)"}).find("span").text
m=soup2.find('div',{"class":"My(6px) Pos(r) smartphone_Mt(6px)"}).find_all("span")[1].text

if "+" in z:
    hah = "green"
else:
    hah = "red"
if "+" in m:
    ha = "green"
else:
    ha ="red"
canva.create_text(100,79,font=(font,40),text=s)
canva.create_text(290,72,font=("Arial bold",19),text=z,fill=hah)
canva.create_text(100,180,font=(font,40),text=n)
canva.create_text(290,173,font=("Arial bold",19),text=m,fill=ha)

urlzz = "https://www.investopedia.com/financial-term-dictionary-4769738"
reszz = requests.get(urlzz)
soup = BeautifulSoup(reszz.text,"lxml")
sss=soup.find_all("div",{"class":"comp tod__article mntl-block"})[0].text
canva.create_text(82,225,font=("Ariel bold",15),text="Term of the day :",fill="black")
canva.create_text(300,310,font=("Ariel",15),text=sss,fill="white",width =605)

url5 = "https://www.marketwatch.com/"
url6 = "https://seekingalpha.com/"
url7 = "https://www.investopedia.com/"
url8 = "https://vnexpress.net/kinh-doanh"
def marketwatch():
    open(webbrowser.open_new(url5))
def seekingalpha():
    open(webbrowser.open_new(url6))
def investopia():
    open(webbrowser.open_new(url7))
def vnexpress():
    open(webbrowser.open_new(url8))
but5 = Button(canva,text="Market Watch", command=marketwatch,bg="gray67")
but5.place(x=400,y=50)
but6 = Button(canva,text="Seeking Alpha", command=marketwatch,bg="gray67")
but6.place(x=400,y=75)
but7= Button(canva,text="Investopedia", command=investopia,bg="gray67")
but7.place(x=400,y=100)
but8= Button(canva,text="Vnexpress Business", command=vnexpress,bg="gray67")
but8.place(x=400,y=125)
canva.create_text(480,30,text="Economic News :",font=(font,20))

canva.pack()
win.mainloop()
