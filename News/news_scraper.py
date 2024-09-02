# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 15:51:09 2024

@author: Max
"""

import requests
from bs4 import BeautifulSoup

# URL der Webseite
url = "https://en.wikipedia.org/wiki/Portal:Current_events/April_2005"

# Abrufen der Webseite
response = requests.get(url)

# Überprüfen, ob die Anfrage erfolgreich war
if response.status_code == 200:
    # Parsen des HTML-Inhalts
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Finden aller grünen Boxen (diese haben normalerweise die Klasse "vevent")
    green_boxes = soup.find_all("div", class_="vevent")
    
    # Liste für die Begriffe mit Hyperlinks
    linked_terms = []
    
    # Durch jede grüne Box iterieren
    for box in green_boxes:
        # Finden aller <a>-Tags innerhalb der Box
        links = box.find_all("a", href=True)
        # Filtern der Begriffe mit Hyperlinks und deren Texte
        for link in links:
            term = link.text.strip()
            if term:
                linked_terms.append(term)
    
    # Ausgabe der gefundenen Begriffe
    #for term in linked_terms:
     #   print(term)
else:
    print(f"Fehler beim Abrufen der Webseite: {response.status_code}")
    

search_string = "edit"

# Liste für die Indizes, wo der String gefunden wird
indices = [i for i, value in enumerate(linked_terms) if value == search_string]

