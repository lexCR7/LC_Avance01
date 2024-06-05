from scanner import Scanner
def main():
    cadena = input("Ingrese la cadena: ")
    s = Scanner(cadena) # Leer cadena
    tokens = s.scanAll()
    print(tokens)

if __name__ == '__main__':
    main()