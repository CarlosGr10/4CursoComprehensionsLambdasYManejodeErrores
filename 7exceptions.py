from email.policy import strict


def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError("No se puede ingresar una cadena vacia")
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False


try:
    print(palindrome(""))
except TypeError:
    print("Solo aceptamos cadenas")


# Con assert staments 

def otherPalindrome(the_string):
    assert len(the_string) == "", "No se puede hacer una cadena vacia"
    return the_string == the_string[::-1]

print(otherPalindrome(""))