import requests

def paid(user):
    status = user.get("IsPaidForCustomer", False)
    return status

def give_access(has_paid):
    if has_paid:
        print("Hai!! OwO")
        return # Tiene acceso
    else:
        print("NO >:v")
        return # Tiene acceso
        
url = "https://{LOCKILINK}.spaces.nexudus.com/en/profile?_resource=Coworker"

headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    user = paid
else:
    print(f'Error: {response.status_code}')
    