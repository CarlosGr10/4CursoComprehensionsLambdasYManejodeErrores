"""Ejercicio de un palindromo"""

def word(string):
    return string == string[::-1]   

palindrome = lambda string:string == string[::-1]

print(palindrome('ana'))

print(word('pato'))