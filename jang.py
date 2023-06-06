from helper import Helper
from node import Node
from jeol import Jeol
from jo import Jo
from mark import Mark
from typing import List
class Jang(Node):
    def __init__(self, raw: str, mark: Mark):
        self.raw = raw
        self.mark = mark
        self.jeols: List[Jeol] = []
        self.jos: List[Jo] = []
        self.__parse()
    
    def __parse(self):
        tl = Helper.split(self.raw, level=1)
        if len(tl) != 0:
            for item in tl:
                self.jeols.append(Jeol(item[0], item[1]))
        else:
            tl = Helper.split(self.raw, level=2)
            if len(tl) != 0:
                for item in tl:
                    self.jos.append(Jo(item[0], item[1]))