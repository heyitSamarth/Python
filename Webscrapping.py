import requests,bs4,lxml,re
# def check_links():
#     re.select()
#     f1.write(link.get('href')+"\n")




f = open("webpage.txt","w",encoding="utf-8")
f1 = open("link.txt","w+",encoding="utf-8")
all_links=[]
s=input("to be searched")
result=requests.get(f"https://www.google.co.in/search?q={s}","UTF-8")
soup=bs4.BeautifulSoup(result.text,"lxml")
f.write(soup.prettify())
special_divs = soup.find_all('div',{'class':"Gx5Zad"})
for divs in special_divs:
    divs_content=divs.find_all('a')
    for link in divs_content:
        s=link.get('href')
        all_links.append(s)
        if(re.search(r'/url', s)):
            f1.write(s[7:].split("&sa")[0]+"\n")
            

        # print(link.get('href')+"\n")
# check_links()
next_page=all_links[-1].split("&sa")[0][:-2]
print(next_page)
i=2
result2=requests.get(f"https://www.google.co.in{next_page}{i}0","UTF-8")
soup2=bs4.BeautifulSoup(result2.text,"lxml")
f.write(soup2.prettify())
special_divs = soup2.find_all('div',{'class':"Gx5Zad"})
for divs in special_divs:
    divs_content=divs.find_all('a')
    for link in divs_content:
        s=link.get('href')
        all_links.append(s)
        if(re.search(r'/url', s)):
            f1.write(s[7:].split("&sa")[0]+"\n")
