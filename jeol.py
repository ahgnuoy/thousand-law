from helper import Helper
from typing import List
from node import Node
from jo import Jo
class Jeol(Node):
    def __init__(self, raw: str):
        self.raw = raw
        self.children: List[Node] = []
        self.__parse()
    
    def __parse(self):
        temp_pos = 0
        index = 0
        while True:
            pos = Helper.forehead_split_s(self.raw, 2, index)
            if pos > 0:
                self.children.append(Jo(self.raw[temp_pos:pos]))
                temp_pos = pos
            else:
                self.children.append(Jo(self.raw[temp_pos:]))
                break
            index += 1
        first_child = self.children[0] if len(self.children) != 0 else None
        if first_child is not None:
            self.text = Helper.match_and_slice(self.raw, first_child.raw)