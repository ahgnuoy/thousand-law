from typing import List
from node import Node
class Mok(Node):
    def __init__(self, raw: str):
        self.level = 5
        self.raw = raw
        self.text = raw
        self.children: List[Node] = []
        self.__parse()
    
    def __parse(self):
        pass