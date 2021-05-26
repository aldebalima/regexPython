# http://docs.python.org/3/library/re.html

# Este módulo fornece operação que coincidem com expressões regulares semelhantes as encontradas em Perl.

import re

strings = ' Both patterns and strings to be searched can be Unicode strings (str)' \
          ' as well as 8-bit strings (bytes). However, unicode strings and 8-bit strings' \
          ' cannot be mixed: that is, you cannot match a unicode string with a byte pattern' \
          ' or vice-versa; similarly, when asking for a substitution, the replacement string' \
          ' must be of the same type as both the pattern and the search string. '
# re.compile - Compila expressão regular caso ela seja utilizda mais de uma vez, queestão de otimização.
regexcompile = re.compile(r'byte')
# re.search - Busca baseada expressão regular a primeira ocorrncia
print(regexcompile.search(strings))
# re.findall - Busca todas as ocorrências baseada em expressão regular
print(regexcompile.findall(strings))
# re.sub - Busca todas as ocorrências e substitui os valores baseadas em expressão regular
print(regexcompile.sub('BYTE',strings))

# Meta caracteres

# | -> ou
print(re.findall(r'byte|type|bit|unicode|Unicode', strings))
# . -> qualquer caracter com exceção de quebra de linha
print(re.findall(r'.yt.', strings))
# [] -> conjunto de caracteres ou ranges [a-zA-Z0-9]
print(re.findall(r'[U,u]nicode', strings))
# flags
print(re.findall(r'unicode', strings, flags=re.IGNORECASE))

#QUNTIFICADORES

# * -> 0 OU N

# + -> 1 OU N
# ? -> 0 OU 1
# {N,M} -> DE N ATÉ M
# {N} -> N VZS