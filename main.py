from datetime import datetime, timedelta
import tkinter as tk
import json

days = ["Sun", "Mon", "Tues", "Weds", "Thurs", "Fri", "Sat"]

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

class Tile():
    def __init__(self, block:Block, box:tk.Frame, row:int, column:int):
        self.block = block
        self.box = box
        self.row = row
        self.column = column

def generate_tiles(root: tk.Tk, gridWidth: int, gridHeight: int, tileWidth:int, tileHeight:int, startTime:int, timeInterval:int):
    start_time = datetime(2000, 1, 1, startTime, 0)  # arbitrary date, just care about time
    times = [start_time + timedelta(minutes=timeInterval * i) for i in range(gridHeight - 1)]

    for y in range(gridHeight):
        for x in range(gridWidth):
            box = tk.Frame(root, width=tileWidth, height=tileHeight, bg="gray",
                highlightthickness=1, highlightbackground="black", highlightcolor="black")
            box.grid(row=y, column=x, sticky="nsew")
            box.grid_propagate(False)
            t = Tile(Block("", datetime.now(), datetime.now(), "gray", ["#empty"]), box, x, y)

            if x == 0 and y != 0:
                lbl = tk.Label(box, text=times[y-1].strftime("%I:%M"), padx=0, pady=0, bg="gray")
                lbl.place(relx=0.5, rely=0.5, anchor="center")

            if y == 0 and x != 0:
                lbl = tk.Label(box, text=days[x-1], padx=0, pady=0, bg="gray")
                lbl.place(relx=0.5, rely=0.5, anchor="center")

    root.update_idletasks()
    root.update()

root = tk.Tk()
root.title("Time Blocking App")

generate_tiles(root, 8, 33, 60, 25, 6, 30)

root.mainloop()