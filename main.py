from scanner import Scanner
def main():
    
    s = Scanner(cadena) # Leer cadena
    tokens = s.scanAll()
    print(tokens)

if __name__ == '__main__':
    main()
