import schedule
import time
import requests, webbrowser
from twilio.rest import Client


def send_text():
    # Your Account SID from twilio.com/console
	account_sid = "your account id"
# Your Auth Token from twilio.com/console
	auth_token  = "your auth token"

	client = Client(account_sid, auth_token)

	message = client.messages.create(
    	to="your number", 
    	from_="twilio free trial number",
    	body="its down" + page.url)
	print ('gotem')

def send_text2():
    # Your Account SID from twilio.com/console
	account_sid = "your account sid"
# Your Auth Token from twilio.com/console
	auth_token  = "your auth token"

	client = Client(account_sid, auth_token)

	message = client.messages.create(
    	to="your phone number", 
    	from_="twilio phonenumber",
    	body="its still up!!" + page.url)
	print gotem



links = ['domain or social network profile you want to monitor']
   # finding the urls and http status 200 or 404 if 200 check page is still up 
   # if 404 or https://twitter.com/account/suspended  you can accept takedown 
for url in links:   
   page = requests.get(url)

   


   #blank = requests.get(h2.uiHeaderTitle)
   #print(page.status_code, page.url) 
   #print(blank.h2.uiHeaderTitle)
   # checks if pages are down or up opens up url in browser if page status code == 200

   if  page.status_code == 404 or page.url == 'https://twitter.com/account/suspended':
   	   print('gotem', page.url)
   	   send_text()
schedule.every(30).minutes.do(send_text)
#while true will run in console and check http status every 30 min 
while True:
	schedule.run_pending()
	time.sleep(30)

	


   
