#! /usr/bin/env python

from random import randint
random_number = randint(1, 100)
print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head>')
print('<title>Hello Word - First CGI Program</title>')
print('</head>')
print('<body>')
print('<p>', random_number, '</p>')
print('<h2>Hello Word! This is my first CGI program</h2>')
print('</body>')
print('</html>')