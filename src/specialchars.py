from pdf import *
"""This file is messy. Try not to use it!"""

class SpecialChar:
    def __init__(self,char:str,fontforge_height:int) -> None:
        self.char = char
        self.fontfore_height = fontforge_height

    def get_height(self):
        return get_font_size()/677*self.fontfore_height  #=how high are 10mm in fontforge * height of bracket in fontforge

    def render(self):
        write_text(self.char)


def left_bracket_top(): return SpecialChar("⎛",1495)
def left_bracket_middle(): return SpecialChar("⎜",498)
def left_bracket_bottom(): return SpecialChar("⎝",1495)


def right_bracket_top(): return SpecialChar("⎞",1495)
def right_bracket_middle(): return SpecialChar("⎟",498)
def right_bracket_bottom(): return SpecialChar("⎠",1495)

def left_square_top(): return SpecialChar("⎡",1500)
def left_square_middle(): return SpecialChar("⎢",1000)
def left_square_bottom(): return SpecialChar("⎣",1500)

def right_square_top(): return SpecialChar("⎤",1500)
def right_square_middle(): return SpecialChar("⎥",1000)
def right_square_bottom(): return SpecialChar("⎦",1500)

def left_curly_top(): return SpecialChar("⎧",750)
def left_curly_middle1(): return SpecialChar("⎪",748/2)
def left_curly_middle2(): return SpecialChar("⎨",1500)
def left_curly_bottom(): return SpecialChar("⎩",750)

def right_curly_top(): return SpecialChar("⎫",750)
def right_curly_middle1(): return SpecialChar("⎪",748/2)
def right_curly_middle2(): return SpecialChar("⎬",1500)
def right_curly_bottom(): return SpecialChar("⎭",750)

def integral_top(): return SpecialChar("⌠",1344)
def integral_bottom(): return SpecialChar("⌡",1322)