import re


def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False
    for i in lines:
        i = check_header(i)
        m = re.match(r'\* (.*)', i)
        if m:
            if not in_list:
                in_list = True
                curr = m.group(1)
                curr = check_bold(curr)
                curr = check_italic(curr)
                i = '<ul><li>' + curr + '</li>'
            else:
                is_bold = False
                is_italic = False
                curr = m.group(1)
                m1 = re.match('(.*)__(.*)__(.*)', curr)
                if m1:
                    is_bold = True
                m1 = re.match('(.*)_(.*)_(.*)', curr)
                if m1:
                    is_italic = True
                if is_bold:
                    curr = m1.group(1) + '<strong>' + \
                           m1.group(2) + '</strong>' + m1.group(3)
                if is_italic:
                    curr = m1.group(1) + '<em>' + m1.group(2) + \
                           '</em>' + m1.group(3)
                i = '<li>' + curr + '</li>'
        else:
            if in_list:
                in_list_append = True
                in_list = False

        m = re.match('<h|<ul|<p|<li', i)
        if not m:
            i = '<p>' + i + '</p>'
        i = check_bold(i)
        i = check_italic(i)
        if in_list_append:
            i = '</ul>' + i
            in_list_append = False
        res += i
    if in_list:
        res += '</ul>'
    return res


def check_header(i):
    count = 0
    for char in i:
        if char == '#':
            count += 1
        else:
            break
    return i if count == 0 else f'<h{count}>{i[count + 1:]}</h{count}>'


def check_italic(curr):
    m1 = re.match('(.*)_(.*)_(.*)', curr)
    if m1:
        curr = m1.group(1) + '<em>' + m1.group(2) + '</em>' + m1.group(3)
    return curr


def check_bold(curr):
    m1 = re.match('(.*)__(.*)__(.*)', curr)
    if m1:
        curr = m1.group(1) + '<strong>' + m1.group(2) + '</strong>' + m1.group(3)
    return curr
