# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 07:38:59 2024

@author: Max
"""

from bs4 import BeautifulSoup
from lxml import html
import requests




##### login? #####

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}

sess = requests.Session()


home_page = sess.get('https://www.trademap.org/Index.aspx', headers = headers)

soup = BeautifulSoup(home_page.content, "html.parser")

print(soup.text)
rvt = soup.find("input", attrs={"name" : "__RequestVerificationToken"})['value']


request_url = ('https://idserv.marketanalysis.intracen.org/Account/Login?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3DTradeMap%26scope%3Dopenid%2520email%2520profile%2520offline_access%2520ActivityLog%26redirect_uri%3Dhttps%253A%252F%252Fwww.trademap.org%252FLoginCallback.aspx%26state%3D270f9c5b4ef641f5b673844f9b87718f%26response_type%3Dcode%2520id_token%26nonce%3Df5558e44fdda40f3b8298ee3138961b0%26response_mode%3Dform_post')
#secure_url =

payload = {'ReturnUrl': '/connect/authorize/callback?client_id=TradeMap&scope=openid%20email%20profile%20offline_access%20ActivityLog&redirect_uri=https%3A%2F%2Fwww.trademap.org%2FLoginCallback.aspx&state=2d9d8f46dcde40aaa5dcbadfaa5af983&response_type=code%20id_token&nonce=fef8c1efcead4d059717125731d55530&response_mode=form_post', 'Username': 'lorenz.meyer@tu-ilmenau.de','Password': 'LMMK','button': 'login','_RequestVerificationToken': 'CfDJ8Ka7ty-C3AJMlEBbf_gx4irfJA_mZs5kj9f9FBoM-IA3aiZU6g-Qk6pEOWjUSppNkdziCA1OYJ22vDK9RWHuuEAkycwSoXm5QbD2f0O3TN7v05EnPEIwp2yUoUqKBQVjYIVgFJfBLUsXYlKDLPY_Pw0','RememberLogin': 'false'}

r = requests.post(request_url, data = payload)

print(r.text)


######## send post request after: Index.aspx 'Method:POST' ##############

