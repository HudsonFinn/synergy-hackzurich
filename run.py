#!/venv/bin/python
import os
import json
from flask import Flask
app = Flask(__name__)

file_data = {}
fileNum = 0

files = [
	'./static/data/zurich2/17-09-2022-01-26-00.json',
	'./static/data/zurich2/17-09-2022-01-26-05.json',
	'./static/data/zurich2/17-09-2022-01-26-10.json',
	'./static/data/zurich2/17-09-2022-01-26-15.json',
	'./static/data/zurich2/17-09-2022-01-26-20.json',
	'./static/data/zurich2/17-09-2022-01-26-25.json'
	]

@app.route('/buildings')
def hello():
	print("Bulidings called")
	return 'This is a list of all buildings'

@app.route('/<building>/now')
def getBuildingData(building):
	global fileNum
	print(fileNum)
	with open(files[fileNum]) as file: # opening the json file
		file_data = json.load(file)

	fileNum = (fileNum + 1) % 4
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