#!/usr/bin/python
# -*- coding: shift-jis -*-

import cgi


form = cgi.FieldStorage()

num = []
num.append(form.getfirst('a1'))
num.append(form.getfirst('b1'))
num.append(form.getfirst('c1'))
num.append(form.getfirst('a2'))
num.append(form.getfirst('b2'))
num.append(form.getfirst('c2'))
num.append(form.getfirst('a3'))
num.append(form.getfirst('b3'))
num.append(form.getfirst('c3'))
num.append(form.getfirst('d1'))
num.append(form.getfirst('e1'))
num.append(form.getfirst('f1'))
num.append(form.getfirst('d2'))
num.append(form.getfirst('e2'))
num.append(form.getfirst('f2'))
num.append(form.getfirst('d3'))
num.append(form.getfirst('e3'))
num.append(form.getfirst('f3'))

ope = form.getfirst('ope')

ans = []
if ope == 'plus':
    for times in range(9):
        ans.append(int(num[times]) + int(num[times + 9]))
else:
    for times in range(9):
        row = int(times / 3)
        row *= 3
        column = int(times % 3)
        ans.append(int(num[row]) * int(num[column + 9])\
                   + int(num[row + 1]) * int(num[column + 3 + 9])\
                   + int(num[row + 2]) * int(num[column + 6 + 9]))

print("Content-Type: text/html")
print()
html_text = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="shift-jis">
    <title>情報通信システム</title>
</head>
<body>
<p>{}</p>
<p>{}</p>
<p>{}</p>
</body>
</html>
'''
print(html_text.format(ans[0:3], ans[3:6], ans[6:9]))
