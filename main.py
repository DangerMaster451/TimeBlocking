from datetime import datetime, timedelta
import tkinter as tk
import json

days = ["Sun", "Mon", "Tues", "Weds", "Thurs", "Fri", "Sat"]
# https://coolors.co/fcf7ff-c4cad0-878c8f-a4969b-655560

class Block():
    def __init__(self, name: str, startTime: datetime, endTime: datetime, color, tags: list[str]) -> None:
        self.name: str = name
        self.startTime: datetime = startTime
        self.endTime: datetime = endTime
        self.color = color
        self.tags = tags

    def toJSON(self) -> str:
        return json.dumps({"name": self.name, "startTime": self.startTime.strftime("%Y-%m-%d %H:%M:%S"),
                            "endTime": self.endTime.strftime("%Y-%m-%d %H:%M:%S"), "color": self.color,
                            "tags": self.tags})

    @classmethod
    def fromJSON(cls, json_str: str):
        data = json.loads(json_str)
        format = "%Y-%m-%d %H:%M:%S"
        return cls(data["name"], datetime.strptime(data["startTime"], format),
                    datetime.strptime(data["endTime"], format), data["color"], data["tags"])

class Tile():
    def __init__(self, block:Block, box:tk.Frame, row:int, column:int, label:tk.Label|None = None):
        self.block = block
        self.box = box
        self.row = row
        self.column = column
        self.label = label

        self.box.bind("<Button-1>", self.on_click)
        if self.label:
            self.label.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        if self.label:
            self.label.config(text="test")
        
def generate_tiles(root: tk.Tk, gridWidth: int, gridHeight: int, tileWidth: int, tileHeight: int, startTime: int, timeInterval: int):
    start_time = datetime(2000, 1, 1, startTime, 0)
    times = [start_time + timedelta(minutes=timeInterval * i) for i in range(gridHeight - 1)]

    tiles = {}

    for y in range(gridHeight):
        for x in range(gridWidth):
            box = tk.Frame(root, width=tileWidth, height=tileHeight, bg="#FCF7FF",
                            highlightthickness=1, highlightbackground="#878C8F", highlightcolor="#878C8F")
            box.grid(row=y, column=x, sticky="nsew")
            box.grid_propagate(False)
            lbl = tk.Label(box, text="", padx=0, pady=0, bg="#FCF7FF", font=("Arial", 10), fg="#878C8F")
            lbl.place(relx=0.5, rely=0.5, anchor="center")

            if x == 0 and y != 0:
                lbl.config(text=times[y-1].strftime("%I:%M").lstrip("0"))

            if y == 0 and x != 0:
                lbl.config(text=days[x-1])

            t = Tile(Block("", datetime.now(), datetime.now(), "#FCF7FF", ["#empty"]), box, y, x, lbl)
            tiles[(x, y)] = t

    root.update_idletasks()
    root.update()

    return tiles


root = tk.Tk()
root.title("Time Blocking App")

tiles = generate_tiles(root, 8, 34, 60, 23, 6, 30)

root.mainloop()