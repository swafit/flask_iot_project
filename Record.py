# record model class
from datetime import datetime

class Record():
    timestamp: datetime
    temperature: float
    humidity: float
    motiondetected: bool
    deviceid: int
