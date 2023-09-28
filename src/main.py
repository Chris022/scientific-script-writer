from pdf import *
from textblock import *
from formula import *

new_document((400,50))
add_font("latinmodern-math") #add math formular
new_page()



set_font("latinmodern-math","",10)
set_cursor(0,8)
#textblock_center_aligned(100,10,"hallo ich bin der beste mensch der welt nicht. Da muss mann auch mal ehrlich sein!")
a = math_value("abc")
b = math_value("1")

math_multi(a,b).render()

export()
