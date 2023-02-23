import requests,bs4,lxml,re
import urllib.parse
# this is used to decode urls 
#https://www.urldecoder.io/python/#:~:text=URL%20Decoding%20query%20strings%20or%20form%20parameters%20in%20Python%20(3,UTF%2D8%20encoding%20by%20default.

def start_scrapping(scrapping_word):
    links=[]
    f1.read()
    result=requests.get(f"https://www.google.co.in{scrapping_word}","UTF-8")
    soup=bs4.BeautifulSoup(result.text,"html.parser")
    f.write(soup.prettify())
    f.writelines("\n ")
    f.writelines("---------------------------new page----------------------------------"+ " \n")
    special_divs = soup.find_all('div',{'class':"Gx5Zad"})# by analysing the lxml i found out ancor tag with link are in class Gx5Zad for every website 
    for divs in special_divs:
        divs_content=divs.find_all('a')# filltered all ankor tags 
        for link in divs_content:
            s=link.get('href') # took out link from the ankor tags
            links.append(s)
            if(re.search(r'/url', s)):#filtering urls and other data 
                f1.write(urllib.parse.unquote(s[7:].split("&sa")[0])+"\n")#decoding url as python encode urls wich wile searching creates a issue
                
    f1.writelines(f"\nAll links from page \n")
    f1.writelines(f"->>>>>> https://www.google.co.in{scrapping_word}  \n")
    f1.writelines("---------------------------new links--------------------------------"+"\n")
    return links


if __name__ == "__main__":
    print("--------------------------------------------------------------------------\n")
    print("Welcome to Web Scrapper  \n")
    print("Get to 100 links  \n")
    input("Press enter to continue\n")

    scrapping_word=input("Enter string u want to scrap ->>  ")
    
    scrapping_word="/search?q="+scrapping_word#for first time will find on google
    print("\nScraping from "+"https://www.google.co.in"+scrapping_word)
    f = open("webpage_structure.txt","w+",encoding="utf-8")# cotain lxml of web page 
    f1 = open("all_links.txt","r+",encoding="utf-8")# will append all links in this 
    links=[]# will contain unformated links
    links=start_scrapping(scrapping_word)
    
    #while analysing lxml i found out last link in links list is for next page 
    #therefore
    next_page=links[-1].split("&sa")[0][:-2]#split as it contains extra values due to python scrapping then we pick first element then 
    #then i removed last two digits as it tell about page 01 for page 2 and 02 for page 3 and so on 
    for i in range(1,10):
        next_page_2=next_page+str(i)+"0"
        print("Scraping from "+"https://www.google.co.in"+next_page_2)
        links=start_scrapping(next_page_2)