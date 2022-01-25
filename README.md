# Python Weather API

### What you need to know

This API enables the user to register weather sensors, sensor data attached to those sensors and to request this data back directly or to request an averaging of any metrics over any number of sensors.

The application is built with Python 3.8.9 and Flask 2.0.2. Requirements can be installed with Pip using the requirements.txt in the root directory. 
    '''pip install -r requirements.txt'''

The app comes with a useful python script called init_db.py which will create the SQLite DB to power the application and which will fill it with some dummy data. 
    - To trigger it call ''' python init_db.py'''

To start the application use:
    '''FLASK_APP=main flask run'''

The app also comes with some very basic testing to test saving our models with valid and invalid data. To run these tests call '''pytest''' in the main directory for the app. These tests are contained within '''test_application.py'''. 

### API Endpoints

The endpoints are as follows:  
@app.route("/"). 
    - Returns a hello world response. Useful for testing the application is running

@app.route("/sensors/create", methods=["POST"])  
    - Post request to create a Sensor in the system. System will return a 200 code if created successfully, or will return a 400 or 500 if request was unsuccessful due to the requests missing attributes, the sensor already existing or if the sensor could not save for another reason.  
    - Example: curl -X POST localhost:5000/sensors/create -H 'Content-Type: application/json' -d '{"uuid":"G05D05", "country":"Ireland", "city":"Athlone"}'. 

@app.route("/sensors/all")  
    - This endpoint lists all sensors in the system. Useful for knowing what ones exist when trying to create sensor data or request specific sensors. 
    - Example: curl localhost:5000/sensors/all. 

@app.route("/sensors/<uuid>")  
    - Lists a specific sensor and its data.  
    - Example: curl localhost:5000/sensors/A1B2C3  

@app.route("/sensor_data/create", methods=["POST"])  
    - Post request to create a SensorData in the system. System will return a 200 code if created successfully, or will return a 400 or 500 if request was unsuccessful due to the requests missing attributes, the specified sensor not existing or if the sensor data could not save for another reason.  
    - Example: curl -X POST localhost:5000/sensor_data/create -H 'Content-Type: application/json' -d '{"sensor_uuid":"A1B2C3", "temp":"70", "humidity":"80", "wind_speed":"40"}'. 

@app.route("/sensor_data/all")  
    - Lists all sensor data records in the system, grouped by their sensor UUID.  
    - Example: curl localhost:5000/sensor_data/all  

@app.route("/sensor_data/<sensor_uuid>")  
    - Lists all the sensor data records associated with a particular sensor UUID. 
    - Example: curl localhost:5000/sensor_data/A1B2C3 

@app.route("/get_metrics/")  
    - This endpoint allows us to call the service which will calculate average results for the specified metrics over the specified timeframe, for specified sensors.   
    Parameters:  
        - sensors: The UUID of the sensors to include in the averaging. Can be provided with a comma separated list to include multiple results.   
        - metrics: Supported values: [temp, humidity, wind_speed]. results will include an average for each metric specified. Can provide multiple with a comma separated list.   
        - start_day: Day which to start taking results from. Must be provided in the form DD-M-YYYY.   
        - start_day: Day which to end taking results from. Must be provided in the form DD-M-YYYY.   
    - Examples:     
        - curl 'localhost:5000/get_metrics/?sensors=A1B2C3&metrics=humidity,temp&start_day=22-1-2022&end_day=30-1-2022'    
        - curl 'localhost:5000/get_metrics/?sensors=A1B2C3,D4E5F6&metrics=humidity,temp&start_day=22-1-2022&end_day=30-1-2022'    
        - curl 'localhost:5000/get_metrics/?sensors=A1B2C3,D4E5F6&metrics=wind_speed&start_day=22-1-2022&end_day=30-1-2022'  
        - curl 'localhost:5000/get_metrics/?sensors=Wrong&metrics=wind_speed&start_day=25-1-2022&end_day=30-1-2022' 
    
