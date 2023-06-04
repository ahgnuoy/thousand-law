import re
from jang import Jang
from jo import Jo
from hang import Hang
from node import Node
from mark import Mark
from typing import List

class Helper:
    # __deli = ["전문", "제[0-9]+장", "제[0-9]+절", "제[0-9]+관", "제[0-9]+조"]
    # part regex
    __part = ["\s+전문", "\s+부칙"]
    # delimeter level regex
    # ①-⑳ u+2460 u+2473 
    # ㉑-㉟ u+3251 u+325F
    # ㊱-㊿ u+32B1 u+32BF
    __dl = ["제[0-9]+장", "제[0-9]+조", "[①-⑳]"] 
    # page header and footer regex
    __pdl = ["법제처\s+[0-9]+\s+국가법령정보센터", "대한민국헌법 \\n"]
    def __init__(self):
        pass

    @staticmethod
    def split(pages, level: int) -> List[Node]:
        # level 0 전문, 장, 부칙
        mark_list: List[Mark] = []
        node_list: List[Node] = []
        if level == 0:
            l0 = re.compile(Helper.__part[0])
            l1 = re.compile(Helper.__dl[0])
            l2 = re.compile(Helper.__part[1])
            for index, text in enumerate(pages):
                iter0 = l0.finditer(text)
                iter1 = l1.finditer(text)
                iter2 = l2.finditer(text)
                for i0 in iter0:
                    mark_list.append(Mark(index, i0.span()[0]))
                for i1 in iter1:
                    mark_list.append(Mark(index, i1.span()[0]))
                for i2 in iter2:
                    mark_list.append(Mark(index, i2.span()[0]))
            for index, mark in enumerate(mark_list):
                if index == len(mark_list) - 1:
                    node_list.append(Jang(Helper.__clear_page_header_footer(Helper.__extract_til_end(pages, mark_list[index]))))
                else:
                    node_list.append(Jang(Helper.__clear_page_header_footer(Helper.__extract(pages, mark_list[index], mark_list[index + 1]))))
        elif level == 1:
            l0 = re.compile(Helper.__dl[1])
            for index, text in enumerate(pages):
                iter0 = l0.finditer(text)
                for i0 in iter0:
                    mark_list.append(Mark(index, i0.span()[0]))
            for index, mark in enumerate(mark_list):
                if index == len(mark_list) - 1:
                    node_list.append(Jo(Helper.__extract_til_end(pages, mark_list[index])))
                else:
                    node_list.append(Jo(Helper.__extract(pages, mark_list[index], mark_list[index + 1])))
        elif level == 2:
            l0 = re.compile(Helper.__dl[2])
            for index, text in enumerate(pages):
                iter0 = l0.finditer(text)
                for i0 in iter0:
                    mark_list.append(Mark(index, i0.span()[0]))
            for index, mark in enumerate(mark_list):
                if index == len(mark_list) - 1:
                    node_list.append(Hang(Helper.__clear_line_feed(Helper.__extract_til_end(pages, mark_list[index]))))
                else:
                    node_list.append(Hang(Helper.__clear_line_feed(Helper.__extract(pages, mark_list[index], mark_list[index + 1]))))
            pass
        else:
            pass
        return node_list

    def __clear_page_header_footer(text: str):
        l0 = re.compile(Helper.__pdl[0])
        sl0 = l0.findall(text)
        for s in sl0:
            text = text.replace(s,"")
            
        l1 = re.compile(Helper.__pdl[1])
        sl1 = l1.findall(text)
        for s in sl1:
            text = text.replace(s,"")

        return text

    def __clear_line_feed(text: str):
        l0 = re.compile("\n")
        sl0 = l0.findall(text)
        for s in sl0:
            text = text.replace(s,"")

        return text

    def __extract(pages, frm: Mark, t: Mark): 
        text = ""
        if frm.page == t.page:
            text = pages[frm.page][frm.index:t.index]
        else:
            for i in range(frm.page, t.page + 1):
                if i == frm.page:
                    text += pages[i][frm.index:]
                elif i == t.page:
                    text += pages[i][:t.index]
                else:
                    text += pages[i][:]
        return text

    def __extract_til_end(pages, mark: Mark):
        text = ""
        for i in range(mark.page, len(pages)):
            if i == mark.page:
                text += pages[i][mark.index:]
            else:
                text += pages[i][:]
        return text

