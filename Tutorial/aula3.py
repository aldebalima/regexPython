# http://docs.python.org/3/library/re.html

# Este módulo fornece operação que coincidem com expressões regulares 
# semelhantes as encontradas em Perl.
# Padrões para checagem que começam com algo e terminam com algo

# Biblioteca padrão e referência

import re

strings = '''059.121.258-74'''
strings2 = '''a059.121.258-74'''
strings3 = '''059.121.258-74b'''
strings4 = '''a059.121.258-74b'''

print('Esse é o texto principal:'+ strings)
print('Validando campos com regex')
print('Sempre encontra independente da posição')
print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', strings))
print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', strings2))
print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', strings3))
print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', strings4))
print('Deve iniciar com as condicionantes')
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', strings))
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', strings2))
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', strings3))
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', strings4))
print('Deve iniciar e terminar com as condicionantes')
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', strings))
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', strings2))
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', strings3))
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', strings4))
print('Negação ^')
print(re.findall(r'[^0-9]+', strings4))




