from node import Node
from jang import Jang
from helper import Helper
from typing import List
from mark import Mark
import json

class Law:
    raw = []
    jangs: List[Node] = []

    def __init__(self, pages):
        self.raw = Helper.clear_pages_header_footer(pages)
        self.__parse()

    def __parse(self):
        temp_mark = Mark(0,0)
        index = 0
        while True:
            mark = Helper.forehead_split_mark_l(self.raw, 0, index)
            if mark is not None:
                self.jangs.append(Jang(Helper.pages_extract(self.raw, temp_mark, mark), temp_mark))
                temp_mark = mark
            else:
                self.jangs.append(Jang(Helper.pages_extract_til_end(self.raw, temp_mark), temp_mark))
                temp_mark = Mark(0,0)
                break
            index += 1
            
        # 첫 노드가 전문인지 확인
        # 순차적으로 생성하며 더 이상 장을 찾을 수 없을 때까지
        # 마지막 노드가 부칙인지 확인
        # pages 구조를 그대로 유지: 합쳐서 하나의 str 변수로 만들경우 득과 실이 무엇인지
    
    def make_file(self):
        '''
        not working properly
        '''
        f = open("out.txt", "w", encoding="utf-8")
        json.dump(self.make_dict(), f, indent=2, ensure_ascii=False)
        f.close()

    def make_dict(self):
        out = {}
        for index, jang in enumerate(self.jangs):
            out[f"{index}"] = {}
            out[f"{index}"]["text"] = jang.text
            out[f"{index}"]["children"] = self.make_children_dict(jang)
        return out
    
    def make_children_dict(self, node: Node):
        out = {}
        if len(node.children) == 0:
            return {}
        else:
            for index, child in enumerate(node.children):
                out[f"{index}"] = {}
                out[f"{index}"]["text"] = child.text
                out[f"{index}"]["children"] = self.make_children_dict(child)
        return out


