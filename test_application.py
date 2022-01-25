import pytest
from models.sensor import Sensor
from models.sensor_data import SensorData 

@pytest.fixture
def valid_sensor():
    sensor = Sensor("TEST123", "USA", "New York")
    yield sensor
    sensor.delete()

@pytest.fixture
def invalid_sensor():
    sensor_info = {
        "uuid": "TEST123",
        "country": "USA",
        "city": "New York"        
    }
    sensor = Sensor(sensor_info["uuid"], sensor_info["country"], sensor_info["city"])
    sensor.save()
    yield sensor_info    
    sensor.delete()

def test_sensor_save_successful(valid_sensor):
    saved = valid_sensor.save()
    assert saved == True
    
def test_sensor_save_unsuccessful(invalid_sensor):
    with pytest.raises(ValueError):
        Sensor(invalid_sensor["uuid"], invalid_sensor["country"], invalid_sensor["city"]).save()

@pytest.fixture
def valid_sensor_data():
    sensor = Sensor("SNRDTA", "IRE", "Galway")
    sensor.save()
    sensor_data = SensorData("SNRDTA", 1, 1, 1)    
    yield sensor_data
    sensor.delete()

@pytest.fixture
def invalid_sensor_data():
    sensor_data = {
        "sensor_uuid": "SNRDTA",
        "temp": 1,
        "humidity": 1,
        "wind_speed":1
    }
    yield sensor_data

    
def test_sensor_data_valid(valid_sensor_data):
    saved = valid_sensor_data.save()
    assert saved == True

def test_sensor_save_unsuccessful(invalid_sensor_data):
    with pytest.raises(ValueError):
        SensorData(invalid_sensor_data["sensor_uuid"], invalid_sensor_data["temp"], invalid_sensor_data["humidity"], invalid_sensor_data["wind_speed"]).save()