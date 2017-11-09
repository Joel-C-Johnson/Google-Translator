from google.cloud import translate
from xlrd import open_workbook
import pyexcel
import ast
import json

    tc = translate.Client()
    tokenwords = open_workbook('output.xlsx')
    book = tokenwords
    p = book.sheet_by_index(0)
    count = 0
    for c in range(p.nrows):
        cell = p.cell(c, 0).value
        if cell:
            count = count + 1
    if count > 1:
        array = []
        result = [['WORDS', 'TRANSLATION']]
        for token_c in p.col(0, 1):
            array.append(token_c.value)
        for words in array:
             translation = tc.translate(words, source_language="en", target_language="ml")
             p = translation['translatedText']
             result.append([words,p])
        sheet = pyexcel.Sheet(result)
        output = flask.make_response(sheet.xlsx)
        output.headers["Content-Disposition"] = "attachment; filename = sss.xlsx"
        output.headers["Content-type"] = "xlsx"
        return output
