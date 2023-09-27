from fpdf import FPDF

pdf = None

# FPDF Functions
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



# Custom Functions

def split_into_lines(words:list, width:int) -> list:
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
    global pdf

    c_x = get_x()

    lines = split_into_lines(split_text_whitespace_right(text),width)

    for line in lines:
        line_text = "".join(line)
        write_text(get_x(),get_y(),line_text) # write line
        set_x(c_x)
        add_y(line_height)



def textblock_right_aligned(width:int, line_height:int, text:str):
    global pdf
    
    c_x = get_x() + width
    add_x(width)

    lines = split_into_lines(split_text_whitespace_left(text),width)

    for line in lines:
        line_text = "".join(line)
        line_width = get_string_width(line_text)

        add_x(-line_width)
        write_text(line_text) # write line
        set_x(c_x)
        add_y(line_height)


def textblock_center_aligned(width:int, line_height:int, text:str):
    global pdf

    c_x = get_x() + width/2
    set_x(c_x)

    lines = split_into_lines(split_text_whitespace_right(text),width)

    for line in lines:
        line_text = "".join(line)
        line_width = get_string_width(line_text)

        add_x(-line_width/2)
        write_text(line_text) # write line
        set_x(c_x)
        add_y(line_height)

    pass

def textblock_block_aligned(width:int, line_height:int, text:str):
    global pdf

    c_x = get_x()

    words = list(map(lambda x: x + " ",split_text_no_whitespace(text))) #add a space after every word, so that every word is at least seperated by one space width
    lines = split_into_lines(words,width)

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




# General Helpers
def to_point(a:float) -> float:
    """converts a value in mm to point"""
    return 1/0.35 * a

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