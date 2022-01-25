from datetime import date, datetime
from functools import reduce
from pprint import pprint
from models.sensor_data import SensorData


class GetMetricsForSensors:
    def __init__(self, sensor_uuids, metrics, start_day, end_day):
        self.sensor_uuids = self.__parse_arg(sensor_uuids)
        self.metrics = self.__parse_arg(metrics)
        self.start_day = self.__parse_day(start_day)
        self.end_day = self.__parse_day(end_day)
        self.averages = {}

    def calculate(self):
        sensor_data = self.get_sensor_data()
        if not sensor_data:
            return self.get_return_value()
        
        sensor_data = self.filter_data_by_dates(sensor_data)
        if not sensor_data:
            return self.get_return_value()
        
        if not self.metrics:
            return self.get_return_value()

        for metric in self.metrics:
            self.averages[metric] = self.get_average_for_metric(metric, sensor_data)

        return self.get_return_value()

    def get_sensor_data(self):
        sensors = list(map(lambda uuid: SensorData.get_sensor_data_by_sensor_uuid(uuid), self.sensor_uuids))
        return [item for sensor_data in sensors for item in sensor_data]
    
    def filter_data_by_dates(self, sensor_data):
        return [ data for data in sensor_data
            if self.start_day <= self.__parse_datetime(data.created_at) <= self.end_day]
            
    def get_average_for_metric(self, metric, sensor_data):
        return reduce(lambda x,y: x+y, [vars(data)[metric] for data in sensor_data]) / len(sensor_data)

    def get_return_value(self):
        return {
            "sensors": self.sensor_uuids,
            "metrics": self.metrics,
            "start_day": self.start_day,
            "end_day": self.end_day,
            "averages": self.averages
        }
    ### Private Methods

    def __parse_arg(self, arg):
        if "," in arg:
            return arg.split(",")
        return [arg]

    def __parse_day(self, arg):
        return datetime.strptime(arg, "%d-%m-%Y")

    def __parse_datetime(self, arg):
        return datetime.strptime(arg, "%Y-%m-%d %H:%M:%S")