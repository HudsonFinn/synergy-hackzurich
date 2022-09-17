import json
import random

ignoreList = []

# Building data
floorIds = ["0", "1", "2", "3", "5", "6", "7"]
roomsPerFloor = [14, 9, 22, 13, 15, 14, 7]

# Limits
airMin = 400
airMax = 2000

tempMin = 0
tempMax = 50

lightMin = 1
lightMax = 1000

#Json Builder
floors = []

temperature = 25
airQuality = 1800
brightness = 750
fireDetected = 0
presence = 0

for (i, id) in enumerate(floorIds):
    rooms = []
    for j in range(roomsPerFloor[i]):
        temperature = random.randint(tempMin, tempMax)
        airQuality = random.randint(airMin, airMax)
        brightness = random.randint(lightMin, lightMax)
        fireDetected = 0
        presence = 0

        sensors = {
            "temperature": temperature,
            "airQuality": airQuality,
            "presence": presence,
            "fireDetected": fireDetected,
            "brightness": brightness
        }

        room = {
            "id": str(id) + f"{(j+1):02}",
            "sensors": sensors
        } 
        rooms.append(room)

    floor = {"rooms" : rooms}
    floors.append(floor)

data = {"floors": floors}

print(json.dumps(data, indent=4))

# Serializing json
json_object = json.dumps(data, indent=4)
 
# Writing to sample.json
with open("static/data/zurich2/17-09-2022-01-26-15.json", "w") as outfile:
    outfile.write(json_object)