from __future__ import annotations
from mark import Mark
from typing import List
class Node:
    raw:str = ""
    text:str = ""
    mark:Mark = None
    children: List = []
    def __init__(self):
        pass