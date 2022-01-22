class SensorData:
    def __init__(self, temp, humidity, wind_speed):
        self.sensor_uuid = None
        self.temp = temp
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.created_at = None