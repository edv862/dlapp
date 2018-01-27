# -*- coding: utf-8 -*-
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage, PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

from io import StringIO, BytesIO
import docx2txt
import io
import sys
import os


# Get text from pdf file
def pdf_2_string(filename):

    # open pdf file
    # scrape = open(filename, 'rb')

    scrape = filename
    pdfFiler = BytesIO(scrape.read())
    # Create a PDF resource manager object that stores shared resources.
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    # Set parameters for analysis.
    laparams = LAParams()
    # Set the converter
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    # Interprete
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    # Boilerplate
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()

    # Extract from file and add it in retstr
    # Make use of device and interpreter classes
    for page in PDFPage.get_pages(
        pdfFiler,
        pagenos,
        maxpages=maxpages,
        password=password,
        caching=caching,
        check_extractable=True
    ):
        interpreter.process_page(page)

    textstr = retstr.getvalue()
    device.close()
    retstr.close()
    return textstr


# Get text from docx file
def docx_2_string(filename):
    text = docx2txt.process(filename)
    return text


# Get text from txt file
def txt_2_string(filename):
    text = filename.read()
    return text


# Get file's extension
def get_extension(file):
    # basename = os.path.basename(filename)  # os independent
    ext = os.path.splitext(file)[-1].lower()
    return ext


# Line definition for lines
def is_lline(str):
    # Its necesary ignore some lines extracted from tables
    # The whitespaces, tabs and other useless characters
    # A line must has at least 30 characters
    if (len(str) >= 30):
        if ((str != "\n") and (str != " ") and (str != "\0") and (str != "")
         and (str != "\t")):
            return True
    return False


# Line definition for paragraphs
def is_line(str):
    # Its necesary ignore some lines extracted from tables
    # The whitespaces, tabs and other useless characters
    # A line must has at least 50 characterss
    if (len(str) >= 50):
        if ((str != "\n") and (str != " ") and (str != "\0") and (str != "")
         and (str != "\t")):
            return True
    return False


# short line definition for paragraphs
def is_sline(str):
    # Its necesary ignore some lines extracted from tables
    # The whitespaces, tabs and other useless characters
    # A line must has at least 30 characters
    if (len(str) >= 10):
        if ((str != "\n") and (str != " ") and (str != "\0") and (str != "")
         and (str != "\t")):
            return True
    return False


# Get a line in the string
# str: document converted
# nline: line to find
def get_line(str, nline):
    i = 1
    j = 1
    result = "Lines exceeded"

    for line in str.splitlines():
        if j == 17:
            print(line)
        j += 1
        if (is_lline(line)):
            if (i == nline):
                result = line
                break
            i += 1

    return result


# Get a paragraph in the string
# str: document converted
# nparag: paragraph to find
def get_paragraph(str, nparag):
    i = 1
    j = 1
    nlines = 0
    result = "Paragraphs exceeded"
    paragraph = ""

    for line in str.splitlines():
        if j == 17:
            print(line)
        j += 1
        
        if (is_line(line)):
            paragraph = paragraph + line
            nlines += 1
        else:
            # Here define, its a paragraph if has at least 2 lines in a row
            if (nlines >= 2):
                # This should be the last line, so it can smaller
                if (is_sline(line)):
                    paragraph = paragraph + line
                    nlines += 1

                if (i == nparag):
                    result = paragraph
                    break
                else:
                    i += 1
                    nlines = 0
                    paragraph = ""
            else:
                nlines = 0
                paragraph = ""
    return result


def extract(filename, opt, number):
    number = int(number)
    # Get file extension
    ext = get_extension(filename.name)

    text = ""

    choice = int(opt)

    if ext == ".pdf":
        text = pdf_2_string(filename)
    elif ext == ".txt":
        aux = txt_2_string(filename)
        text = aux.decode("utf-8")
    elif ext == ".docx":
        text = docx_2_string(filename)
    else:
        # Invalid extension.
        pass

    if (choice == 1):
        line_choice = get_line(text, number)
        return line_choice
    elif (choice == 2):
        paragraph = get_paragraph(text, number)
        return paragraph


# reader.py arg1
# arg1: file.*
# *: txt, pdf, docx
if __name__ == '__main__':
    # Take arguments
    args = []
    for arg in sys.argv[1:]:
        args.append(arg)

    # 1st argument is the file
    filename = args.pop(0)

    # 2nd argument is l or p
    opt = args.pop(0)

    # 3rd arguments its value
    number = int(args.pop(0))

    # Get file extension
    ext = get_extension(filename)

    text = ""

    if ext == ".pdf":
        text = pdf_2_string(filename)
    elif ext == ".txt":
        aux = txt_2_string(filename)
        text = aux.decode("utf-8")
    elif ext == ".docx":
        text = docx_2_string(filename)
    else:
        # Invalid extension.
        pass

    if (opt == 'l'):
        line_choice = get_line(text, number)
        print("Line: " + line_choice)
    elif (opt == 'p'):
        paragraph = get_paragraph(text, number)
        print("Paragraph: " + paragraph)
