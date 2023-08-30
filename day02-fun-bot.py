import requests
import json

import schedule

def jokes(f):
    
    data = requests.get(f)
    tt = json.loads(data.text)
    return tt





def send_slack_message(payload, webhook):
    """Send a Slack message to a channel via a webhook. 
    
    Args:
        payload (dict): Dictionary containing Slack message, i.e. {"text": "This is a test"}
        webhook (str): Full Slack webhook URL for your chosen channel. 
    
    Returns:
        HTTP response code, i.e. <Response [503]>
    """

    return requests.post(webhook, json.dumps(payload))



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
import schedule
import time

def job():
    print("SCHEDULE working...")

	
def animate_me():
    corpo = ''
    #corpo, vent , temperature = get_tempo_from_localidade("Povoa de Varzim")
    f = r"https://official-joke-api.appspot.com/random_ten"
    all_ten = jokes(f)
    webhook = "https://hooks.slack.com/services/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"

    for i in all_ten:
        if i["type"] == "programming":
            print(i["setup"])
            print(i["punchline"], "\n")
            corpo += str(i["setup"]) + '\n'
            corpo += str(i["punchline"])
            
            

            payload = {"text": corpo}

            send_slack_message(payload, webhook)
                  
            print ("enviada anedota:\n" + corpo)


animate_me()







        
