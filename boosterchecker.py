#!/usr/bin/env python3

"""
# Boosterchecker.
# Script die checkt of bepaalde jaartallen aan de beurt zijn voor de Boostervaccinatie serie tegen COVID-19
# Als een jaartal aan de beurt is stuurt een bot een bericht in een telegram groep
# Tom Kluter
"""


import time
import requests

# Define constant variables
API_KEY = ""
GROUP_ID = ""
YEARS = [1999, 2000, 2001, 2002, 2003, 2004]
already_send = []
OVERIGE_TEXT = "en eerder zijn aan de beurt!\nInplannen op: planjeprik.nl\nEnkele tips: https://twitter.com/locuta/status/1475840225674997768?s=20"

# Last item in the list
LAST_ITEM = YEARS[-1]

while True:
	final = requests.get(f"https://user-api.coronatest.nl/vaccinatie/programma/booster/{LAST_ITEM}/NEE")
	final_response = final.json()

	if final_response["success"]:
		text = f"Geboortejaar {LAST_ITEM} {OVERIGE_TEXT}"
		message = f"https://api.telegram.org/bot{API_KEY}/sendMessage?chat_id={GROUP_ID}&text={text}"
		requests.get(message)
		break

	for year in YEARS:
		if year not in already_send:
			print(f"Jaren nog te gaan: {year}")
			request = requests.get(f"https://user-api.coronatest.nl/vaccinatie/programma/booster/{year}/NEE")
			response = request.json()

			if response['success']:
				text = f"Geboortejaar {year} {OVERIGE_TEXT}"
				message = f"https://api.telegram.org/bot{API_KEY}/sendMessage?chat_id={GROUP_ID}&text={text}"
				requests.get(message)
				already_send.append(year)

	print("120 seconds sleep....")
	time.sleep(120)
