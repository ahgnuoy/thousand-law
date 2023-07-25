from helper import Helper
from typing import List
from node import Node
from mok import Mok
from counter import Counter
class Ho(Node):
    def __init__(self, raw: str, counter: Counter):
        self.level = 4
        self.raw = raw
        self.text = raw
        self.counter = counter
        self.counter.value[4] += 1
        self.children: List[Node] = []
        self.__parse()
    
    def __parse(self):
        index = 0
        if Helper.check_got_level(self.raw, 5, index):
            pos = Helper.forehead_split_s(self.raw, 5, index)
            temp_pos = pos
            while True:
                pos = Helper.forehead_split_s(self.raw, 5, index + 1)
                if pos > 0:
                    self.children.append(Mok(self.raw[temp_pos:pos]))
                    temp_pos = pos
                else:
                    self.children.append(Mok(self.raw[temp_pos:]))
                    break
                index += 1
        else:
            # 조 하위에 목이 없음
            pass

        first_child = self.children[0] if len(self.children) != 0 else None
        if first_child is not None:
            self.text = Helper.match_and_slice(self.raw, first_child.raw)
        else:
            self.text = self.raw