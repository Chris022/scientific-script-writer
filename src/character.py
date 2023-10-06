"""
This file holds the Char datatype. A Char represents a single character. This file then offers some functions to get measurements of the char
"""
from dataclasses import dataclass

import helpers as helpers
import pdf_helpers as pdf_helpers

@dataclass(init=True, repr=True, eq=True, match_args=True)
class Char:
    """Wraper Class for a single char. Acts like a blueprint for generating PrintChars"""
    unicode: int
    char: str
    rel_height: float
    rel_width: float

def alphanum_char(char:str) -> Char:
    if(not char.isalnum()): raise Exception("Can only crate alphanumeric Char with 'alphanum_char' function!")
    return Char(
        unicode=ord(char),
        char=char,
        rel_height=1,
        rel_width=pdf_helpers.get_string_rel_width(char)
    )

def special_char(char:str, rel_height:float) -> Char:
    return Char(
        unicode=ord(char),
        char=char,
        rel_height=rel_height,
        rel_width=pdf_helpers.get_string_rel_width(char)
    )


@dataclass(init=True, repr=True, eq=True, match_args=True)
class AbsChar:
    """This represents a specific instance of a character (with absolute position and size)"""
    x_pos: float
    y_pos: float
    height: float
    width: float

def print_char(char: Char, font_size: float, x_pos: float, y_pos: float):
    return AbsChar(
        x_pos=x_pos,
        y_pos=y_pos,
        height=char.rel_height*font_size,
        width=char.rel_width*font_size
    )
