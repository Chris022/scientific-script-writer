"""This file holds helperfunctions that use the fpdf library"""
from fpdf import FPDF
from helpers import *

# TODO: convert to immutable
def set_font_size(pdf:FPDF,size: int) -> FPDF:
    """This function accepts a FPDF object and sets the fontsize of it"""
    pdf.set_font(family=pdf.font_family,size=to_point(size))
    return pdf


def get_string_rel_width(string:str):
    """This function returns the relative width of a string"""
    pdf = FPDF(orientation="p", unit="mm")

    pdf = set_font_size(pdf,10)
    rel_width = pdf.get_string_width(string)/10

    del pdf # cleanup

    return rel_width