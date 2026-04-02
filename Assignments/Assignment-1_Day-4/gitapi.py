import requests
url = "https://api.github.com/users/BALASURIYA-PERIYASAMY"
data = requests.get(url).json()

followers=data["followers"]
public_repos=data["public_repos"]
location=data["location"]


if followers>10:
    print("Popular user!")
else:
    print("Keep growing!")


if public_repos>5:
    print("Active contributor!")
else:
    print("Just getting started!")

if location is not None:
    print(location)
else:
    print("Location is not Set:")

print(data["name"])
print(data["login"])
print(data["followers"])
print(data["name"])
