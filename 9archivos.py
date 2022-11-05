from ast import For
import numbers


def read():
    numbers = []
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

# El atributo a es el metodo escritura sin sobrescritura (agrega)
# El atributo w es escritura y sobrescritura (Edita lo que hay dentro)
def write():
    names = ["CARLOS","PAPO"]
    with open("./archivos/names.txt", "a", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")


def run():
    write()




if __name__ == '__main__':
    run()