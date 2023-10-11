"""This file contains Functions for creating textblocks"""
"""This file is messy. Try not to use it!"""
from pdf import *
from helpers import *


def __split_into_lines(words:list, width:int) -> list:
    """Takes a list of words and the width of a line and splits the word list into a list of lines of words"""
    lines = []

    line = []
    line_width = 0
    for word in words:
        word_width = get_string_width(word)

        if word_width > width:
            print("TEXT ERROR: word width is bigger than width of textblock")
            continue

        if(line_width + word_width > width):
            lines.append(line)
            line = []
            line_width = 0

        line.append(word)
        line_width += word_width
    lines.append(line) #add last line
    return lines

def textblock_left_aligned(width:int, line_height:int, text:str):
    """Writes left aligned text to the pdf"""
    c_x = get_x()

    lines = __split_into_lines(split_text_whitespace_right(text),width)

    for line in lines:
        line_text = "".join(line)
        write_text(get_x(),get_y(),line_text) # write line
        set_x(c_x)
        add_y(line_height)



def textblock_right_aligned(width:int, line_height:int, text:str):
    """Writes right aligned text to the pdf"""
    c_x = get_x() + width
    add_x(width)

    lines = __split_into_lines(split_text_whitespace_left(text),width)

    for line in lines:
        line_text = "".join(line)
        line_width = get_string_width(line_text)

        add_x(-line_width)
        write_text(line_text) # write line
        set_x(c_x)
        add_y(line_height)


def textblock_center_aligned(width:int, line_height:int, text:str):
    """Writes center aligned text to the pdf"""
    c_x = get_x() + width/2
    set_x(c_x)

    lines = __split_into_lines(split_text_whitespace_right(text),width)

    for line in lines:
        line_text = "".join(line)
        line_width = get_string_width(line_text)

        add_x(-line_width/2)
        write_text(line_text) # write line
        set_x(c_x)
        add_y(line_height)

    pass

def textblock_block_aligned(width:int, line_height:int, text:str):
    """Writes block aligned text to the pdf"""
    c_x = get_x()

    words = list(map(lambda x: x + " ",split_text_no_whitespace(text))) #add a space after every word, so that every word is at least seperated by one space width
    lines = __split_into_lines(words,width)

    for line in lines[:-1]:
        text_width = sum(map(lambda word: get_string_width(word), line))
        empty_space = width - text_width
        empty_space_per_word = empty_space/(len(line)-1)

        for word in line:
            word_width = get_string_width(word)
            write_text(word)
            add_x(word_width+empty_space_per_word)
        
        set_x(c_x)
        add_y(line_height)

    #deal with last line
    write_text("".join(lines[-1]))

