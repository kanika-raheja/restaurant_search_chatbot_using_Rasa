#!/usr/bin/env python3
from __future__ import print_function
import zomatopy
import json

print("test")

def filterOnBudget(budget,restaurantList):
		min=0
		max=5000

		cost = int(budget)

		if(cost==1):
			min=0
			max=500
		elif(cost==2):
			min=500
			max=1000
		elif(cost==3):
			min=1000
			max=5000
		else:
			min=0
			max=5000

		c=0
		resp=""
		for res in restaurantList:
			if(res['restaurant']['average_cost_for_two']<max and res['restaurant']['average_cost_for_two'] >min ):
				resp=resp+res['restaurant']['name']+ " in "+ res['restaurant']['location']['address']+ "------price------"+str(res['restaurant']['average_cost_for_two'])+"\n" 
				c=c+1 

		if(c==0):
			resp= "No restaurant in this budget please increase the budget for search"
		elif(c<5):
			resp=resp + "Only "+str(c) + " results found for more chnage the budget"

		return resp
		
config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
zomato = zomatopy.initialize_app(config)
location_detail=zomato.get_location('delhi', 1)
d1 = json.loads(location_detail)
lat=d1["location_suggestions"][0]["latitude"]
lon=d1["location_suggestions"][0]["longitude"]
cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get('chinese')), 100)
print(results)
d = json.loads(results)
response=""
if d['results_found'] == 0:
    response= "no results"
else:
    response=filterOnBudget(1,d['restaurants'])
print(response)





    
