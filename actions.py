from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
	
	def filterOnBudget(self,budget,restaurantList):
		min=0
		max=10000

		cost = budget

		if(cost==1):
			min=0
			max=300
		elif(cost==2):
			min=300
			max=700
		elif(cost==3):
			min=700
			max=10000
		else:
			min=0
			max=10000

		c=0
		first_five=""
		first_five_mail=""
		next_five=""
		top_ten=""
		
		newlist = sorted(restaurantList, key=lambda res: float(res['restaurant']['user_rating']['aggregate_rating']), reverse=True)
		for res in newlist:
			if(res['restaurant']['average_cost_for_two']<max and res['restaurant']['average_cost_for_two'] >min ): 
				if(c<5):
					first_five=first_five+res['restaurant']['name']+ " in "+ res['restaurant']['location']['address']+ " has been rated "+res['restaurant']['user_rating']['aggregate_rating'] +  "\n\n"
					first_five_mail=first_five_mail+res['restaurant']['name']+ " in "+ res['restaurant']['location']['address']+ " has been rated "+res['restaurant']['user_rating']['aggregate_rating']+"." + "\n And average cost for two is "+ str(res['restaurant']['average_cost_for_two']) +"\n\n"	     
				else:
					next_five=next_five+res['restaurant']['name']+ " in "+ res['restaurant']['location']['address']+ " has been rated "+res['restaurant']['user_rating']['aggregate_rating']+"." + "\n And average cost for two is "+ str(res['restaurant']['average_cost_for_two']) +"\n\n" 	     
				c=c+1
				if(c==10):
					break
		
		if(c==0):
			first_five= "Sorry, we could not find any matching restaurants."
			top_ten== "Sorry, we could not find any matching restaurants."
		elif(c<5):
			first_five=first_five + "Only "+str(c) + " results found."
			top_ten=first_five_mail
		elif(c>5 and c<=10):
			top_ten=first_five_mail+next_five

		html="""
		<html>
		<head>
		<style>
		</style>
		</head>
		<body>
		<p>Hi!</p>
		<p>Thanks for using FoodieBot. Here are our top recommendations:</p>	
		<pre>"""
		html=html + top_ten+ "</pre><p>Bon, Appetit..!!</p><p>FoodieBot</p></body></html>"
		global resp_mail
		resp_mail = html

		return first_five

		
	def run(self, dispatcher, tracker, domain):
		print("Running Restaurant Search")
		config={ "user_key":"edc113a4b46e63420883a00b873fa61a"}
		zomato = zomatopy.initialize_app(config)
		global loc
		loc = tracker.get_slot('location')
		search_results = tracker.get_slot('search_results')
		global cuisine
		cuisine = tracker.get_slot('cuisine').lower()
		budget=tracker.get_slot('price')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'Chinese':25, 'Mexican':73,'Italian':55,'American':1,'North Indian':50,'South Indian':85}
		budget_dict={'low':1,'mid':2,'high':3}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 50)
		d = json.loads(results)
		response=""
		if d['results_found'] == 0:
			response= "Sorry, we could not find any matching restaurants."
			search_results= False
		else:
			response=self.filterOnBudget(budget_dict.get(budget),d['restaurants'])
			if response=="Sorry, we could not find any matching restaurants." :
				search_results=False
			else:
				search_results= True
		
		dispatcher.utter_message("-----"+"\n"+response)
		return [SlotSet('location',loc),SlotSet('search_results',search_results)]



class ActionCheckLocation(Action):
	def name(self):
		return 'action_check_location'
		
	def run(self, dispatcher, tracker, domain):
		
		print("Validating Location")
		list_loc = ["ahmedabad","bangalore","chennai","delhi","hyderabad","kolkata","mumbai","pune","agra","ajmer","aligarh","allahabad","amravati","amritsar",
					"asansol","aurangabad","bareilly","belgaum","bhavnagar","bhiwandi","bhopal","bhubaneswar","bikaner","bokaro steel city","chandigarh","coimbatore",
					"cuttack","dehradun","dhanbad","durg-bhilai nagar","durgapur","erode","faridabad","firozabad","ghaziabad","gorakhpur","gulbarga","guntur","gurgaon",
					"guwahati","hubli-dharwad","indore","jabalpur","jaipur","jalandhar","jammu","jamnagar","jamshedpur","jhansi","jodhpur","kannur","kanpur","kakinada",
					"kochi","kottayam","kolhapur","kollam","kota","kozhikode","kurnool","lucknow","ludhiana","madurai","malappuram","mathura","goa","mangalore","meerut",
					"moradabad","mysore","nagpur","nanded","nashik","nellore","noida","palakkad","patna","pondicherry","raipur","rajkot","rajahmundry","ranchi","rourkela",
					"salem","sangli","siliguri","solapur","srinagar","sultanpur","surat","thiruvananthapuram","thrissur","tiruchirappalli","tirunelveli","tiruppur","ujjain",
					"vijayapura","vadodara","varanasi","vasai-virar city","vijayawada","visakhapatnam","warangal","gwalior"]
		loc = tracker.get_slot('location')
		if loc is not None:
			if loc.lower() in list_loc:
				return[SlotSet('location',loc)]
			else:
				dispatcher.utter_template("utter_wrong_location",tracker)
				return[SlotSet('location',None)]
		else:
			dispatcher.utter_message("Location is not understandable")
			return[SlotSet('location', None)]

class ActionSendEmail(Action):

    def name(self):
        return 'action_send_mail'
		
    def run(self, dispatcher, tracker, domain):
        print("Sending Email")
        from_user = 'foodiebot.dummy@gmail.com'
        to_user = tracker.get_slot('email_address')
        password = 'foodie@12'
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(from_user, password)
        subject = 'Top '+cuisine+ ' restaurants in '+loc+ ' recommended by FoodieBot..!!'
        msg = MIMEMultipart()
        msg['From'] = from_user
        msg['TO'] = to_user
        msg['Subject'] = subject
        msg.attach(MIMEText(resp_mail,'html'))
        text = msg.as_string()
        server.sendmail(from_user,to_user,text)
        server.close()
        

class ActionCheckCuisine(Action):
	def name(self):
		return 'action_check_cuisine'

	def run(self, dispatcher, tracker, domain):
		print("Validating Cuisine")
		cuisine=tracker.get_slot('cuisine')
		freetext = tracker.get_slot('freetext')
		cuisine_list = ['american','italian','chinese','mexican','north indian','south indian']
		cuisine_buttons = {1:"Chinese", 2:"Italian", 3:"Mexican", 4:"American", 5:"South Indian", 6:"North Indian"}

		if  cuisine is None and freetext is not None and str(freetext).isdigit():
			cuisine = cuisine_buttons.get(int(freetext))
		elif cuisine is None and freetext is not None and str(freetext).lower() not in cuisine_list:
			dispatcher.utter_template("utter_wrong_cuisine",tracker)
			cuisine = freetext
			freetext = None
		elif cuisine is None or str(cuisine).lower() not in cuisine_list:
			dispatcher.utter_template("utter_wrong_cuisine",tracker)
			cuisine = None


		return [SlotSet('cuisine',cuisine),SlotSet('freetext',None)]

class ActionCheckBudget(Action):
	def name(self):
		return 'action_check_budget'

	def run(self, dispatcher, tracker, domain):
		print("Validating Budget")
		budget=tracker.get_slot('price')
		freetext = tracker.get_slot('freetext')
		budget_list = ['low','mid','high']
		budget_buttons = {1:"low", 2:"mid", 3:"high"}
		budget_button_list =["1","2","3"]

		if budget is None and freetext is not None and str(freetext).isdigit() and str(freetext) in budget_button_list :
			budget = budget_buttons.get(int(freetext))
		elif budget is None and freetext is not None and str(freetext).isdigit() and str(freetext) not in budget_button_list :
			if(int(freetext) >0 and int(freetext) <=300):
				budget="low"
			elif(int(freetext) >300 and int(freetext) <=700):
				budget="mid"
			elif(int(freetext)>700):
				budget="high"

		elif budget is None and freetext is not None and str(freetext).lower() not in budget_list:
			dispatcher.utter_template("utter_wrong_budget",tracker)
			budget = None
			freetext = None
		elif budget is None and freetext is not None and str(freetext).lower() in budget_list:
			budget = freetext
			freetext = None
		elif budget is None or str(budget).lower() not in budget_list:
			dispatcher.utter_template("utter_wrong_budget",tracker)
			budget = None


		return [SlotSet('price',budget),SlotSet('freetext',None)]

class ActionSlotReset(Action):
	def name(self):
		return 'action_slot_reset'

	def run(self, dispatcher, tracker, domain):
		print("Resetting Slots")
		return [SlotSet('cuisine',None),SlotSet('location', None),SlotSet('email_address', None),SlotSet('price',None),SlotSet('freetext',None),SlotSet('search_results',None)]

