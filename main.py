import sys
import requests
import time
import threading
from bs4 import BeautifulSoup
from colorama import init, Fore
init(convert=True)
title = "N.A."
raiting = "N.A."
metascore = "N.A."
duration = "N.A."
release = "N.A."
genere = "N.A."
desc = "N.A."
director = "N.A."
cst = "N.A."
 


def loading():
    for i in range(0, 100):
        time.sleep(0.05)
        bar = "[" + "█" * i + " " * (100 - i) + "\b]"
        sys.stdout.write("\r"+"Fetching: " +  bar +str(i + 1)+ "%")
        sys.stdout.flush()


def printdata():
    print()
    print(Fore.LIGHTBLACK_EX + "Title: " + Fore.LIGHTRED_EX + title)
    print(Fore.LIGHTBLACK_EX + "IMDB Raiting: " + Fore.LIGHTYELLOW_EX + raiting + "/10")
    print(Fore.LIGHTBLACK_EX + "Meta Score: " + Fore.LIGHTYELLOW_EX + metascore + "/100")
    print(Fore.LIGHTBLACK_EX + "Duration: " + Fore.LIGHTCYAN_EX + duration)
    print(Fore.LIGHTBLACK_EX + "Release Date: " + Fore.LIGHTCYAN_EX + release)
    print(Fore.LIGHTBLACK_EX + "Genre: " + Fore.LIGHTBLUE_EX + genere)
    print(Fore.LIGHTBLACK_EX + "Description: " + Fore.LIGHTWHITE_EX + desc)
    print(Fore.LIGHTBLACK_EX + "Director: " + Fore.LIGHTGREEN_EX + director)
    print(Fore.LIGHTBLACK_EX + "Cast: " + Fore.LIGHTMAGENTA_EX + cst)

def soup_class_finder(soup_object, class_name, select_param, index):
    try:
        if select_param == None:
            return soup_object.find('div', class_=class_name).next_element.strip()
        elif index == None:
            return soup_object.find('div', class_=class_name).select(select_param)
        else:
            return soup_object.find('div', class_=class_name).select(select_param)[index].next_element.strip()
    except:
        return "N.A."
def scrapping():
    global title, raiting, metascore, duration, release, genere, desc, director, cst
    args = sys.argv[1:]
    movie = '+'.join(args)
    document = requests.get('https://www.imdb.com/find?ref_=nv_sr_fn&q='+movie+'&s=tt')
    soup = BeautifulSoup (document.content, 'html.parser')
    firstlink = soup.select("tr a")[0].get('href')
    movielink = requests.get("http://www.imdb.com" + firstlink)
    soup2 = BeautifulSoup (movielink.content, 'html.parser')
    title =soup_class_finder(soup2, "title_wrapper","h1",0)
    raiting =soup_class_finder(soup2, "ratingValue","strong span",0)
    metascore =soup_class_finder(soup2, "titleReviewBarItem","a div span",0)
    duration =soup_class_finder(soup2, "subtext","time",0)
    release =soup_class_finder(soup2, "subtext","a",-1)
    genre =soup_class_finder(soup2, "subtext","a",None)
    genere = ""
    for i in range(0,len(genre)-1):
        genere = genere + genre[i].get_text() + (", " if i + 1 !=len(genre)-1 else "")
    desc =soup_class_finder(soup2, "summary_text",None,-1)
    director =soup_class_finder(soup2, "credit_summary_item","a",0)
    try:  
        cast =  soup2.findAll('div', class_='credit_summary_item')[2].select("a")
        cst = ""
        for i in range(0,len(cast)-1):
            cst = cst + cast[i].get_text() + (", " if i + 1 !=len(cast)-1 else "")
    except:
        pass
    
if __name__ == '__main__':
    t1 = threading.Thread(target=loading, args=()) 
    t2 = threading.Thread(target=scrapping, args=())
    t1.start() 
    t2.start()
    t1.join()
    t2.join()
    printdata()
