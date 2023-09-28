# NOTIFICATION  WEATHER #

# Get Weather 
# https://www.thepythoncode.com/code/extract-weather-data-python

# send Webhook Message SLACK
# https://api.slack.com/messaging/webhooks

# SCHEDULER
# https://www.jcchouinard.com/python-automation-using-task-scheduler/

# jaumendes
# 16 05 2023
# Modulo 4 - WorkShop para Jovens Mercado Trabalho 
# Import the following modules
# $ pip install --upgrade pip
# $ pip install requests, bs4, schedule, tqdm

import json
import sys
import requests
import base64

import re

from bs4 import BeautifulSoup as bs
import requests

from datetime import datetime

def get_current_time():
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

refs = []

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
# US english
LANGUAGE = "en-US,en;q=0.5"

def get_weather_data(url):
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html = session.get(url)
    # create a new soup
    soup = bs(html.text, "html.parser")
    # store all results on this dictionary
    result = {}
    # extract region
    result['region'] = soup.find("div", attrs={"id": "wob_loc"}).text
    # extract temperature now
    result['temp_now'] = soup.find("span", attrs={"id": "wob_tm"}).text
    # get the day and hour now
    result['dayhour'] = soup.find("div", attrs={"id": "wob_dts"}).text
    # get the actual weather
    result['weather_now'] = soup.find("span", attrs={"id": "wob_dc"}).text
    # get the precipitation
    result['precipitation'] = soup.find("span", attrs={"id": "wob_pp"}).text
    # get the % of humidity
    result['humidity'] = soup.find("span", attrs={"id": "wob_hm"}).text
    # extract the wind
    result['wind'] = soup.find("span", attrs={"id": "wob_ws"}).text
    # get next few days' weather
    next_days = []
    days = soup.find("div", attrs={"id": "wob_dp"})
    for day in days.findAll("div", attrs={"class": "wob_df"}):
        # extract the name of the day
        day_name = day.findAll("div")[0].attrs['aria-label']
        # get weather status for that day
        weather = day.find("img").attrs["alt"]
        temp = day.findAll("span", {"class": "wob_t"})
        # maximum temparature in Celsius, use temp[1].text if you want fahrenheit
        max_temp = temp[0].text
        # minimum temparature in Celsius, use temp[3].text if you want fahrenheit
        min_temp = temp[2].text
        next_days.append({"name": day_name, "weather": weather, "max_temp": max_temp, "min_temp": min_temp})
    # append to result
    result['next_days'] = next_days
    return result
    

def get_tempo_from_localidade(localidade):
    #if __name__ == "__main__":
    URL = "https://www.google.com/search?lr=lang_en&ie=UTF-8&q=weather"
    import argparse
    parser = argparse.ArgumentParser(description="Quick Script for Extracting Weather data using Google Weather")
    parser.add_argument("region", nargs="?", help="""Region to get weather for, must be available region.
                                        Default is your current location determined by your IP Address""",
                        default=localidade)
    # parse arguments
    args = parser.parse_args()
    region = args.region
    if region:
        region = region.replace(" ", "+")
        URL += f"+{region}"
    # get data
    data = get_weather_data(URL)
    # print data
    print("Weather for:", data["region"])
    print("Now:", data["dayhour"])
    print(f"Temperature now: {data['temp_now']}°C")
    print("Description:", data['weather_now'])
    print("Precipitation:", data["precipitation"])
    print("Humidity:", data["humidity"])
    print("Wind:", data["wind"])
    
    # BODY #
    
    refs= ''
    #refs += "Weather for : "+ data["region"]
    #refs += "\nNow : "+ data["dayhour"]
    refs += f"\nTemperature now : {data['temp_now']}°C"
    #refs +="\nDescription : "+ data['weather_now']
    refs += "\nPrecipitation : "+ data["precipitation"]
    #refs += "\nHumidity : "+ data["humidity"]
    refs += "\nWind : "+ data["wind"]
    vento = data["wind"]
    vento = vento.split(" ")[0]
    temp = data['temp_now']
    if int(temp) > 15:
        refs += "\nAgradavel Temperatura"
    else:
        refs += "\nTemperatura baixa"
    if int(vento) < 15 :
        refs += "\nVento Agradável"
    else:
        refs += "\nVento moderado"
   
    return refs, str(vento), str(temp)
    
    
    #for dayweather in data["next_days"]:
    #    print("="*40, dayweather["name"], "="*40)
     #   print("Description:", dayweather["weather"])
      #  print(f"Max temperature: {dayweather['max_temp']}°C")
       # print(f"Min temperature: {dayweather['min_temp']}°C")


########################### GET WEATHER V 2
def remove_html(string):
    
    regex = re.compile(r'<[^>]+>')
    return regex.sub('', string)

def get_mares_description(location):
    
    import requests
    from bs4 import BeautifulSoup

    url = "https://tabuademares.com/pt/porto/"+location
    urlx = 'http://worldagnetwork.com/'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    #content = soup.find_all(class_='grafico_estado_actual_texto1')
    contents = soup.find_all(class_="txt_descripcion")
    mail_content = str(contents)
    print (mail_content)
    olha = mail_content.split("Hoje  terça-feira")[1]
    
    ole = olha.split("txt_descripcion")[0]
    print (ole[1:-16])


    mail_content = ole[1:-16]
    #nnn = mail_content.split("preia-mar")[1]

    


    text=mail_content
    new_text=remove_html(mail_content)
    print(f"Text without html tags: {new_text}")
    return new_text


###########################
def send_slack_notif(mensagem):
    
#if __name__ == '__main__':
	# Webhooks URL
	#url = "https://hooks.slack.com/services/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"
	url = "https://hooks.slack.com/services/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"
	
	# Message you wanna send
	
	
	# Title
	title = (f"Jaumendes Bot :satellite:")
	
	# All slack data
	slack_data = {

		"username": "Testing",
		"attachments": [
			{
				"color": "#FF0000",
				"fields": [
					{
						"title": title,
						"value": mensagem,
						"short": "false",

					}
				]
			}
		]
	}
	
	# Size of the slack data
	byte_length = str(sys.getsizeof(slack_data))
	headers = {'Content-Type': "application/json",
			'Content-Length': byte_length}
	
	# Posting requests after dumping the slack data
	response = requests.post(url, data=json.dumps(slack_data), headers=headers)
	
	# Post request is valid or not!
	if response.status_code != 200:
		raise Exception(response.status_code, response.text)
	print ("SENT NOTIF TO SLACK")

# slackig
#from slack_webhook import Slack

#slack = Slack(url='https://hooks.slack.com/services/T00/B00/XXX')
#slack.post(text="Hello, world.")
#///
"""
slack = Slack(url='https://hooks.slack.com/services/T00/B00/XXX')
slack.post(text="Robert DeSoto added a new task",
    attachments = [{
        "fallback": "Plan a vacation",
        "author_name": "Owner: rdesoto",
        "title": "Plan a vacation",
        "text": "I've been working too hard, it's time for a break.",
        "actions": [
            {
                "name": "action",
                "type": "button",
                "text": "Complete this task",
                "style": "",
                "value": "complete"
            },
            {
                "name": "tags_list",
                "type": "select",
                "text": "Add a tag...",
                "data_source": "static",
                "options": [
                    {
                        "text": "Launch Blocking",
                        "value": "launch-blocking"
                    },
                    {
                        "text": "Enhancement",
                        "value": "enhancement"
                    },
                    {
                        "text": "Bug",
                        "value": "bug"
                    }
                ]
            }
        ]
    }]
)"""
# SEND ANOTHER

def send_slack_message(payload, webhook):
    """Send a Slack message to a channel via a webhook. 
    
    Args:
        payload (dict): Dictionary containing Slack message, i.e. {"text": "This is a test"}
        webhook (str): Full Slack webhook URL for your chosen channel. 
    
    Returns:
        HTTP response code, i.e. <Response [503]>
    """

    return requests.post(webhook, json.dumps(payload))



def check_vento():
    corpo, vent , temperature = get_tempo_from_localidade("Povoa de Varzim")
    webhook = "https://hooks.slack.com/services/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"
    payload = {"text": str(corpo)}

    if int(vent) < 18 or int(temperature)> 18 :
        send_slack_message(payload, webhook)
        print ("Está bom pra caminhar !!! Vento : ", vent)
    else:
        print ("Muito vento: "+vent + "\nLow Temp : "+ temperature)

# SEND MESSAGE WITH PY TO SLACK
#

def use_channel_send(channel_id,texto):
    import SlackApi
    # ID of channel you want to post message to
    

    try:
        # Call the conversations.list method using the WebClient
        result = client.chat_postMessage(
            channel=channel_id,
            text=texto
            # You could also use a blocks[] array to send richer content
        )
        # Print result, which includes information about the message (like TS)
        print(result)

    except SlackApiError as e:
        print(f"Error: {e}")
#use_channel_send("Testing","Hello world!")        
# BUILD MESSAGES #


# SEND WITH SLACK 


def send_to_streams():
    messages = []
    messages.append(get_mares_description("povoa-de-varzim"))
    messages.append(get_tempo_from_localidade("Povoa de Varzim"))

    for i in messages:
        send_slack_notif(i)
        print("####   Notification sent to slack Testing ####\n")


# SEND WITH GMAIL


# SCHEDULE JOBS
import schedule
import time

def job():
    print("SCHEDULE working...")

#schedule.every(10).seconds.do(job)
schedule.every(15).minutes.do(check_vento)
schedule.every().hour.do(check_vento)
#schedule.every().day.at("10:30").do(job)
#schedule.every(5).to(10).minutes.do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)
#schedule.every().day.at("12:42", "Europe/Amsterdam").do(job)
#schedule.every().minute.at(":17").do(job)

def job_with_argument(name):
    print(f"I am {name}")

#schedule.every(10).seconds.do(job_with_argument, name="Peter")
from time import sleep
from tqdm import tqdm
num = 10

while True:
    #print ("SCHEDULE working...")
    check_vento()
    #send_to_streams()
    schedule.run_pending()
    get_current_time()
    time.sleep(900)
    
    #for i in tqdm(range(60)):
    #    sleep(1)
# SEND IMG TO SLACK


