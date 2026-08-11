from datetime import datetime
import json

class Block():
    def __init__(self, name:str, startTime:datetime, endTime:datetime) -> None:
        self.name:str = name
        self.startTime:datetime = startTime
        self.endTime:datetime = endTime

    @classmethod
    def fromJSON(cls, json_str:str):
        data = json.loads(json_str)
        return cls(name=data["name"], startTime=data["startTime"], endTime=data["endTime"])

    def toJSON(self) -> str:
        return f'{{"name":"{self.name}", "startTime":"{self.startTime}", "endTime":"{self.endTime}"}}'