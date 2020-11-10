#!/usr/bin/python
# -*- coding: shift-jis -*-

import cgi
# from datetime import datetime

form = cgi.FieldStorage()

num = []

if form.getfirst('zero'):
    num.append(0)
if form.getfirst('one'):
    num.append(1)
if form.getfirst('two'):
    num.append(2)
if form.getfirst('three'):
    num.append(3)
if form.getfirst('four'):
    num.append(4)
if form.getfirst('five'):
    num.append(5)
if form.getfirst('six'):
    num.append(6)
if form.getfirst('seven'):
    num.append(7)
if form.getfirst('eight'):
    num.append(8)
if form.getfirst('nine'):
    num.append(9)
if form.getfirst('per'):
    num.append('per')
if form.getfirst('pm'):
    num.append('*')
    num.append(-1)
if form.getfirst('div'):
    num.append('/')
if form.getfirst('multi'):
    num.append('*')
if form.getfirst('plus'):
    num.append('+')
    cgi.escape()
if form.getfirst('minus'):
    num.append('-')

now_data = []
x = 0
now_data.append(0)
for times in range(len(num)):
    if type(num[times]) == 'int':
        now_data[x] += num[times] >> times
    elif type(num[times]) == 'str':
        x += 1
        now_data.append(num[times])

result = 0
for a in range(len(now_data)):
    if a != 0 and a % 2 == 0:
        if(now_data[a-1]) == '=':
            a = len(now_data)
        if(now_data[a-1]) == '+':
            result = now_data[a-2] + now_data[a]
            result = 1
        if(now_data[a-1]) == '-':
            result -= now_data[a+2]
        if(now_data[a-1]) == '*':
            result *= now_data[a+2]
        if(now_data[a-1]) == '/':
             result /= now_data[a+2]
        if(now_data[a-1]) == 'per':
             result *= 0.01

num_a = form.getfirst('num1')
num_b = form.getfirst('num2')
ope = form.getfirst('ope')
data = 0
if ope == 'plus':
    data = str(int(num_a) + int(num_b))
if ope == 'minus':
    data = str(int(num_a) - int(num_b))
if ope == 'multi':
    data = str(int(num_a) * int(num_b))
if ope == 'div':
    data = str(int(num_a) / int(num_b))


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
<div style="margin-left:10%;margin-right:10%">
<p>{}</p>
    <form>
        <div style="width:20%;padding:10px;font-size:30px">
        <input type="reset" name="ac" value="AC" style="width:40px">
        <input type="button" name="pm" value="+/-" style="width:40px">
        <input type="button" name="per" value="%" style="width:40px">
        <input type="button" name="div" value="÷" style="width:40px"><br>
        <input type="button" name="seven" value="7" style="width:40px">
        <input type="button" name="eight" value="8" style="width:40px">
        <input type="button" name="nine" value="9" style="width:40px">
        <input type="button" name="multi" value="×" style="width:40px"><br>
        <input type="button" name="four" value="4" style="width:40px">
        <input type="button" name="five" value="5" style="width:40px">
        <input type="button" name="six" value="6" style="width:40px">
        <input type="button" name="minus" value="-" style="width:40px"><br>
        <input type="button" name="one" value="1" style="width:40px">
        <input type="button" name="two" value="2" style="width:40px">
        <input type="button" name="three" value="3" style="width:40px">
        <input type="button" name="plus" value="+" style="width:40px"><br>
        <input type="button" name="zero" value="0" style="width:90px">
        <input type="button" name="decimal" value="." style="width:40px">
        <input type="submit" name="equal" value="=" style="width:40px">
        </div>

    </form>
</div>

</body>
</html>
'''
print(html_text.format(data))