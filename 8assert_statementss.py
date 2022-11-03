def divisors(num):
    divs = []
    for i in range(1, num + 1):
        if num % i == 0:
            divs.append(i)
        return divs

def run():
    try:
        inter = input("Agrega un numero: ")
        assert inter.isnumeric(), "Debes de ingresar un numero"
        print(divisors(int(inter)))
        print(".: TERMINO EL PROGRAMA :.")
    except ValueError:
        print("Ingresar un número por favor")


if __name__ == '__main__':
    run()