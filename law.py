from node import Node
from jang import Jang
from helper import Helper
from typing import List, Dict
import json

class Law:
    raw = []
    jangs: List[Jang] = []

    def __init__(self, pages):
        self.raw = Helper.clear_pages_header_footer(pages)
        self.__parse()

    def __parse(self):
        root = Node()
        for item in Helper.pages_split(self.raw, level=0):
            self.jangs.append(Jang(item[0], item[1]))
    
    def make_file(self):
        f = open("out.txt", "w", encoding="utf-8")
        json.dump(self.make_dict(), f, indent=2, ensure_ascii=False)
        f.close()

    def make_dict(self):
        out = {}
        # 절 없이 바로 조로 넘어감
        for index0, jang in enumerate(self.jangs):
            out[f"{index0}"] = {}
            out[f"{index0}"]["text"] = jang.text
            out[f"{index0}"]["children"] = {}
            if len(jang.jeols) != 0:
                for index1, jeol in enumerate(jang.jeols):
                    out[f"{index0}"]["children"][f"{index1}"] = {}
                    out[f"{index0}"]["children"][f"{index1}"]["text"] = jeol.text
                    out[f"{index0}"]["children"][f"{index1}"]["children"] = {}
                    if len(jeol.jos) != 0:
                        for index2, jo in enumerate(jeol.jos):
                            out[f"{index0}"]["children"][f"{index1}"]["children"][f"{index2}"] = {}
                            out[f"{index0}"]["children"][f"{index1}"]["children"][f"{index2}"]["text"] = jo.text
                            out[f"{index0}"]["children"][f"{index1}"]["children"][f"{index2}"]["children"] = {}
                            if len(jo.hangs) != 0:
                                for index3, hang in enumerate(jo.hangs):
                                    out[f"{index0}"]["children"][f"{index1}"]["children"][f"{index2}"]["children"][f"{index3}"] = {}
                                    out[f"{index0}"]["children"][f"{index1}"]["children"][f"{index2}"]["children"][f"{index3}"]["text"] = hang.raw
                                    out[f"{index0}"]["children"][f"{index1}"]["children"][f"{index2}"]["children"][f"{index3}"]["children"] = {}
            elif len(jang.jos) != 0:
                for index1, jo in enumerate(jang.jos):
                    out[f"{index0}"]["children"][f"{index1}"] = {}
                    out[f"{index0}"]["children"][f"{index1}"]["text"] = jo.text
                    out[f"{index0}"]["children"][f"{index1}"]["children"] = {}
                    if len(jo.hangs) != 0:
                        for index2, hang in enumerate(jo.hangs):
                            out[f"{index0}"]["children"][f"{index1}"]["children"][f"{index2}"] = {}
                            out[f"{index0}"]["children"][f"{index1}"]["children"][f"{index2}"]["text"] = hang.raw
                            out[f"{index0}"]["children"][f"{index1}"]["children"][f"{index2}"]["children"] = {}
            else:
                pass
        return out


