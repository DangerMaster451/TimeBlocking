from datetime import datetime
import json

class Block():
    def __init__(self, name:str, startTime:datetime, endTime:datetime, color, tags:list[str]) -> None:
        self.name:str = name
        self.startTime:datetime = startTime
        self.endTime:datetime = endTime
        self.color = color
        self.tags = tags

    def toJSON(self) -> str:
        return json.dumps({"name": self.name, "startTime": self.startTime.strftime("%Y-%m-%d %H:%M:%S"), 
                           "endTime": self.endTime.strftime("%Y-%m-%d %H:%M:%S"), "color": self.color,
                           "tags": self.tags})

    @classmethod
    def fromJSON(cls, json_str:str):
        data = json.loads(json_str)
        format = "%Y-%m-%d %H:%M:%S"
        return cls(data["name"], datetime.strptime(data["startTime"], format),
                   datetime.strptime(data["endTime"], format), data["color"], data["tags"])

   

b = Block("Band", datetime(2000, 1, 1, 0, 0, 0), datetime(2000, 1, 1, 1, 0, 0), "white", ["#busy"])
s = b.toJSON()
print(s)
c = Block.fromJSON(s)
print(c.tags)