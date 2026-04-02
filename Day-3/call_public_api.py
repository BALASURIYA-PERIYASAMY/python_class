import requests

url= "https://api.github.com/users/BALASURIYA-PERIYASAMY"
response = requests.get(url)
print(type(response))
print(response.status_code,"\n")
print(response.json(),"\n")
print(type(response.json()),"\n")

response_dict=response.json()

id=response_dict["id"]
print("id"+":"+str(id))

type=response_dict["type"]
print("type"+":"+type)

company=response_dict["company"]
print("company"+":"+str(company))

location=response_dict["location"]
print("location"+":"+str(location))

twitter_username=response_dict["twitter_username"]
print("twitter_username"+":"+str(twitter_username))

