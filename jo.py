from helper import Helper
from typing import List
from node import Node
from hang import Hang
from counter import Counter
class Jo(Node):
    def __init__(self, raw: str, counter: Counter):
        self.raw = raw
        self.children: List[Hang] = []
        self.counter: Counter = counter
        self.counter.value[2] += 1
        self.__parse()
    
    def __parse(self):
        index = 0
        if Helper.check_got_level(self.raw, 3, index):
            # 조 하위에 항이 있음
            pos = Helper.forehead_split_s(self.raw, 3, index)
            temp_pos = pos
            while True:
                pos = Helper.forehead_split_s(self.raw, 3, index + 1)
                if pos > 0:
                    self.children.append(Hang(self.raw[temp_pos:pos], self.counter))
                    temp_pos = pos
                else:
                    self.children.append(Hang(self.raw[temp_pos:], self.counter))
                    break
                index += 1
        else:
            # 조 하위에 항이 없음
            pass

        first_child = self.children[0] if len(self.children) != 0 else None
        if first_child is not None:
            self.text = Helper.match_and_slice(self.raw, first_child.raw)
        else:
            self.text = self.raw