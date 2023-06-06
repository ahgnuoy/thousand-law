import re
from mark import Mark
from typing import List, Tuple

class Helper:
    # __deli = ["전문", "제[0-9]+장", "제[0-9]+절", "제[0-9]+관", "제[0-9]+조"]
    # part regex
    __part = ["\s+전문", "\s+부칙"]
    # delimeter level regex
    # ①-⑳ u+2460 u+2473 
    # ㉑-㉟ u+3251 u+325F
    # ㊱-㊿ u+32B1 u+32BF
    __dl = ["제[0-9]+장|\s+전문|\s+부칙", "제[0-9]+절", "제[0-9]+조", "[①-⑳]"] 
    # page header and footer regex
    __pdl = ["법제처\s+[0-9]+\s+국가법령정보센터", "대한민국헌법 \\n"]
    def __init__(self):
        pass

    @staticmethod
    def split(text: str, level: int) -> List[Tuple]:
        mark_list: List[Mark] = []
        tuple_list: List[Tuple] = []
        # 전문, 장, 부칙
        comp = re.compile(Helper.__dl[level])
        iter = comp.finditer(text)
        for index, it in enumerate(iter):
            mark_list.append(Mark(index, it.span()[0]))
        for index, mark in enumerate(mark_list):
            if index == len(mark_list) - 1:
                tuple_list.append((Helper.__extract_til_end(text, mark), mark))
            else:
                tuple_list.append((Helper.__extract(text, mark, mark_list[index + 1]), mark))
        return tuple_list

    def pages_split(pages: List[str], level: int) -> List[Tuple]:
        mark_list: List[Mark] = []
        tuple_list: List[Tuple] = []
        # 전문, 장, 부칙
        comp = re.compile(Helper.__dl[level])
        for index, text in enumerate(pages):
            iter = comp.finditer(text)
            for i in iter:
                mark_list.append(Mark(index, i.span()[0]))
        for index, mark in enumerate(mark_list):
            if index == len(mark_list) - 1:
                tuple_list.append((Helper.__pages_extract_til_end(pages, mark), mark))
            else:
                tuple_list.append((Helper.__pages_extract(pages, mark, mark_list[index + 1]), mark))
        return tuple_list
    
    def clear_pages_header_footer(pages: List[str]) -> List[str]:
        for page in pages:
            page = Helper.__clear_page_header_footer(page)
        return pages

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

    def __pages_extract(pages: List[str], frm: Mark, t: Mark) -> str: 
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

    def __pages_extract_til_end(pages: List[str], mark: Mark) -> str:
        text = ""
        for i in range(mark.page, len(pages)):
            if i == mark.page:
                text += pages[i][mark.index:]
            else:
                text += pages[i][:]
        return text

    def __extract(text: str, frm: Mark, t: Mark) -> str: 
        return text[frm.index:t.index]

    def __extract_til_end(text: str, mark: Mark) -> str:
        return text[mark.index:]

