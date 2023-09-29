"""This file contains helper functions in general"""


def to_point(a:float) -> float:
    """converts a value in mm to point"""
    return a * 4.2

def split_text_whitespace_right(text:str) -> list:
    """takes a string and creates a list of words where the space always is appended at the end of a word."""
    words = []
    start = 0
    end = 0

    text = text.lstrip().rstrip() #remove leading and tailing whitespace

    last_letter_was_whitespace = False
    for letter in text:
        
        if letter == ' ':
            last_letter_was_whitespace = True
            end+=1
            continue

        if last_letter_was_whitespace:
            words.append(text[start:end])
            start = end
        
        last_letter_was_whitespace = False
        end+=1
    words.append(text[start:end]) #add last word
    return words

def split_text_whitespace_left(text:str) -> list:
    """takes a string and creates a list of words where the space always is appended at the start of a word."""
    words = split_text_whitespace_right(text[::-1])
    return list((map(lambda word: word[::-1],words)))[::-1]

def split_text_no_whitespace(text:str) -> list:
    """takes a string and creates a list of words without whitespaces."""
    words = split_text_whitespace_right(text)
    return list((map(lambda word: word.replace(" ",""),words)))