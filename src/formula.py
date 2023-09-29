"""This file holds functions for typeseting math formuals"""

from pdf import *
from helpers import *

class Term:

    def __init__(self,render,relative_height,relative_width) -> None:
        self.render = render
        self.relative_width = relative_width
        self.relative_height = relative_height # relative_height * font_size = actual height

    def get_abs_height(self):
        return to_abs_height(self.relative_height)

def frac(a:Term,b:Term) -> Term:
    minimize_factor = 3
    def render():
        width = max(a.relative_width,b.relative_width)*get_font_size()
        normal_font = get_font_size()
        minimized_font = get_font_size()-minimize_factor

        #draw line
        horizontal_line(width)
        add_x(-width)
        add_y(-0.125*get_font_size())
        
        set_font_size(minimized_font)
        add_y(-a.get_abs_height()/2)
        add_x((width-a.relative_width*get_font_size())/2)
        a.render()
        add_x(-(width+a.relative_width*get_font_size())/2)
        add_y(a.get_abs_height()/2)
        set_font_size(normal_font)

        add_y(0.25*get_font_size())

        set_font_size(minimized_font)
        add_y(b.get_abs_height()/2)
        add_x((width-b.relative_width*get_font_size())/2)
        b.render()
        add_x(-width/2-b.relative_width*get_font_size()/2)
        add_y(-b.get_abs_height()/2)
        set_font_size(normal_font)


        add_y(-0.125*get_font_size())
        add_x(width)

    return Term(render,a.relative_height*(get_font_size()-minimize_factor)/get_font_size()+b.relative_height*(get_font_size()-minimize_factor)/get_font_size()+0.25,max(a.relative_width,b.relative_width))


def math_binary_op(a:Term,b:Term,op:str) -> Term:
    def render():
        a.render()

        add_y(get_font_size()/2)

        add_x(get_font_size()/10) #add spcae
        write_text_line(op)
        add_x(get_font_size()/10) #add spcae

        add_y(-get_font_size()/2)

        b.render()
    return Term(render,1,a.relative_width + get_string_width(op)/get_font_size() + b.relative_width)

def math_value(a:str) -> Term:
    def render():
        add_y(1*get_font_size()/2)
        write_text_line(a)
        add_y(-1*get_font_size()/2)
    return Term(render,1,get_string_width(a)/get_font_size())