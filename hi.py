import requests

url = 'https://{LOCKILINK}.spaces.nexudus.com/en?_resource=Coworker&_depth=2'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Assuming the response is in JSON format
    # Process the data as needed
else:
    print(f'Error: {response.status_code}')
    
    
user_data 

pago = user_data.get("IsPaidForCustomer")

if pago:
    # Tiene acceso
else: 
    # No tiene acceso
