from database.manager import DatabaseManager

class Sensor:
    def __init__(self, uuid, country, city, created_at=None):
        self.uuid = uuid
        self.country = country
        self.city = city
        self.created_at = created_at
        self.saved = created_at != None

    @property
    def uuid(self):
        return self._uuid

    @uuid.setter
    def uuid(self, value):
        if Sensor.uuid_exists(value):
            raise ValueError("UUID already exists in DB")
        self._uuid = value

    def save(self):
        db_manager = DatabaseManager()
        query_string = "INSERT INTO Sensors (uuid, country, city) values(?, ?, ?)"
        res = db_manager.execute_query(query_string, [self.uuid, self.country, self.city])    
        if res["success"]:
            self.saved = True
            return True
        return False

    def delete(self):
        db_manager = DatabaseManager()
        query_string = "DELETE FROM Sensors WHERE uuid = ?"
        res = db_manager.execute_query(query_string, [self.uuid])    
        if res["success"]:
            self.saved == False
            return True
        return False

    ### Static Methods
    @staticmethod
    def get_all_sensors():
        db_manager = DatabaseManager()
        query = "SELECT * FROM Sensors"
        res = db_manager.execute_query(query)
        
        sensors = list(map(lambda row: Sensor(row[1], row[2], row[3], row[4]), 
            res["data"]
        ))
        return sensors

    @staticmethod
    def get_sensor_by_uuid(uuid):
        db_manager = DatabaseManager()
        query = "SELECT * FROM Sensors WHERE uuid = ?"
        res = db_manager.execute_query(query, [uuid])

        sensor = None
        if res["data"]:
            row = res["data"][0]
            sensor = Sensor(row[1], row[2], row[3], row[4])
        return sensor

    @staticmethod
    def uuid_exists(uuid):
        db_manager = DatabaseManager()
        query = "SELECT * FROM Sensors WHERE uuid = ?"
        res = db_manager.execute_query(query, [uuid])
        if res["data"]:
            return True
        return False
        



