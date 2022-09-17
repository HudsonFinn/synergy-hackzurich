#!/venv/bin/python
import os
import json
from flask import Flask
app = Flask(__name__)

file_data = {}
fileNum = 0

dirPath = "./static/data/zurich2"

files = []

for path in os.listdir(dirPath):
    # check if current path is a file
    fullPath = os.path.join(dirPath, path)
    files.append(fullPath)

files.sort()

print(files)

@app.route('/buildings')
def hello():
	print("Bulidings called")
	return 'This is a list of all buildings'

@app.route('/<building>/now')
def getBuildingData(building):
	global fileNum
	print(fileNum)
	print(files[fileNum])
	with open(files[fileNum]) as file: # opening the json file
		file_data = json.load(file)
	fileNum = (fileNum + 1) % (len(files))
	return file_data

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