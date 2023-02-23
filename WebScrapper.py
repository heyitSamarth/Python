from abc import abstractmethod
import requests ,bs4, re
import urllib.parse

class WebScrapper():
    def __init__(self):
        pass
    @abstractmethod
    def scrapping():
        pass



class Input():
    link=''
    def __init__(self):
        print("--------------------------------------------------------------------------\n")
        print("Welcome to Web Scrapper  \n")
        print("Get to 100 links  \n")
        input("Press enter to continue\n")
        while True:
            scrapping_word = input("Enter string u want to scrap ->>  ")
            if scrapping_word!='': 
                self.link="/search?q="+scrapping_word
                break
            else:
                print('Please Enter a Valid Word')
        
        


class CreateUrl():
    url=''
    def __init__(self,scrapping_link):
        self.url=f"https://www.google.co.in{scrapping_link}"
    


class Scrape():
    def __init__(self):
        pass
    def make_soup(self, url):
        result=requests.get(f"{url}","UTF-8")
        soup=bs4.BeautifulSoup(result.text,"html.parser")
        return soup

class LinkScrapper():    
    all_links=[]
    def __init__(self):
        pass
    def scrapping(self,soup,links): 
        special_divs = soup.find_all('div',{'class':"Gx5Zad"})# by analysing the lxml i found out ancor tag with link are in class Gx5Zad for every website 
        for divs in special_divs:
            divs_content=divs.find_all('a')# filltered all ankor tags 
            for link in divs_content:
                s=link.get('href') # took out link from the ankor tags
                self.all_links.append(s)
                if(re.search(r'/url', s)):#filtering urls and other data 
                    links.append(urllib.parse.unquote(s[7:].split("&sa")[0]))

class Process():
    all_links=[]
    def processer(self,url):
        scrape_object=Scrape()
        soup=scrape_object.make_soup(url.url)
        print(f"Scrapping from {url.url}")
        link_scrapper_object=LinkScrapper()
        link_scrapper_object.scrapping(soup,links)
        links.append(f"\nAll links from page")
        links.append(f"->>>>>> {url.url}")
        links.append(f"----------------------------------------------------------------------------------\n")
        self.all_links=link_scrapper_object.all_links
    def last_link(self):
        return self.all_links[-1].split("&sa")[0][:-2]

class Output():
    def __init__(self,links):
        f=open("all_links.txt","r+")
        for link in links:
            f.read()
            f.write(link+"\n")
        
class ImageScrapper():
    def __init__(self):
        pass
    def scrapping():
        pass

class IconScrapper():
    def __init__(self):
        pass
    def scrapping():
        pass


if __name__ == "__main__":
    links=[]
    first_link=Input()
    url=CreateUrl(first_link.link)
    p=Process()
    p.processer(url)
    pagechanging_link=p.last_link()
    for i in range(1,10):
        next_page=pagechanging_link+str(i)+"0"
        url=CreateUrl(next_page)
        p=Process()
        p.processer(url)
    Output(links)

