# http://docs.python.org/3/library/re.html

# Este módulo fornece operação que coincidem com expressões regulares 
# semelhantes as encontradas em Perl.
# Padrões para checagem Greed e non-greedy (lazy) grupos e retrovisores

# Biblioteca padrão e referência

import re

strings = ''' <p> Aleatório 1</p><p> Aleatório 2</p><p> Aleatório 3</p><div> Aleatório 4</div><p></p>'''
print('Esse é o texto principal:'+ strings)
print('O comportamento greed função de parada de leitura não ocorre no momento desejado, capturando todo o texto')

print(re.findall(r'<[divp]{1,3}>.*<\/[divp]{1,3}>', strings))
print(re.findall(r'<[divp]{1,3}>.+<\/[divp]{1,3}>', strings))

print('O comportamento NON greed parada é na primeira referência encontrada para o grupo de repetição')

print(re.findall(r'<[divp]{1,3}>.*?<\/[divp]{1,3}>', strings))
print(re.findall(r'<[divp]{1,3}>.+?<\/[divp]{1,3}>', strings))

print('------------------------------------------')
print('Grupos e retrovisores')

print('Grupos são criados por parentesis () o ?: iguinora os valores internos do parentesses')
print(re.findall(r'<(.+?)>(.+?)<\/\1>', strings))
print('Para reorganizar utilizando nomes de preferência e não os retrovisores de posição no caso \1')
print(re.findall(r'<(?P<tag>.+?)>(.+?)<\/(?P=tag)>', strings))



