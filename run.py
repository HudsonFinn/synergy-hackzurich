import os
#!/venv/bin/python
from flask import Flask
app = Flask(__name__)

@app.route('/buildings')
def hello():
	return 'This is a list of all buildings'

@app.route('/<building>/now')
def getBuildingData(building):
	return f'This building is called {building}'

@app.route('/<building>/day')
def getBuildingDayData(building):
	return f'This is data for the last 24 hours of {building}'

# Keep this at the bottom of run.py

if __name__ == "__main__":
    if os.environ.get('IS_CONTAINER') != 'true':
        app.run(debug=True)
    else:
        port = os.environ.get('PORT')
        if port == None:
            port = '5000'
        app.run(host=f'0.0.0.0:{port}')