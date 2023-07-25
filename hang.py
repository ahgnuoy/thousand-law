from helper import Helper
from typing import List
from node import Node
from ho import Ho
from counter import Counter
class Hang(Node):
    def __init__(self, raw: str, counter: Counter):
        self.level = 3
        self.raw = raw
        self.text = raw
        self.counter: Counter = counter
        self.counter.value[3] += 1
        self.children: List[Node] = []
        self.__parse()
    
    def __parse(self):
        index = 0
        if Helper.check_got_level(self.raw, 4, index):
            pos = Helper.forehead_split_s(self.raw, 4, index)
            temp_pos = pos
            while True:
                pos = Helper.forehead_split_s(self.raw, 4, index + 1)
                if pos > 0:
                    self.children.append(Ho(self.raw[temp_pos:pos], self.counter))
                    temp_pos = pos
                else:
                    self.children.append(Ho(self.raw[temp_pos:], self.counter))
                    break
                index += 1
        else:
            # 조 하위에 호가 없음
            pass

        first_child = self.children[0] if len(self.children) != 0 else None
        if first_child is not None:
            self.text = Helper.match_and_slice(self.raw, first_child.raw)
        else:
            self.text = self.raw