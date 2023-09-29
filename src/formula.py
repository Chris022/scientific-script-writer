"""This file holds functions for typeseting math formuals"""

from pdf import *
from helpers import *

class Term:

    def __init__(self,render,relative_height,width) -> None:
        self.render = render
        self.width = width
        self.relative_height = relative_height # relative_height * font_size = actual height

    def get_abs_height(self):
        return to_abs_height(self.relative_height)

def frac(a:Term,b:Term) -> Term:
    def render():
        width = max(a.width,b.width)

        #draw line
        horizontal_line(width)
        add_x(-width)
        add_y(-0.25*get_font_size())
        
        add_y(-a.get_abs_height()/2)
        add_x((width-a.width)/2)
        a.render()
        add_x(-width/2-a.width/2)
        add_y(a.get_abs_height()/2)

        add_y(0.5*get_font_size())

        add_y(b.get_abs_height()/2)

        add_x((width-b.width)/2)
        b.render()
        add_x(-width/2-b.width/2)
        add_y(-b.get_abs_height()/2)

        add_y(-0.25*get_font_size())
        add_x(width)

    return Term(render,a.relative_height+b.relative_height+0.5,max(a.width,b.width))


def math_multi(a:Term,b:Term) -> Term:
    def render():
        a.render()

        add_y(1*get_font_size()/2)

        add_x(get_font_size()/10) #add spcae
        write_text_line("⋅")
        add_x(get_font_size()/10) #add spcae

        add_y(-1*get_font_size()/2)

        b.render()
    return Term(render,1,a.width + get_font_size("⋅") + b.width)
    

def math_value(a:str) -> Term:
    def render():
        add_y(1*get_font_size()/2)
        write_text_line(a)
        add_y(-1*get_font_size()/2)
    return Term(render,1,get_string_width(a))