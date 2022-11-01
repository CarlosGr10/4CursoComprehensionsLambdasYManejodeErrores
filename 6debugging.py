def divisors(num):
    divs = []
    for i in range(1, num + 1):
        if num % i == 0:
            divs.append(i)
        return divs

def run():
    try:
        inter = int(input("Agrega un numero: "))
        print(divisors(inter))
        print(".: TERMINO EL PROGRAMA :.")
    except ValueError:
        print("Ingresar un número por favor")


if __name__ == '__main__':
    run()