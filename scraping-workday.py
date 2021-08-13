from bs4 import BeautifulSoup
import re

#THIS IS JOKE CODE!!!

plist = []
alist = []
target_url = ""####Please Input Your Like Girl
r = requests.get(target_url)
soup = BeautifulSoup(r.content, 'lxml')
s = soup.find_all("div", class_="go2")
ul = soup.find_all("dt")
for p in s:
    p = str(p)
    p = de.sub("", p)
    p = p.replace("\n", "")
    p = p.replace(" ", "")
    plist.append(p)
for a in ul[28:36]:
    a = str(a)
    a = a.replace("\n", "")
    a = a.replace(" ", "")
    alist.append(a)
for i in range(len(plist)):
    b = alist.pop(0)
    c = plist.pop(0)
    b = re.sub(r'[a-z]', "", b)
    b = re.sub('\n', "", b)
    b = b.replace("</dt>", "")
    b = b.replace("<", "")
    b = b.replace(">", "")
    b = b.replace("\"", "")
    b = b.replace("=", "")
    b = b.replace(" ", "")
    b = b.rstrip("/")
    c = re.sub(r'[a-z]', "", c)
    c = re.sub('\n', "", c)
    c = c.replace("</dt>", "")
    c = c.replace("<", "")
    c = c.replace(">", "")
    c = c.replace("\"", "")
    c = c.replace("=", "")
    c = c.replace(" ", "")
    o = c + b
    o = o.replace(" ", "")
    print(o)