#Invoke the API URL and print the response
import requests
response = requests.get('https://jsonplaceholder.typicode.com/posts')
print(response)
#parse the JSON data from the response
data=response.json()
print(data)

#How to parse the Json Document data
import json
formated_json = json.dumps(data, indent=4)
print(formated_json)
data = {
    "email": "aishwarya.rao@example.com",
    "phone": "9876543210",
    "address": {
      "street": "MG Road",
      "city": "Bengaluru",
      "state": "Karnataka",
      "pincode": 560001
    }
}
print(data)
print(data.items())
print(data.values())
print(data.keys())