import requests

BASE_URL = 'https://contact.plaid.com/'

def post_api(endpoint, data):
	url = BASE_URL + endpoint
	try: 
		response = requests.post(url, data)
	except Exception as e:
		response = e
	return handle_response(response)

def handle_response(response):
	if isinstance(response, Exception):
		print(response)
		return response
	else:
		return response

def apply_to_plaid(name, email, resume, phone, github, twitter, website, location, candy, superpower):
  application = {
		"name": name,
		"email": email,
		"resume": resume,
		"phone": phone, 
		"github": github,
		"twitter": twitter,
		"website": website,
		"location": location,
		"candy": candy,
		"superpower": superpower
	}
  return post_api("jobs", application)
  
  
if __name__ == "__main__":
  apply_to_plaid(
    # name
		"Sachin Meier",
		# email
		"sachin.meier@gmail.com",
		# resume link
		"https://www.sachinmeier.com/assets/Resume_SM.pdf",
		# phone number
		"781-990-9802",
		# github link
		"https://github.com/SachinMeier/",
		# twitter link
		"https://twitter.com/SachinMeier/",
		# website link
		"https://sachinmeier.com",
		# location
		"San Francisco",
		# favorite candy
		"Welch's Fruit Snacks",
		# superpower
		"all things bitcoin"
	)