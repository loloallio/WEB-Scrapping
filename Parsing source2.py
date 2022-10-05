from openpyxl import Workbook
import re
import os


def cleaning(a, b):
    for it in b:
        a = a.replace(str(it), ' ')
    return a.strip()


def get_link(w):
    jk = []
    pattern = re.compile(r'https://www.[a-z]*.com/[/a-z-]*/[.a-z]*')
    match = pattern.findall(w)
    for ma in match:
        jk.append(ma)
    return jk


def get_date(op):
    pattern = re.compile(r'[0-9]*\s[A-Za-z]*\s[0-9]*')
    coincidence = pattern.findall(op)
    return coincidence[0]


def cleandescp(lis, worf):
    while worf in lis:
        lis = lis.replace(lis[lis.find('<'):lis.find('>') + 1], ' ')
    return lis


# delete list for cleaning the description
delete_list = ['<span style="color: #3f3f3f;">', '<p style="margin-bottom: 0in;">', '</span>', '</p>', '<p>',
               '<p style="margin-bottom: 0cm; text-align: justify;">', '<span style="color: #000000;">', '<span>',
               '<span style="color: black;">', '<p style="text-align: left;">', '<strong>', '</strong>',
               '<p style="margin-bottom: 0in; text-align: left;">', '<em>', '</em>',
               '<p style="margin-top: 0in; margin-bottom: 0in;">', '<p style="margin-bottom: 6pt;">', '</a>',
               '<p style="margin: 0in;">']

# open excel
wb = Workbook()
excel = "DLA Piper Press Releases.xlsx"

# open file source
file = open("source2.txt", "r", encoding="utf-8")

# worksheet
ws1 = wb.active
ws1.title = 'Press Releases'

counter = 1

# downloads news' link, tittle, description and date.
for i in file:
    # link and tittle
    if i.startswith('<a class="article-link unit__title-link"'):
        ws1["A" + str(counter)] = ("https://www.dlapiper.com" + i[i.find('/en/us'):i.find('/">') + 1])
        ws1["B" + str(counter)] = i[i.find('/">') + 3:-5]
    # description and link
    elif i.startswith('<div class="article-abstract" data-bind="html: Abstract">'):
        description = cleaning(i[i.find('Abstract">') + 10:-7], delete_list)
        ws1["C" + str(counter)] = cleandescp(description, 'href')
        if '<a href' in i:
            col = 5
            for i in get_link(i):
                ws1.cell(column=col, row=counter, value=i)
                col += 1
    # date
    elif i.startswith('<div class="meta__date"'):
        ws1["D" + str(counter)] = str(get_date(i))
        counter += 1

file.close()
wb.save(filename=excel)
os.remove("source2.txt")
