# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 15:51:09 2024

@author: Max
"""

import requests
from bs4 import BeautifulSoup
from datetime import date
import pickle 
import numpy as np 

class news:
    def __init__(self):
        self.when_scraped = date.today();
        
################################################################################


def save_object(obj, filename):
    with open(filename, 'wb') as outp:  # Overwrites any existing file.
        pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)

def load_object(filename):
    
    NEWS = open(filename, 'rb')
    NEWS = pickle.load(NEWS)
    
    return NEWS
        

def scrape(url):


    # Abrufen der Webseite
    response = requests.get(url)

    # Überprüfen, ob die Anfrage erfolgreich war
    if response.status_code == 200:
        # Parsen des HTML-Inhalts
        soup = BeautifulSoup(response.content, "html.parser")
    
        # Finden aller grünen Boxen (div mit der Klasse 'vevent')
        green_boxes = soup.find_all("div", class_="vevent")
    
        # Liste für die extrahierten Sätze
        sentences = []
    
        # Durch jede grüne Box iterieren
        for box in green_boxes:
            # Finden der Listenpunkte (li-Elemente)
            list_items = box.find_all("li")
            for item in list_items:
                # Text des Listenelements extrahieren
                sentence = item.get_text().strip()
                if sentence:
                    sentences.append(sentence)
    

    else:
                print(f"Fehler beim Abrufen der Webseite: {response.status_code}")
                
    return sentences


################################################################################

#Please select the years to scraoe 
    
################################################################################
start = 2004
stop =  2010
################################################################################

base_url = 'https://en.wikipedia.org/wiki/Portal:Current_events/'

################################################################################

years = np.arange(start, stop+1, 1); 
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


NEWS = news()

#scrapy = np.array(scrape(base_url+months[1]+'_'+str(years[1])))
#scrapy = np.delete(scrapy,  np.where((scrapy == "edit") | (scrapy == "watch") | (scrapy == "history")))

a = np.zeros((1,1), dtype = np.dtype('<U863'))

for k in years: 
    
    a = np.zeros((1,1), dtype = np.dtype('<U863'))
    
    for j in range(12):
        
        scrapy = np.array(scrape(base_url+months[j]+'_'+str(k)), dtype = str)
        scrapy = np.delete(scrapy,  np.where((scrapy == "edit") | (scrapy == "watch") | (scrapy == "history")))
        scrapy = np.reshape(scrapy, (scrapy.shape[0],1))
        
        if a.shape[0] < scrapy.shape[0]:
            a_old = a
            a = np.zeros((scrapy.shape[0],j+1), dtype = np.dtype('<U863'))
            a[0:a_old.shape[0],0:a_old.shape[1]] = a_old
    
        a = np.append(a,np.zeros((a.shape[0],1), dtype = np.dtype('<U863')), 1)
        a[0:scrapy.shape[0],j:j+1] = scrapy
        


    setattr(NEWS, str(k), np.delete(a,0,1))
            
        

filename = 'news.pkl'

save_object(NEWS, filename)




                 