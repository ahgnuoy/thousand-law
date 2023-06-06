from helper import Helper
from typing import List
from node import Node
from hang import Hang
from mark import Mark
class Jo(Node):
    def __init__(self, raw: str, mark: Mark):
        self.raw = raw
        self.mark = mark
        self.hangs: List[Hang] = []
        self.__parse()
    
    def __parse(self):
        tl = Helper.split(self.raw, level=3)
        if len(tl) != 0:
            for item in tl:
                self.hangs.append(Hang(item[0], item[1]))