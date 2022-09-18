# Welcome to Synergy!

This is the "backend" for the **Synergy** application which we developed for HackZurich. This repo initially started as a RestAPI to serve data to the [Unity Mobile application]([https://github.com/OliverUrsell/synergy-zurich](https://github.com/OliverUrsell/synergy-zurich)) we were building. It ended up as a simulator of buildings with the capability to serve continuous sensor data to the app and simulate fires spreading through buildings.

## What it does
Once the application is running, it initialises a building (parameters currently predefined in code) to random possess random properties. When queried, it returns the sensor data from the building in JSON format. The application will continuously update the building properties giving slight random variations to reflect the nature of the fluctuating properties of a real building. A fire can also be started on any random level which will spread throughout the building realistically until the building is destroyed.

## Endpoints
We have 4 main endpoints which can be queried:

`/<buildingName>/now`

Returns the current sensor data for the simulated building

`/startfire`

Begins a fire on a random floor of the simulated building, will spread through whole building until destroyed and then reset the building to a 'normal' simulated state

`/stopfire`

Stops any fire that is currently happening, resets the building to a 'normal' simulated state

## Build the app
Clone the repo
```
git clone https://github.com/HudsonFinn/synergy-hackzurich.git
```
Activate the virtual environment
```
source venv/bin/activate
```
> Note: You will need VirtualEnv installed

Install required pip packages
```
pip install -r requirements.txt
```
Run the server
```
gunicorn --bind 0.0.0.0:5000 server:app
```
You should now be able to query the above endpoints at
```
http://localhost:5000/
```
