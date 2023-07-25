import re
from mark import Mark
from typing import List, Tuple

class Helper:
    # __deli = ["전문", "제[0-9]+장", "제[0-9]+절", "제[0-9]+관", "제[0-9]+조"]
    __deli = [ ["\n\s+제", "장"], ["\n\s+제", "절"], ["\n제", "조"], [], ["\n","\."], [], ["\n", ")"] ]
    # level 3 
    __hang_deli = [ "\s①", "\n②", "\n③", "\n④", "\n⑤", "\n⑥", "\n⑦", "\n⑧", "\n⑨", "\n⑩", "\n⑪", "\n⑫", "\n⑬", "\n⑭", "\n⑮", "\n⑯", "\n⑰", "\n⑱", "\n⑲", "\n⑳", "\n㉑", "\n㉒", "\n㉓", "\n㉔", "\n㉕", "\n㉖", "\n㉗", "\n㉘", "\n㉙", "\n㉚", "\n㉛", "\n㉜", "\n㉝", "\n㉞", "\n㉟", "\n㊱", "\n㊲", "\n㊳", "\n㊴", "\n㊵", "\n㊶", "\n㊷", "\n㊸", "\n㊹", "\n㊺", "\n㊻", "\n㊼", "\n㊽", "\n㊾", "\n㊿" ]
    # level 5
    __mok_deli = [ "\n가\.", "\n나\.", "\n다\.", "\n라\.", "\n마\.", "\n바\.", "\n사\.", "\n아\.", "\n자\.", "\n차\.", "\n카\.", "\n타\.", "\n파\.", "\n하\." ] 
    # part regex
    __part = ["\s+전문", "\s+부칙"]
    # delimeter level regex
    # ①-⑳ u+2460 u+2473 
    # ㉑-㉟ u+3251 u+325F
    # ㊱-㊿ u+32B1 u+32BF
    __dl = ["제[0-9]+장|\s+전문|\s+부칙", "\n제[0-9]+절", "\n제[0-9]+조", "\s①|\n[②-⑳]"] 
    # page header and footer regex
    __pdl = ["법제처\s+[0-9]+\s+국가법령정보센터", "대한민국헌법 \\n"]
    def __init__(self):
        pass

    @staticmethod
    def forehead_split_mark_l(pages: List[str], level: int, index: int) -> Mark:
        return Helper.__find_mark_l(pages, Helper.__make_deli(level, index))

    @staticmethod
    def forehead_split_s(text: str, level: int, index: int) -> str:
        return Helper.__find_pos_s(text, Helper.__make_deli(level, index))
    
    @staticmethod
    def clear_pages_header_footer(pages: List[str]) -> List[str]:
        for index, page in enumerate(pages):
            pages[index] = Helper.__clear_page_header_footer(page)
        return pages

    @staticmethod
    def pages_extract(pages: List[str], frm: Mark, t: Mark) -> str: 
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

    @staticmethod
    def pages_extract_til_end(pages: List[str], mark: Mark) -> str:
        text = ""
        for i in range(mark.page, len(pages)):
            if i == mark.page:
                text += pages[i][mark.index:]
            else:
                text += pages[i][:]
        return text

    @staticmethod
    def match_and_slice(original: str, match: str) -> str:
        found_index = original.find(match)
        return original[:] if found_index < 0 else original[:found_index]

    @staticmethod
    def check_got_level(text: str, level: int, index: int):
        comp = re.compile(Helper.__make_deli(level, index if level == 1 or level == 2 else 0))
        sear = comp.search(text)
        if sear is not None:
            return True
        else:
            return False

    def __make_deli(level: int, index: int) -> str:
        '''
        @param\n
        level int (jang, jeol, jo, hang)\n
        index int\n
        @return\n
        (level = 1, index = 2) -> "\\n제2절"
        '''
        if level == 3:
            return Helper.__hang_deli[index]
        elif level ==5:
            return Helper.__mok_deli[index]
        else:
            return Helper.__deli[level][0] + str(index+1) + Helper.__deli[level][1]

    def __find_mark_l(pages: List[str], deli: str) -> Mark:
        mark_list: List[Mark] = []
        comp = re.compile(deli)
        for index, page in enumerate(pages):
            iter = comp.finditer(page)
            for it in iter:
                mark_list.append(Mark(index, it.span()[0]))

        if len(mark_list) == 1:
            return mark_list[0]
        elif len(mark_list) == 0:
            # something goes wrong
            return None
        else: 
            # len(mark_list) > 1
            return None

    def __find_pos_s(text: str, deli: str) -> int:
        pos_list: List[int] = []
        comp = re.compile(deli)
        iter = comp.finditer(text)
        for it in iter:
            pos_list.append(it.span()[0])
        
        if len(pos_list) == 1:
            return pos_list[0]
        elif len(pos_list) == 0:
            return -1
        else: # 11조의2 변수 발생으로 첫번째 pos_iter return 
            return pos_list[0]

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

    @staticmethod
    def process_text(text: str) -> str:
        return Helper.__trim_white_spaces(Helper.__clear_line_feed(text))

    def __clear_line_feed(text: str) -> str:
        l0 = re.compile("\n")
        sl0 = l0.findall(text)
        for s in sl0:
            text = text.replace(s,"")

        return text
    
    def __trim_white_spaces(text: str) -> str:
        l0 = re.compile("^\s+")
        sl0 = l0.findall(text)
        for s in sl0:
            text = text.replace(s,"")

        return text
