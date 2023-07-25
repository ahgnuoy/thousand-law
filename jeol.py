from helper import Helper
from typing import List
from node import Node
from jo import Jo
from counter import Counter
class Jeol(Node):
    def __init__(self, raw: str, counter: Counter):
        self.level = 1
        self.raw = raw
        self.children: List[Node] = []
        self.counter = counter
        self.__parse()
    
    def __parse(self):
        temp_pos = 0
        index = 0
        pos = Helper.forehead_split_s(self.raw, 2, self.counter.value[2])
        temp_pos = pos
        while True:
            pos = Helper.forehead_split_s(self.raw, 2, self.counter.value[2] + 1)
            if pos > 0:
                self.children.append(Jo(self.raw[temp_pos:pos], self.counter))
                temp_pos = pos
            else:
                self.children.append(Jo(self.raw[temp_pos:], self.counter))
                break
            index += 1
        first_child = self.children[0] if len(self.children) != 0 else None
        if first_child is not None:
            self.text = Helper.match_and_slice(self.raw, first_child.raw)