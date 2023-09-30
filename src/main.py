from pdf import *
from textblock import *
from formula import *


new_document((400,500))
add_font("latinmodern-math") #add math formular
new_page()



set_font("latinmodern-math","",10)

#textblock_center_aligned(100,10,"hallo ich bin der beste mensch der welt nicht. Da muss mann auch mal ehrlich sein!")
set_cursor(20,250)
bruch = math_frac(math_value("A"),math_value("A"))
mega_bruch = math_frac(math_frac(bruch,math_frac(bruch,bruch)),math_frac(bruch,math_frac(bruch,bruch)))
power = math_power(mega_bruch,mega_bruch)

math_brackets("(",power,")").render()

math_value("abc").render()


export()
