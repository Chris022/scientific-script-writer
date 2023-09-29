from pdf import *
from textblock import *
from formula import *

new_document((400,100))
add_font("latinmodern-math") #add math formular
new_page()



set_font("latinmodern-math","",10)
set_cursor(100,50)
#textblock_center_aligned(100,10,"hallo ich bin der beste mensch der welt nicht. Da muss mann auch mal ehrlich sein!")

a = math_value("H")
b = math_value("1")
c = math_value("2")

bruch = frac(a,b)
#bruch.render()
bruch2 = frac(bruch,bruch)
bruch2.render()



export()
