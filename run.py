#!/venv/bin/python
import os
import json
from flask import Flask
app = Flask(__name__)

file_data = {}

def appSetup(app):
	global file_data
	with open('./static/data/zurich2/17-09-2022-01-26-00.json') as file: # opening the json file
		file_data = json.load(file)

@app.route('/buildings')
def hello():
	print("Bulidings called")
	return 'This is a list of all buildings'

@app.route('/<building>/now')
def getBuildingData(building):
	return file_data

@app.route('/<building>/day')
def getBuildingDayData(building):
	return f'This is data for the last 24 hours of {building}'

# Keep this at the bottom of run.py
appSetup(app)

if __name__ == "__main__":
    if os.environ.get('IS_CONTAINER') != 'true':
        app.run(debug=True)
    else:
        port = os.environ.get('PORT')
        if port == None:
            port = '5000'
        app.run(host=f'0.0.0.0:{port}')