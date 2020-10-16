#!/usr/bin/python
# -*- coding: utf-8 -*-

import cgi
from datetime import datetime

# form = cgi.FieldStorage()

print("Content-Type: text/html")
print()
html_text = '''
<!DOCTYPE html>
<html>
    <head><meta charset="shift-jis" /></head>
<body>
    <p>JPN: %s<br/></p>
</body>
</html>
''' % datetime.now()
print(html_text.encode("cp932", 'ignore').decode('cp932'))