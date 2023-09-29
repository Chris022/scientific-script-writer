"""This file holds functions for typeseting math formuals"""

from pdf import *
from helpers import *
from specialchars import *

class Term:

    def __init__(self,render,relative_height,relative_width) -> None:
        self.render = render
        self.relative_width = relative_width
        self.relative_height = relative_height # relative_height * font_size = actual height

    def get_abs_height(self):
        return to_abs_height(self.relative_height)
    
    
def combine_vertical(components:list,height:int):
    """This function takes seperate pices that in sum prodruce a symbol. This symbol can then be scaled vertically!"""
    h = 0
    for component,repeat in components:
        for i in range(0,int(height) if repeat else 1):
            h += component.get_height()
    add_y(-h/2)
    for component,repeat in components:
        for i in range(0,int(height) if repeat else 1):
            add_y(component.get_height())
            component.render()
    add_y(-h/2)
    add_x(get_string_width(components[-1][0].char))

def math_brackets(left:str,middle:Term,right:str) -> Term:
    if(middle.relative_height < 1.1): height = 0
    else: height = middle.relative_height
    def render():
        if(height == 0): 
            add_y(get_font_size()/2)
            write_text_line(left)
            add_y(-get_font_size()/2)
        else: math_bracket(left,round((middle.relative_height-3)/1))
        middle.render()
        if(height == 0):
            add_y(get_font_size()/2)
            write_text_line(right)
            add_y(-get_font_size()/2)
        else: math_bracket(right,round((middle.relative_height-3)/1))

    return Term(render,4.5+height,get_string_width(left)+get_string_width(right)/get_font_size() + middle.relative_width)


def math_bracket(el:str,height:int) -> None:
    if(el == "("):   combine_vertical([(left_bracket_top(),False),(left_bracket_middle(),True),(left_bracket_bottom(),False)],height)
    elif(el == ")"): combine_vertical([(right_bracket_top(),False),(right_bracket_middle(),True),(right_bracket_bottom(),False)],height)
    elif(el == "["): combine_vertical([(left_square_top(),False),(left_square_middle(),True),(left_square_bottom(),False)],height)
    elif(el == "]"): combine_vertical([(right_square_top(),False),(right_square_middle(),True),(right_square_bottom(),False)],height)
    elif(el == "{"): combine_vertical([(left_curly_top(),False),(left_curly_middle1(),True),(left_curly_middle2(),False),(left_curly_middle1(),True),(left_curly_bottom(),False)],height)
    elif(el == "}"): combine_vertical([(right_curly_top(),False),(right_curly_middle1(),True),(right_curly_middle2(),False),(right_curly_middle1(),True),(right_curly_bottom(),False)],height)
    

def math_frac(a:Term,b:Term) -> Term:
    minimize_factor = 0.8
    def render():
        width = max(a.relative_width,b.relative_width)*get_font_size()*1.2
        normal_font = get_font_size()
        minimized_font = get_font_size()*minimize_factor

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

    return Term(render,max(a.relative_height,b.relative_height)*2*(get_font_size()*minimize_factor)/get_font_size()+0.25,max(a.relative_width,b.relative_width)*1.2)


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