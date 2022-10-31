def divisors(num):
    divs = []
    for i in range(1, num + 1):
        if num % i == 0:
            divs.append(i)
        return divs

def run():
    inter = int(input("Agrega un numero: "))
    print(divisors(inter))
    print(".: TERMINO EL PROGRAMA :.")


if __name__ == '__main__':
    run()