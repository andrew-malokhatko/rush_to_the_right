from pathlib import Path
import struct
from game.block import Block

class Creator:
    def __init__(self, name):
        self.name = name
        self.levels_path = Path(__file__).parent.parent / "my_levels"

    def create_map(self):
        with open(self.levels_path / self.name, "wb") as f:
            for i in range(30):
                for k in range(10):
                    data = struct.pack("hhh", i, k, 0)
                    f.write(data)

    def load_map(self, file: Path):
        with open(file, "rb") as f:
            version = f.read(2)
            #some version checks
            data = f.read(6)
            map = {}

            while len(data) == 6:
                 x, y, id = struct.unpack("hhh", data)
                 map[x, y] = Block(id, x, y)
                 data = f.read(6)

        return map


"""       map structure 

00 00    object =  00 00   00 00  00 00

 ver_h                 h_x     h_y   h_id

"""