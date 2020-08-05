import requests


#facade pattern to access api with ease of use inside the program
class Covid:


	def make_req(self, country_name):
		result = requests.get("https://api.covid19api.com/summary").json() #convert to json data
		for country in result["Countries"]:
			if country["Country"] == country_name:
				return country
		raise ValueError("country not found")


	def total_confirmed(self, country_name):
		return self.make_req(country_name)["TotalConfirmed"]

	def total_deaths(self, country_name):
		return self.make_req(country_name)["TotalDeaths"]

	def total_recovered(self, country_name):
		return self.make_req(country_name)["TotalRecovered"]




covid = Covid()

print(covid.total_confirmed("Canada"))
print(covid.total_recovered("Canada"))
print(covid.total_deaths("Canada"))