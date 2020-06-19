## interactive_story_6
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* greet{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"location": "Bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_check_budget
    - slot{"price": "mid"}
    - slot{"freetext": null}
    - action_search_restaurants
* affirm
    - utter_ask_email_send
* email_confirmation{"email_address": "abhilashdixitece@gmail.com"}
    - slot{"email_address": "abhilashdixitece@gmail.com"}
    - action_send_mail
    - utter_sent_email
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}


## interactive_story_7
* greet
    - utter_greet
* restaurant_search{"cuisine": "North Indian", "location": "Bangalore", "price": "mid"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "Bangalore"}
    - slot{"price": "mid"}
    - action_check_location
    - slot{"location": "Bangalore"}
    - action_check_cuisine
    - slot{"cuisine": "North Indian"}
    - slot{"freetext": null}
    - action_check_budget
    - slot{"price": "mid"}
    - slot{"freetext": null}
    - action_search_restaurants
    - utter_ask_email_send
* email_confirmation{"email_address": "abhilashdixitece@gmail.com"}
    - slot{"email_address": "abhilashdixitece@gmail.com"}
    - action_send_mail
    - utter_sent_email
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}

## interactive_story_8
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "chandigarh"}
    - slot{"cuisine": "italian"}
    - slot{"location": "chandigarh"}
    - action_check_location
    - slot{"location": "chandigarh"}
    - action_check_cuisine
    - slot{"cuisine": "italian"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"freetext": "3"}
    - slot{"freetext": "3"}
    - action_check_budget
    - slot{"price": "high"}
    - slot{"freetext": null}
    - action_search_restaurants
    - utter_ask_email_send
* deny
    - utter_goodbye
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}

## interactive_story_9
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_check_location
    - slot{"location": null}
    - action_default_ask_rephrase
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_check_cuisine
    - slot{"cuisine": "american"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"freetext": "3"}
    - slot{"freetext": "3"}
    - action_check_budget
    - slot{"price": "high"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_email_send
* affirm
    - utter_ask_email_address
* email_confirmation{"email_address": "kanikaraheja@ymail.com"}
    - slot{"email_address": "kanikaraheja@ymail.com"}
    - action_send_mail
    - utter_sent_email
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}

## interactive_story_10
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_check_location
    - slot{"location": "chandigarh"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"freetext": "3"}
    - slot{"freetext": "3"}
    - action_check_budget
    - slot{"price": "high"}
    - slot{"freetext": null}
    - action_search_restaurants
    - utter_ask_email_send
* email_confirmation{"email_address": "abhilashdixitece@gmail.com"}
    - slot{"email_address": "abhilashdixitece@gmail.com"}
    - action_send_mail
    - utter_sent_email
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}

## interactive_story_11
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Bangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"location": "Bangalore"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - utter_ask_email_send
* email_confirmation{"email_address": "abhilashdixitece@gmail.com"}
    - slot{"email_address": "abhilashdixitece@gmail.com"}
    - action_send_mail
    - utter_sent_email
* affirm
    - utter_goodbye
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_ask_email_send
* deny
    - utter_goodbye
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}

# new stories

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"location": "Bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"freetext": "300-700 range"}
    - slot{"freetext": "300-700 range"}
    - action_check_budget
    - slot{"price": "300-700 range"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - utter_ask_email_send
* email_confirmation{"email_address": "kanikaraheja@ymail.com"}
    - slot{"email_address": "kanikaraheja@ymail.com"}
    - action_send_mail
    - utter_sent_email
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_check_location
    - slot{"location": null}
* restaurant_search{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - action_check_location
    - slot{"location": "Allahabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"freetext": "high"}
    - slot{"freetext": "high"}
    - action_check_budget
    - slot{"price": null}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "Allahabad"}
    - utter_ask_email_send
* email_confirmation{"email_address": "kanikaraheja@ymail.com"}
    - slot{"email_address": "kanikaraheja@ymail.com"}
    - action_send_mail
    - utter_sent_email
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_check_location
    - slot{"location": "kolkata"}
    - utter_ask_cuisine
* restaurant_search{"freetext": "4"}
    - slot{"freetext": "4"}
    - action_check_cuisine
    - slot{"cuisine": "American"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"freetext": "low"}
    - slot{"freetext": "low"}
    - action_check_budget
    - slot{"price": "low"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "kolkata"}
    - utter_ask_email_send
* affirm
    - utter_ask_email_address
* email_confirmation{"email_address": "kanikaraheja@ymail.com"}
    - slot{"email_address": "kanikaraheja@ymail.com"}
    - action_send_mail
    - utter_sent_email
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_check_location
    - slot{"location": null}
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"freetext": "seafood"}
    - slot{"freetext": "seafood"}
    - action_check_cuisine
    - slot{"cuisine": "seafood"}
    - slot{"freetext": null}
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_price
* restaurant_search{"freetext": "450"}
    - slot{"freetext": "450"}
    - action_check_budget
    - slot{"price": "mid"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_email_send
* affirm
    - utter_ask_email_address
* email_confirmation{"email_address": "kanikaraheja@ymail.com"}
    - slot{"email_address": "kanikaraheja@ymail.com"}
    - action_send_mail
    - utter_sent_email
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Chandigarh"}
    - action_check_location
    - slot{"location": "Chandigarh"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"freetext": "high"}
    - slot{"freetext": "high"}
    - action_check_budget
    - slot{"price": "high"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "Chandigarh"}
    - utter_ask_email_send
* deny
    - utter_goodbye
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "price": "low", "location": "chandigarh"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "chandigarh"}
    - slot{"price": "low"}
    - action_check_location
    - slot{"location": "chandigarh"}
    - action_check_cuisine
    - slot{"cuisine": "mexican"}
    - slot{"freetext": null}
    - action_check_budget
    - slot{"price": "low"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - utter_ask_email_send
* deny
    - utter_goodbye
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}



## interactive_story_1
* restaurant_search{"cuisine": "american", "location": "Delhi"}
    - slot{"cuisine": "american"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"location": "Delhi"}
    - action_check_cuisine
    - slot{"cuisine": "american"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"freetext": "300"}
    - slot{"freetext": "300"}
    - action_check_budget
    - slot{"price": "low"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"search_results": true}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_check_budget
    - slot{"price": "mid"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"search_results": true}
    - utter_ask_email_send
* deny
    - utter_goodbye
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}

## interactive_story_1
* restaurant_search{"price": "low", "cuisine": "american"}
    - slot{"cuisine": "american"}
    - slot{"price": "low"}
    - action_check_cuisine
    - slot{"cuisine": "american"}
    - slot{"freetext": null}
    - action_check_budget
    - slot{"price": "low"}
    - slot{"freetext": null}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"search_results": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_budget
    - slot{"price": "high"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"search_results": true}
    - utter_ask_email_send
* email_confirmation{"email_address": "kanikaraheja@ymail.com"}
    - slot{"email_address": "kanikaraheja@ymail.com"}
    - action_send_mail
    - utter_sent_email
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}

## interactive_story_1
* restaurant_search{"cuisine": "mexican", "location": "ujjain"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "ujjain"}
    - action_check_location
    - slot{"location": "ujjain"}
    - action_check_cuisine
    - slot{"cuisine": "mexican"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_budget
    - slot{"price": "low"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "ujjain"}
    - slot{"search_results": true}
    - utter_ask_email_send
* deny
    - utter_goodbye
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"price": "low", "cuisine": "mexican", "location": "kannur"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "kannur"}
    - slot{"price": "low"}
    - action_check_cuisine
    - slot{"cuisine": "mexican"}
    - slot{"freetext": null}
    - action_check_location
    - slot{"location": "kannur"}
    - action_check_budget
    - slot{"price": "low"}
    - slot{"freetext": null}
    - action_search_restaurants
    - utter_ask_email_send
* deny
    - utter_goodbye
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}


## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "kanpur"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "kanpur"}
    - action_check_location
    - slot{"location": "kanpur"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_budget
    - slot{"price": "high"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "kanpur"}
    - utter_ask_email_send
* deny
    - utter_goodbye
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "Pune"}
    - slot{"cuisine": "american"}
    - slot{"location": "Pune"}
    - action_check_location
    - slot{"location": "Pune"}
    - action_check_cuisine
    - slot{"cuisine": "american"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"freetext": "600"}
    - slot{"freetext": "600"}
    - action_check_budget
    - slot{"price": "mid"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - utter_ask_email_send
* email_confirmation{"email_address": "abhilashdixitece@gmail.com"}
    - slot{"email_address": "abhilashdixitece@gmail.com"}
    - action_send_mail
    - utter_sent_email
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}


## interactive_story_1
* restaurant_search{"cuisine": "chinese", "location": "Kolkata"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Kolkata"}
    - action_check_location
    - slot{"location": "Kolkata"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"freetext": "mid"}
    - slot{"freetext": "mid"}
    - action_check_budget
    - slot{"price": "mid"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - utter_ask_email_send
* deny
    - utter_goodbye
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}
	
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "Bangalore"}
    - slot{"cuisine": "american"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"location": "Bangalore"}
    - action_check_cuisine
    - slot{"cuisine": "american"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"freetext": "reasonable"}
    - slot{"freetext": "reasonable"}
    - action_check_budget
    - slot{"price": null}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - utter_ask_email_send
* deny
    - utter_goodbye
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_email_send
* deny
    - utter_goodbye
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - action_check_location
    - slot{"location": "hyderabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_check_cuisine
    - slot{"cuisine": "Italian"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_check_budget
    - slot{"price": "mid"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "hyderabad"}
    - utter_ask_email_send
* deny
    - utter_goodbye
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - action_check_location
    - slot{"location": "ahmedabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_check_budget
    - slot{"price": "mid"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "ahmedabad"}
    - utter_ask_email_send
* email_confirmation{"email_address": "abhilashdixitece@gmail.com"}
    - slot{"email_address": "abhilashdixitece@gmail.com"}
    - action_send_mail
    - utter_sent_email
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "kanpur"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "kanpur"}
    - action_check_location
    - slot{"location": "kanpur"}
    - action_check_cuisine
    - slot{"cuisine": "mexican"}
* restaurant_search{"cuisine": "American", "price": "low", "location": "Kochi"}
    - slot{"cuisine": "American"}
    - slot{"location": "Kochi"}
    - slot{"price": "low"}
    - action_check_cuisine
    - slot{"cuisine": "American"}
    - slot{"freetext": null}
    - action_check_location
    - slot{"location": "Kochi"}
    - action_check_budget
    - slot{"price": "low"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "Kochi"}
    - slot{"search_results": false}
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}

## interactive_story_2
* restaurant_search{"price": "high", "cuisine": "American", "location": "Kochi"}
    - slot{"cuisine": "American"}
    - slot{"location": "Kochi"}
    - slot{"price": "high"}
    - action_check_location
    - slot{"location": "Kochi"}
    - action_check_budget
    - slot{"price": "high"}
    - slot{"freetext": null}
    - action_check_cuisine
    - slot{"cuisine": "American"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "Kochi"}
    - slot{"search_results": false}
* affirm
    - utter_goodbye
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "Kochi"}
    - slot{"cuisine": "american"}
    - slot{"location": "Kochi"}
    - action_check_location
    - slot{"location": "Kochi"}
    - action_check_cuisine
    - slot{"cuisine": "american"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"location": "kanpur"}
    - utter_ask_email_send
* email_confirmation{"email_address": "abhilashdixitece@gmail.com"}
    - slot{"email_address": "abhilashdixitece@gmail.com"}
    - action_send_mail
    - utter_sent_email
* affirm
    - utter_goodbye
    - action_check_budget
    - slot{"price": "low"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "Kochi"}
    - slot{"search_results": true}
    - utter_ask_email_send
* deny
    - utter_goodbye
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"location": "Bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_check_cuisine
    - slot{"cuisine": "american"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"freetext": "mid"}
    - slot{"freetext": "mid"}
    - action_check_budget
    - slot{"price": "mid"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - slot{"search_results": true}
    - utter_ask_email_send
* email_confirmation{"email_address": "abhilashdixitece@gmail.com"}
    - slot{"email_address": "abhilashdixitece@gmail.com"}
    - action_send_mail
    - utter_sent_email
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "low", "cuisine": "chinese", "location": "Bangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Bangalore"}
    - slot{"price": "low"}
    - action_check_location
    - slot{"location": "Bangalore"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"freetext": null}
    - action_check_budget
    - slot{"price": "low"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - slot{"search_results": true}
    - utter_ask_email_send
* email_confirmation{"email_address": "abhilashdixitece@gmail.com"}
    - slot{"email_address": "abhilashdixitece@gmail.com"}
    - action_send_mail
    - utter_sent_email
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "mid", "cuisine": "chinese", "location": "Delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Delhi"}
    - slot{"price": "mid"}
    - action_check_location
    - slot{"location": "Delhi"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"freetext": null}
    - action_check_budget
    - slot{"price": "mid"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"search_results": true}
    - utter_ask_email_send
* email_confirmation{"email_address": "abhilashdixitece@gmail.com"}
    - slot{"email_address": "abhilashdixitece@gmail.com"}
    - action_send_mail
    - utter_sent_email
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"location": "Bangalore"}
    - utter_ask_cuisine
* restaurant_search{"freetext": "thai"}
    - slot{"freetext": "thai"}
    - action_check_cuisine
    - slot{"cuisine": "thai"}
    - slot{"freetext": null}
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_check_cuisine
    - slot{"cuisine": "mexican"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_check_budget
    - slot{"price": "mid"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - slot{"search_results": true}
    - utter_ask_email_send
* email_confirmation{"email_address": "abhilashdixitece@gmail.com"}
    - slot{"email_address": "abhilashdixitece@gmail.com"}
    - action_send_mail
    - utter_sent_email
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"freetext": "seafood"}
    - slot{"freetext": "seafood"}
    - action_check_cuisine
    - slot{"cuisine": "seafood"}
    - slot{"freetext": null}
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_budget
    - slot{"price": "high"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"search_results": true}
    - utter_ask_email_send
* email_confirmation{"email_address": "abhilashdixitece@gmail.com"}
    - slot{"email_address": "abhilashdixitece@gmail.com"}
    - action_send_mail
    - utter_sent_email
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}

## interactive_story_1
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"location": "pune"}
    - utter_ask_cuisine
* restaurant_search{"freetext": "mughlai"}
    - slot{"freetext": "mughlai"}
    - action_check_cuisine
    - slot{"cuisine": "mughlai"}
    - slot{"freetext": null}
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_budget
    - slot{"price": "high"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "pune"}
    - slot{"search_results": true}
    - utter_ask_email_send
* email_confirmation{"email_address": "abhilashdixitece@gmail.com"}
    - slot{"email_address": "abhilashdixitece@gmail.com"}
    - action_send_mail
    - utter_sent_email
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}

## interactive_story_1
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"location": "pune"}
    - utter_ask_cuisine
* restaurant_search{"freetext": "punjabi"}
    - slot{"freetext": "punjabi"}
    - action_check_cuisine
    - slot{"cuisine": "punjabi"}
    - slot{"freetext": null}
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_budget
    - slot{"price": "high"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "pune"}
    - slot{"search_results": true}
    - utter_ask_email_send
* email_confirmation{"email_address": "abhilashdixitece@gmail.com"}
    - slot{"email_address": "abhilashdixitece@gmail.com"}
    - action_send_mail
    - utter_sent_email
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}

## interactive_story_1
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"location": "pune"}
    - utter_ask_cuisine
* restaurant_search{"freetext": "spicy"}
    - slot{"freetext": "spicy"}
    - action_check_cuisine
    - slot{"cuisine": "spicy"}
    - slot{"freetext": null}
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_budget
    - slot{"price": "high"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "pune"}
    - slot{"search_results": true}
    - utter_ask_email_send
* email_confirmation{"email_address": "abhilashdixitece@gmail.com"}
    - slot{"email_address": "abhilashdixitece@gmail.com"}
    - action_send_mail
    - utter_sent_email
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}

## interactive_story_1
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"location": "pune"}
    - utter_ask_cuisine
* restaurant_search{"freetext": "mughlai"}
    - slot{"freetext": "mughlai"}
    - action_check_cuisine
    - slot{"cuisine": "mughlai"}
    - slot{"freetext": null}
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_budget
    - slot{"price": "high"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "pune"}
    - slot{"search_results": true}
    - utter_ask_email_send
* email_confirmation{"email_address": "abhilashdixitece@gmail.com"}
    - slot{"email_address": "abhilashdixitece@gmail.com"}
    - action_send_mail
    - utter_sent_email
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}

## interactive_story_1
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"location": "pune"}
    - utter_ask_cuisine
* restaurant_search{"freetext": "indonesian"}
    - slot{"freetext": "indonesian"}
    - action_check_cuisine
    - slot{"cuisine": "indonesian"}
    - slot{"freetext": null}
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_budget
    - slot{"price": "high"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "pune"}
    - slot{"search_results": true}
    - utter_ask_email_send
* email_confirmation{"email_address": "abhilashdixitece@gmail.com"}
    - slot{"email_address": "abhilashdixitece@gmail.com"}
    - action_send_mail
    - utter_sent_email
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}

## interactive_story_1
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"location": "pune"}
    - utter_ask_cuisine
* restaurant_search{"freetext": "continental"}
    - slot{"freetext": "continental"}
    - action_check_cuisine
    - slot{"cuisine": "continental"}
    - slot{"freetext": null}
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_budget
    - slot{"price": "high"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "pune"}
    - slot{"search_results": true}
    - utter_ask_email_send
* email_confirmation{"email_address": "abhilashdixitece@gmail.com"}
    - slot{"email_address": "abhilashdixitece@gmail.com"}
    - action_send_mail
    - utter_sent_email
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}



## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_check_location
    - slot{"location": "chandigarh"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"freetext": "low"}
    - slot{"freetext": "low"}
    - action_check_budget
    - slot{"price": "low"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - slot{"search_results": true}
    - utter_ask_email_send
* email_confirmation{"email_address": "abhilashdixitece@gmail.com"}
    - slot{"email_address": "abhilashdixitece@gmail.com"}
    - action_send_mail
    - utter_sent_email
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Bangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"location": "Bangalore"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"freetext": "mid"}
    - slot{"freetext": "mid"}
    - action_check_budget
    - slot{"price": "mid"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - slot{"search_results": true}
    - utter_ask_email_send
* email_confirmation{"email_address": "abhilashdixitece@gmail.com"}
    - slot{"email_address": "abhilashdixitece@gmail.com"}
    - action_send_mail
    - utter_sent_email
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chnadigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chnadigarh"}
    - action_check_location
    - slot{"location": null}
* restaurant_search{"location": "chandigarh"}
    - slot{"location": "chandigarh"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"freetext": "low"}
    - slot{"freetext": "low"}
    - action_check_budget
    - slot{"price": "low"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - slot{"search_results": true}
    - utter_ask_email_send
* email_confirmation{"email_address": "abhilashdixitece@gmail.com"}
    - slot{"email_address": "abhilashdixitece@gmail.com"}
    - action_send_mail
    - utter_sent_email
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "benagalore"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "benagalore"}
    - action_check_location
    - slot{"location": null}
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"freetext": "mid"}
    - slot{"freetext": "mid"}
    - action_check_budget
    - slot{"price": "mid"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - slot{"search_results": true}
    - utter_ask_email_send
* email_confirmation{"email_address": "abhilashdixitece@gmail.com"}
    - slot{"email_address": "abhilashdixitece@gmail.com"}
    - action_send_mail
    - utter_sent_email
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "thai", "location": "ahmedabad"}
    - slot{"cuisine": "thai"}
    - slot{"location": "ahmedabad"}
    - action_check_location
    - slot{"location": "ahmedabad"}
    - action_check_cuisine
    - slot{"cuisine": null}
    - slot{"freetext": null}
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"freetext": "high"}
    - slot{"freetext": "high"}
    - action_check_budget
    - slot{"price": "high"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "ahmedabad"}
    - slot{"search_results": true}
    - utter_ask_email_send
* deny
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "mangalore"}
    - slot{"location": "mangalore"}
    - action_check_location
    - slot{"location": "mangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_check_budget
    - slot{"price": "mid"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "mangalore"}
    - slot{"search_results": true}
    - utter_ask_email_send
* affirm
    - utter_ask_email_address
* email_confirmation{"email_address": "abhilashdixitece@gmail.com"}
    - slot{"email_address": "abhilashdixitece@gmail.com"}
    - action_send_mail
    - utter_sent_email
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}

## interactive_story_1
* restaurant_search{"cuisine": "chinese", "location": "Bangalore", "price": "mid"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Bangalore"}
    - slot{"price": "mid"}
    - action_check_location
    - slot{"location": "Bangalore"}
    - action_check_budget
    - slot{"price": "mid"}
    - slot{"freetext": null}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - slot{"search_results": true}

## interactive_story_2
* restaurant_search{"cuisine": "chinese", "location": "Bangalore", "price": "mid"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Bangalore"}
    - slot{"price": "mid"}
    - action_check_location
    - slot{"location": "Bangalore"}
    - action_check_budget
    - slot{"price": "mid"}
    - slot{"freetext": null}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - slot{"search_results": true}
    - utter_ask_email_send
* affirm
    - utter_ask_email_address
* email_confirmation{"email_address": "abhilashdixitece@gmail.com"}
    - slot{"email_address": "abhilashdixitece@gmail.com"}
    - action_send_mail
    - utter_sent_email
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}

## interactive_story_1
* restaurant_search{"cuisine": "american", "location": "Delhi", "price": "mid"}
    - slot{"cuisine": "american"}
    - slot{"location": "Delhi"}
    - slot{"price": "mid"}
    - action_check_location
    - slot{"location": "Delhi"}
    - action_check_budget
    - slot{"price": "mid"}
    - slot{"freetext": null}
    - action_check_cuisine
    - slot{"cuisine": "american"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"search_results": true}

## interactive_story_1
* restaurant_search{"cuisine": "chinese", "location": "lucknow", "price": "mid"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "lucknow"}
    - slot{"price": "mid"}
    - action_check_location
    - slot{"location": "lucknow"}
    - action_check_budget
    - slot{"price": "mid"}
    - slot{"freetext": null}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "lucknow"}
    - slot{"search_results": true}
    - utter_ask_email_send
* email_confirmation
    - utter_ask_email_address
    - utter_ask_email_address

## interactive_story_2
* restaurant_search{"cuisine": "chinese", "location": "kanpur"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "kanpur"}
    - action_check_location
    - slot{"location": "kanpur"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"location": "kanpur"}
    - slot{"search_results": true}
    - utter_ask_email_send
* email_confirmation
    - utter_ask_email_address
* email_confirmation{"email_address": "abhilashdixitece@gmail.com"}
    - slot{"email_address": "abhilashdixitece@gmail.com"}
    - action_send_mail
    - utter_sent_email
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "mysore"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "mysore"}
    - action_check_location
    - slot{"location": "mysore"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"freetext": null}

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Bangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"location": "Bangalore"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - slot{"search_results": true}
    - utter_ask_email_send
* affirm
    - utter_ask_email_address
* email_confirmation{"email_address": "abhilashdixitece@gmail.com"}
    - slot{"email_address": "abhilashdixitece@gmail.com"}
    - action_send_mail
    - utter_sent_email
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "hennai"}
    - slot{"cuisine": "american"}
    - slot{"location": "hennai"}
    - action_check_location
    - slot{"location": null}
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_cuisine
    - slot{"cuisine": "american"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_check_budget
    - slot{"price": "mid"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "Chennai"}
    - slot{"search_results": true}
    - utter_ask_email_send
* affirm
    - utter_ask_email_address
* email_confirmation{"email_address": "abhilashdixitece@gmail.com"}
    - slot{"email_address": "abhilashdixitece@gmail.com"}
    - action_send_mail
    - utter_sent_email
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_check_location
    - slot{"location": "chandigarh"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_check_budget
    - slot{"price": "mid"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - slot{"search_results": true}
    - utter_ask_email_send
* deny
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "Bangalore"}
    - slot{"cuisine": "american"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"location": "Bangalore"}
    - action_check_cuisine
    - slot{"cuisine": "american"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - slot{"search_results": true}
    - utter_ask_email_send
* deny
    - utter_goodbye

## interactive_story_21
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "siliguri"}
    - slot{"location": "siliguri"}
    - action_check_location
    - slot{"location": "siliguri"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"freetext": "550"}
    - slot{"freetext": "550"}
    - action_check_budget
    - slot{"price": "mid"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "siliguri"}
    - slot{"search_results": true}
    - utter_ask_email_send
* deny
    - utter_goodbye
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"location": null}
    - slot{"email_address": null}
    - slot{"price": null}
    - slot{"freetext": null}


## interactive_story_22
* greet
    - utter_greet
* restaurant_search{"price": "high", "cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "high"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"freetext": null}
    - action_check_budget
    - slot{"price": "high"}
    - slot{"freetext": null}
    - utter_ask_location
* restaurant_search{"location": "Pondicherry"}
    - slot{"location": "Pondicherry"}
    - action_check_location
    - slot{"location": "Pondicherry"}
    - action_search_restaurants
    - slot{"location": "Pondicherry"}
    - slot{"search_results": true}
    - utter_ask_email_send
* deny
    - utter_goodbye
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"location": null}
    - slot{"email_address": null}
    - slot{"price": null}
    - slot{"freetext": null}
* goodbye
    - utter_goodbye
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"freetext": null}
    - slot{"location": null}
    - slot{"price": null}
    - slot{"email_address": null}
    - slot{"search_results": null}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennm"}
    - slot{"location": "chennm"}
    - action_check_location
    - slot{"location": null}
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"location": "Chennai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_check_cuisine
    - slot{"cuisine": "american"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_budget
    - slot{"price": "high"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "Chennai"}
    - slot{"search_results": true}
    - utter_ask_email_send
* deny
    - utter_goodbye
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"location": null}
    - slot{"email_address": null}
    - slot{"price": null}
    - slot{"freetext": null}
    - slot{"search_results": null}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "kanpur"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "kanpur"}
    - action_check_location
    - slot{"location": "kanpur"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_budget
    - slot{"price": "high"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "kanpur"}
    - slot{"search_results": false}
    - utter_ask_email_send
* deny
    - utter_goodbye
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"location": null}
    - slot{"email_address": null}
    - slot{"price": null}
    - slot{"freetext": null}
    - slot{"search_results": null}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"location": "Chennai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "arabian"}
    - slot{"cuisine": "arabian"}
    - action_check_cuisine
    - slot{"cuisine": null}
    - slot{"freetext": null}
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"freetext": null}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_check_budget
    - slot{"price": "mid"}
    - slot{"freetext": null}
    - action_search_restaurants
    - slot{"location": "Chennai"}
    - slot{"search_results": true}
    - utter_ask_email_send
* deny
    - utter_goodbye
    - action_slot_reset
    - slot{"cuisine": null}
    - slot{"location": null}
    - slot{"email_address": null}
    - slot{"price": null}
    - slot{"freetext": null}
    - slot{"search_results": null}
