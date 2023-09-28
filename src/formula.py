"""This file holds functions for typeseting math formuals"""

from pdf import *
from helpers import *

class Term:

    render = None
    relative_height = 1 # relative_height * font_size = actual height

    def __init__(self,render,relative_height) -> None:
        self.render = render
        self.relative_height = relative_height

def frac(a:Term,b:Term) -> Term:
    def render():
        height = (a.relative_height + b.relative_height + 0.5) * get_font_size()

    return Term(render,2.5)


def math_multi(a:Term,b:Term) -> Term:
    def render():
        a.render()

        add_y(1*get_font_size()/2)

        add_x(get_font_size()/10) #add spcae
        write_text_line("⋅")
        add_x(get_font_size()/10) #add spcae

        add_y(-1*get_font_size()/2)

        b.render()
    return Term(render,1)
    

def math_value(a:str) -> Term:
    def render():
        add_y(1*get_font_size()/2)
        write_text_line(a)
        add_y(-1*get_font_size()/2)
    return Term(render,1)