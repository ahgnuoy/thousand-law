from helper import Helper
from typing import List
from node import Node
from jo import Jo
from mark import Mark
class Jeol(Node):
    def __init__(self, raw: str, mark: Mark):
        self.raw = raw
        self.mark = mark
        self.jos: List[Jo] = []
        self.__parse()
    
    def __parse(self):
        tl = Helper.split(self.raw, level=2)
        if len(tl) != 0:
            for item in tl:
                self.jos.append(Jo(item[0], item[1]))
        first_child = self.jos[0] if len(self.jos) != 0 else None
        if first_child is not None:
            self.text = Helper.match_and_slice(self.raw, first_child.raw)