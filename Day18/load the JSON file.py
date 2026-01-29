#Load the JSON file and print the data and its type
import json
with open("studentsdetails.json", "r") as file:
    data = json.load(file)
    print(data)
    print(type(data))

#Formatting JSON for better readability
formated_json = json.dumps(data, indent=4)
print(formated_json)

