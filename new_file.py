import requests

url = "https://twelve-data1.p.rapidapi.com/time_series"

querystring = {"symbol":"AMZN","interval":"1day","outputsize":"30","format":"json"}

headers = {
	"X-RapidAPI-Key": "61d11dfc19msh8f1adb96bd2e05ep1030d1jsn073be1c1af0e",
	"X-RapidAPI-Host": "twelve-data1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())