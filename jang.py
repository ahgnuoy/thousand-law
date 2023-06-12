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
        self.children: List[Node] = []
        self.__parse()
    
    def __parse(self):
        temp_pos = 0
        index = 0
        # 절 체크
        # 조로 바로 넘어갈 수 있음
        # 조의 누적 카운트
        if Helper.check_got_jeol(self.raw):
            while True:
                pos = Helper.forehead_split_s(self.raw, 1, index)
                if pos > 0:
                    self.children.append(Jeol(self.raw[temp_pos:pos]))
                    temp_pos = pos
                else:
                    self.children.append(Jeol(self.raw[temp_pos:]))
                    break
                index += 1
        elif Helper.check_got_jo(self.raw):
            while True:
                pos = Helper.forehead_split_s(self.raw, 2, index)
                if pos > 0:
                    self.children.append(Jo(self.raw[temp_pos:pos]))
                    temp_pos = pos
                else:
                    self.children.append(Jo(self.raw[temp_pos:]))
                    break
                index += 1

        first_child = self.children[0] if len(self.children) != 0 else None
        if first_child is not None:
            self.text = Helper.match_and_slice(self.raw, first_child.raw)
        else:
            self.text = self.raw
    