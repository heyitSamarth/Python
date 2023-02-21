import requests,bs4,lxml
f = open("link.txt","w+",encoding="utf-8")
s=input("to be searched")
result=requests.get(f"https://www.google.co.in/search?q={s}","UTF-8")
soup=bs4.BeautifulSoup(result.text,"lxml")

# for i in soup.select('div'):
#     f.writelines(i.contents)
f.write(soup.prettify())




special_divs = soup.find_all('div',{'class':"Gx5Zad"})


for divs in special_divs:
    divs_content=divs.find_all('a')
    for link in divs_content:
    # f.writelines(divs.get('href')+"\n")
        print(link.get('href')+"\n")

# f.close()