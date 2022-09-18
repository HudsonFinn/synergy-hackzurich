#!/venv/bin/python
import os
import json
from flask import Flask
from createdata import updateData 

app = Flask(__name__)


global file_data
global fire
global fileNum
fileNum = 0
file_data = {}
fire = False

dirPath = "./static/data/zurich2"

files = []

for path in os.listdir(dirPath):
    # check if current path is a file
    fullPath = os.path.join(dirPath, path)
    files.append(fullPath)

files.sort()

path = "./static/data/zurich2/init.json"
with open(path) as file: # opening the json file
	file_data = json.load(file)

def updateFire(status):
	global fire
	fire = status

def updateFileData(data):
	global file_data
	file_data = data

@app.route('/buildings')
def hello():
	print("Bulidings called")
	return 'This is a list of all buildings'

@app.route('/<building>/now')
def getBuildingData(building):
	print(fire)
	global fileNum
	if fire:
		with open(files[fileNum]) as fireFile: # opening the json file
			fireData = json.load(fireFile)
		print(files[fileNum])
		fileNum = fileNum + 1
		print(fileNum)
		if fileNum == len(files):
			updateFire(False)
		return fireData
	else:
		newData = updateData(file_data)
		updateFileData(newData)
		return file_data

@app.route('/startfire')
def startFire():
	global fileNum
	updateFire(True)
	fileNum = 0
	return 'Fire started: ' + str(fire)

@app.route('/stopfire')
def stopFire():
	updateFire(False)
	return 'Fire started: ' + str(fire)

@app.route('/<building>/day')
def getBuildingDayData(building):
	return f'This is data for the last 24 hours of {building}'


if __name__ == "__main__":
    if os.environ.get('IS_CONTAINER') != 'true':
        app.run(debug=True)
    else:
        port = os.environ.get('PORT')
        if port == None:
            port = '5000'
        app.run(host=f'0.0.0.0:{port}')