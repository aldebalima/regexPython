# http://docs.python.org/3/library/re.html

# Este módulo fornece operação que coincidem com expressões regulares 
# semelhantes as encontradas em Perl.
# Padrões para checagem

# Biblioteca padrão e referência

import re

strings = ''' Both patterns and strings to be searched can be Unicode strings (str)' 
           as well as 8-bit strings (bytes). However, unicode strings and 8-bit strings' 
           cannot be mixed: that is, you cannot match a unicode string with a byte pattern' 
           or vice-versa; similarly, when asking for a substitution, the replacement string' 
           must be of the same type as both the pattern and the search string. '''
print('Esse é o texto principal:'+ strings)
# re.search - Busca baseada expressão regular a primeira ocorrncia
print('-----------------------------------')
print('re.search')
print(re.search(r'byte', strings))
print(re.search(r'8-', strings))

# re.findall - Busca todas as ocorrências baseada em expressão regular
print('-----------------------------------')
print('re.findall')
print(re.findall(r'byte', strings))
print(re.findall(r'8-', strings))
# re.sub - Busca todas as ocorrências e substitui os valores baseadas em expressão regular
print('-----------------------------------')
print('re.sub de 8- para 18-')
print(re.sub(r'8-',r'18-', strings))
# re.compile - Compila expressão regular caso ela seja utilizda mais de uma vez, 
# questão de otimização.
regexcompile = re.compile(r'byte')
# re.search - Busca baseada expressão regular a primeira ocorrncia
print('-----------------------------------')
print('re.search + compile')
print(regexcompile.search(strings))
# re.findall - Busca todas as ocorrências baseada em expressão regular
print('-----------------------------------')
print('re.findall + compile')
print(regexcompile.findall(strings))
# re.sub - Busca todas as ocorrências e substitui os valores baseadas em expressão regular
print('-----------------------------------')
print('re.sub + compile')
print(regexcompile.sub('BYTE',strings))
# Meta caracteres
# | -> ou
print('-----------------------------------')
print('Metacaracteres')

print('Ou -> |')
print(re.findall(r'byte|type|bit|unicode|Unicode', strings))
# . -> qualquer caracter com exceção de quebra de linha
print('Qualquer caracter -> .')
print(re.findall(r'.yt.', strings))
# [] -> conjunto de caracteres ou ranges [a-zA-Z0-9]
print('Range de caracteres -> [a-zA-Z0-9]')
print(re.findall(r'[Uu]nicode', strings))
# flags
print('Flags re.IGUINORECASE considera independente do case sensitive')
print(re.findall(r'unicode', strings, flags=re.IGNORECASE))


#-------------------------------------------------------------------
#QUANTIFICADORES
text ='''
Lorem ipsum dolor sit aet ammmmmmet, consectetur diiiiipisccccing elit. Cras at velit finibus, tempus eros vel, pharetra sem. Proin ac odio in urna ornare condimentum. Phasellus bibendum a sem porta condimentum. Nunc ex dolor, tincidunt id neque a, pellentesque vehicula est. Aliquam erat volutpat. Donec maximus nulla id erat consequat pellentesque. Nam orci ex, sagittis a metus sollicitudin, luctus faucibus lorem. Ut molestie sapien in purus placerat volutpat. Aenean facilisis justo at orci laoreet, nec lobortis mauris suscipit. Aenean feugiat, orci aliquet laoreet ultrices, erat libero sodales sapien, quis tristique lectus mi a felis. Aliquam sit amet fermentum leo. Donec a maximus nisl, ut porta purus. Nam vel congue felis, at sollicitudin quam. Sed vel turpis sit amet augue suscipit elementum nec eu est. Donec faucibus malesuada justo. Vivamus a ullamcorper magna.
'''
print('Esse será o novo texto:' +text)
print('Quantificadores')
print('* -> 0 OU N')
# * -> 0 OU N
print(re.findall(r'am*et', text))
print(re.findall(r'di*pisc*ing', text))
print('+ -> 0 OU N')
# + -> 1 OU N
print(re.findall(r'am+et', text))
print('? -> 0 OU 1')
# ? -> 0 OU 1
print(re.findall(r'am?et', text))
print('{N,M} -> DE N ATÉ M')
# {N,M} -> DE N ATÉ M
print(re.findall(r'am{0,6}et', text))
# {N} -> N VZS
print('{N} -> N VZS')
print(re.findall(r'am{1}et', text))
