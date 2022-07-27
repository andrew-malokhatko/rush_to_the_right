from pathlib import Path
import struct
from game.block import tBlock

class Editor:
    """def create_map(self):
        with open(self.levels_path / self.name, "wb") as f:
            for i in range(30):
                for k in range(10):
                    data = struct.pack("hhh", i, k, 0)
                    f.write(data)"""

    def load_map(self, file: Path):

        with open(file, "rb") as f:
            version = f.read(2)
            data = f.read(6)
            map_args = []

            while len(data) == 6:
                 x, y, id = struct.unpack("hhh", data)
                 map_args.append(tBlock(x, y, id))
                 data = f.read(6)

        return map_args

    def save_map(self, file: Path, blocks):
         with open(file, "wb") as f:
            f.write(struct.pack("h", 0)) # version
            for block in blocks:
                data = struct.pack("hhh", block[0], block[1], blocks[block].id)
                f.write(data)




"""       map structure 

00 00    object =  00 00   00 00  00 00

 ver_h                 h_x     h_y   h_id

"""