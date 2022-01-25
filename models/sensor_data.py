from database.manager import DatabaseManager
from models.sensor import Sensor

class SensorData:
    def __init__(self, sensor_uuid, temp, humidity, wind_speed, created_at=None):
        self.sensor_uuid = sensor_uuid
        self.temp = temp
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.created_at = created_at
        self.saved = created_at != None

    def save(self):
        db_manager = DatabaseManager()
        query_string = "INSERT INTO SensorData (sensor_uuid, temperature, humidity, wind_speed) values(?, ?, ?, ?)"
        res = db_manager.execute_query(query_string, [self.sensor_uuid, self.temp, self.humidity, self.wind_speed])
        if res["success"]:
            self.saved = True
            return True
        return False

    @property
    def sensor_uuid(self):
        return self._sensor_uuid

    @sensor_uuid.setter
    def sensor_uuid(self, value):
        if Sensor.uuid_exists(value):
            self._sensor_uuid = value
        else:
            raise ValueError("Sensor UUID does not exist")


    ### Static Methods
    @staticmethod
    def get_all_sensor_data():
        db_manager = DatabaseManager()
        query = "SELECT * FROM SensorData"
        res = db_manager.execute_query(query) 
        sensor_data = list(map(lambda row: SensorData(row[1], row[2], row[3], row[4], row[5]), 
            res["data"]
        ))
        return sensor_data

    @staticmethod
    def get_sensor_data_by_sensor_uuid(uuid):
        db_manager = DatabaseManager()
        query = "SELECT * FROM SensorData WHERE sensor_uuid = ?"
        res = db_manager.execute_query(query, [uuid])

        sensor_data = list(map(lambda row: SensorData(row[1], row[2], row[3], row[4], row[5]), 
            res["data"]
        ))
        return sensor_data