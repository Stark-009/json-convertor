import json
import re
import sys
import time

# with open('data.json') as json_file:
#     data = json.load(json_file)

id = input("Choose an id : ") 

if bool(re.match('^(?=.*[0-9]$)(?=.*[a-z])', id)) == False:
    print("Please enter a aphanumeric ID")
    sys.exit()

if len(id) != 2:
    print("Please enter a ID of lenght 20")
    sys.exit()

time = int(time.time())

name = input("Your name : ") 

city = input("Choose any city[Kolkata,Delhi,Mumbai] : ") 

if city.lower() != 'kolkata' and city.lower() != 'delhi' and city.lower() != 'mumbai':
    print("Please Choose any one from the above")
    sys.exit()

age = input("Choose your age(18-50) :")

if int(age) < 18 or int(age) > 50:
    print("Please insert a valid age")
    sys.exit

data = {}
data['people'] = []
data['people'].append({
    'id': id,
    'time': time,
    'name': name,
    'city': city,
    'age' : age
})

# a = []
# entry 
# if not os.path.isfile(data.json):
#     a.append(entry)
#     with open(fname, mode='w') as f:
#         f.write(json.dumps(a, indent=2))
# else:
#     with open(data.json) as feedsjson:
#         feeds = json.load(feedsjson)

#     feeds.append(entry)
#     with open(fname, mode='w') as f:
#         f.write(json.dumps(feeds, indent=2))
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
