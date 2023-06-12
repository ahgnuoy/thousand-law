from typing import List
from node import Node
class Hang(Node):
    def __init__(self, raw: str):
        self.raw = raw
        self.text = raw
        self.children: List[Node] = []
        self.__parse()
    
    def __parse(self):
        pass