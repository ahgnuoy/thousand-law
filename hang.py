from typing import List
from node import Node
from mark import Mark
class Hang(Node):
    def __init__(self, raw: str, mark: Mark):
        self.raw = raw
        self.mark = mark
        self.children: List[Node] = []
        self.__parse()
    
    def __parse(self):
        pass