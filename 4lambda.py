"""Ejercicio de un palindromo"""

def word(string):
    return string == string[::-1]   

palindrome = lambda string:string == string[::-1]

print(palindrome('ana'))

print(word('pato'))


# Eleva al cuadrado un numero
square = lambda x: x**2
print(square(5))

# Manejo de cadenas
upper_chain = lambda stri: stri.upper()[::-1]
print(upper_chain('socat'))

# Manejar lambdas en un dicconario
def run(operation,num1,num2):
    OP = {
        'su':lambda a,b: a + b,
        're':lambda a,b: a - b,
        'mu':lambda a,b: a * b,
        'di':lambda a,b: a / b,
    }

    return OP[operation](num1,num2)

if __name__ == '__main__':
    print(run('su',1,2))



