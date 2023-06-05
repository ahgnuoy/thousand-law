import re
from mark import Mark
from jang import Jang
from helper import Helper
from typing import List

class Law:
    __raw = []
    __jangs: List[Jang] = []
    __temp_mark: Mark

    def __init__(self, pages):
        self.__raw = pages
        self.__temp_mark = Mark(0, 0)
        self.__parse()
    
    def print_all(self):
        pass

    def __parse(self):
        self.__jangs = Helper.split(self.__raw, level=0)
        for jang in self.__jangs:
            jang.children = Helper.split([jang.raw], level=1)
            for jeol in jang.children:
                jeol.children = Helper.split([jeol.raw], level=2)
                for jo in jeol.children:
                    jo.children = Helper.split([jo.raw], level=3)

        for jang in self.__jangs:
            for jeol in jang.children:
                for jo in jang.children:
                    for hang in jo.children:
                        print(hang.raw)
    
    def make_file(self):
        f = open("out.txt", "w", encoding="utf-8")
        for jang in self.__jangs:
            for jo in jang.children:
                for hang in jo.children:
                    f.write(hang.raw)
        f.close()
