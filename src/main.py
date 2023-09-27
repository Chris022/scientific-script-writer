from pdf import *
from textblock import *

new_document((400,50))
new_page()

set_font("Arial","B",10)
set_cursor(0,8)
textblock_center_aligned(100,10,"hallo ich bin der beste mensch der welt nicht. Da muss mann auch mal ehrlich sein!")

export()
