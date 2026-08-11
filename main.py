from datetime import datetime
import json

class Block():
    def __init__(self, name:str, startTime:datetime, endTime:datetime, color) -> None:
        self.name:str = name
        self.startTime:datetime = startTime
        self.endTime:datetime = endTime
        self.color = color

    @classmethod
    def fromJSON(cls, json_str:str):
        data = json.loads(json_str)
        return cls(name=data["name"], startTime=data["startTime"], endTime=data["endTime"], color=data["color"])

    def toJSON(self) -> str:
        return f'{{"name":"{self.name}", "startTime":"{self.startTime}", "endTime":"{self.endTime}", "color":"{self.color}"}}'

b = Block("Band", datetime(2000, 1, 1, 0, 0, 0), datetime(2000, 1, 1, 1, 0, 0), "white")
s = b.toJSON()
c = Block.fromJSON(s)
print(c.startTime)