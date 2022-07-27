import struct
from pathlib import Path

def create_map():
        with open(Path(__file__).parent / "level_1", "wb") as f:
            f.write(struct.pack("h", 0))
            for i in range(30):
                for k in range(10):
                    if k%2 ==0:
                        data = struct.pack("hhh", i, k, 0)
                    else:
                        data = struct.pack("hhh", i, k, 1)
                    f.write(data)

create_map()