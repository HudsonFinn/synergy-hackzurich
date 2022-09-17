import json
import random

ignoreList = []

# Building data
floorIds = ["0", "1", "2", "3", "5", "6", "7"]
roomsPerFloor = [14, 9, 22, 13, 15, 14, 7]

# Limits
airMin = 400
airMax = 2000
airInitVar = 300
airVar = 200

tempMin = 0
tempMax = 50
tempInitVar = 5
tempVar = 4

lightMin = 1
lightMax = 1000
lightInitVar = 300
lightVar = 200

#Json Builder
floors = []

temperature = 25
airQuality = 1800
brightness = 750
fireDetected = 0
presence = 0

def getAirVal(init, var):
    plusOrMinus = random.randint(0,1)*2-1
    newVal = init + (plusOrMinus * random.randint(0, var))
    newVal = min(airMax, max(airMin, newVal))
    return newVal

def getTempVal(init, var):
    plusOrMinus = random.randint(0,1)*2-1
    offset = (plusOrMinus * random.randint(0, var))
    newVal = init + offset
    newVal = min(tempMax, max(tempMin, newVal))
    return newVal

def getLightVal(init, var):
    plusOrMinus = random.randint(0,1)*2-1
    newVal = init + (plusOrMinus * random.randint(0, var))
    newVal = min(lightMax, max(lightMin, newVal))
    return newVal

def generateInitialData(temperature, airQuality, brightness):
    for (i, id) in enumerate(floorIds):
        rooms = []
        for j in range(roomsPerFloor[i]):
            tempTemperature = getTempVal(temperature, tempInitVar)
            tempAirQuality = getAirVal(airQuality, airInitVar)
            tempBrightness = getLightVal(brightness, lightInitVar)
            tempFireDetected = 0
            tempPresence = 0

            sensors = {
                "temperature": tempTemperature,
                "airQuality": tempAirQuality,
                "presence": tempPresence,
                "fireDetected": tempFireDetected,
                "brightness": tempBrightness
            }

            room = {
                "id": str(id) + f"{(j+1):02}",
                "sensors": sensors
            } 
            rooms.append(room)

        floor = {"rooms" : rooms}
        floors.append(floor)

    data = {"floors": floors}
    return data


def updateData(oldData):
    tempFloors = []
    for (i, id) in enumerate(floorIds):
        tempRooms = []
        for j in range(roomsPerFloor[i]):
            #print("intial")
            #print(oldData['floors'][int(i)]['rooms'][int(j-1)]['sensors'])
            roomData = oldData['floors'][int(i)]['rooms'][int(j)]['sensors']

            tempTemperature = roomData['temperature']
            tempAirQuality = roomData['airQuality']
            tempBrightness = roomData['brightness']
            tempFireDetected = roomData['fireDetected']
            tempPresence = roomData['presence']

            tempTemperature = getTempVal(tempTemperature, tempVar)
            tempAirQuality = getAirVal(tempAirQuality, airVar)
            tempBrightness = getLightVal(tempBrightness, lightVar)
            tempFireDetected = 0
            tempPresence = 0

            tempSensors = {
                "temperature": tempTemperature,
                "airQuality": tempAirQuality,
                "presence": tempPresence,
                "fireDetected": tempFireDetected,
                "brightness": tempBrightness
            }
            #print("new")
            #print(sensors)

            tempRoom = {
                "id": str(id) + f"{(j+1):02}",
                "sensors": tempSensors
            } 
            tempRooms.append(tempRoom)

        tempFloor = {"rooms" : tempRooms}
        tempFloors.append(tempFloor)

    data = {"floors": tempFloors}
    return data

floor0 = [7, 3, 9, 8, 6, 13, 10, 11, 5, 1, 14, 12, 4, 2]
floor1 = [4, 1, 2, 3, 5, 9, 8, 6, 7]
floor2 = [14, 10, 13, 15, 17, 16, 
            6, 19, 20, 12, 5, 21, 
            22, 18, 11, 7, 8, 1, 9,
            4, 3, 2]
floor3 = [6, 9, 7, 8, 10, 5, 12, 1, 13,
            4, 3, 2]
floor4 = [15, 14, 9, 10, 8, 11, 6, 7, 1, 
            4, 2, 3]
floor5 = [6, 7, 5, 11, 13, 9, 1, 10, 
            14, 4, 3, 2]
floor6 = [2, 1, 3, 7, 4, 5, 6]
floorScenarios = [floor0, floor1, floor2, floor3, floor4, floor5, floor6]

def generateFire(oldData, floor, scenarios):
    floorsOnFire = []
    floorsOnFire.append(floor)


    print(scenarios[floor])

initialData = generateInitialData(temperature, airQuality, brightness) 
print(json.dumps(initialData, indent=4))

# Serializing json
json_object = json.dumps(initialData, indent=4)
 
print(initialData['floors'][0]['rooms'][0]['sensors'])

# generateFire(initialData, 3, floorScenarios)
# Writing to sample.json
with open("static/data/zurich2/17-09-2022-01-26-00.json", "w") as outfile:
    outfile.write(json_object)

for i in range(10):
    initialData = updateData(initialData)
    print(initialData['floors'][0]['rooms'][0]['sensors'])
    json_object = json.dumps(initialData, indent=4) 
    with open(f"static/data/zurich2/17-09-2022-01-26-{((i+1) * 5):02}.json", "w") as outfile:
        outfile.write(json_object)

