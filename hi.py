import requests

def paid(user):
    status = user.get("IsPaidForCustomer", False)
    return status

def give_access(has_paid):
    if has_paid:
        return # Has access
    else:
        return # Doesn't have acces
        
url = "https://{LOCKILINK}.spaces.nexudus.com/en/profile?_resource=Coworker"

headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    user = paid(data)
    give_access(user)
else:
    print(f'Error: {response.status_code}')
    