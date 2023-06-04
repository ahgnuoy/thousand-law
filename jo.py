from node import Node
class Jo(Node):
    def __init__(self, text: str):
        self.raw = text
        self.children: Node = []
    
    def __parse(self, text: str):
        pass