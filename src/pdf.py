"""This File contains functions that can be used to interact with the PDF document"""
from fpdf import FPDF
from helpers import *

pdf = None

def new_document(dim:tuple):
    """creates a new FPDF document with the given size"""
    global pdf
    pdf = FPDF(orientation="p", unit="mm", format=dim)

def new_page():
    global pdf
    pdf.add_page()

def set_font(family: str | None = None,style = "",size: int = 0):
    global pdf
    pdf.set_font(family=family,style=style,size=to_point(size))

def set_cursor(x:int,y:int):
    global pdf
    pdf.set_xy(x,y)

def set_x(x:float):
    global pdf
    pdf.set_x(x)

def set_y(y:float):
    global pdf
    c_x = pdf.get_x()
    pdf.set_y(y)
    pdf.set_x(c_x)

def get_x() -> float:
    global pdf
    return float(pdf.get_x())

def get_y() -> float:
    global pdf
    return float(pdf.get_y())

def add_x(dx:float):
    global pdf
    pdf.set_x(pdf.get_x() + dx)

def add_y(dy:float):
    global pdf
    c_x = pdf.get_x()
    pdf.set_y(pdf.get_y() + dy)
    pdf.set_x(c_x)

def get_string_width(word:str) -> float:
    global pdf
    return float(pdf.get_string_width(word))

def write_text(text:str) -> None:
    global pdf
    pdf.text(get_x(),get_y(),text)

def export():
    global pdf
    pdf.output("text.pdf","F")