# Generator expression, Iterables e Iterators em Python
import sys

iterable = ['Eu','tenho','um','__iter__']
iterator = iter(iterable)
lista = [n for n in range(100000)]
generator = (n for n in range(100000))

'''
Em listas como o Generator não podemos acessar o len (quantidade de caracteres)
nem algum caractere da lista e nem nada q esteja na lista, já q o generator não está na memória
'''

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))
print(next(generator))
print(next(generator))

