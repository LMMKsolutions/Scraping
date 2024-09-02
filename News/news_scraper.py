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
    
    # Ausgabe der extrahierten Sätze
    for sentence in sentences:
        print(sentence)
else:
    print(f"Fehler beim Abrufen der Webseite: {response.status_code}")

