from tokens import Token, TokenType

class Scanner:
    def __init__(self,text):
        self.it = iter(text)
        self.curr = None  # Caracter actual
        self.advance()

    # Funcion que va pasando por todo el texto
    def advance(self):
        try:
            self.curr = next(self.it)
        except StopIteration:
            self.curr = None  #Una vez terminado el recorrido volvemos a colocar en null

    def scan(self):
        while self.curr is not None:
            # Ignorar espacios
            if self.curr in ('\n','\t',' '):
                self.advance()
            elif self.curr == '(':
                self.advance()
                return Token(TokenType.LPAREN, '(')
            elif self.curr == ')':
                self.advance()
                return Token(TokenType.RPAREN, ')')
            elif self.curr == 't':
                self.verify('true')
                return Token(TokenType.TRUE, 'true')
            elif self.curr == 'f':
                self.verify('false')
                return Token(TokenType.FALSE, 'false')
            elif self.curr == 'a':
                self.verify('and')
                return Token(TokenType.AND, 'and')
            elif self.curr == 'o':
                self.verify('or')
                return Token(TokenType.OR, 'or')
            elif self.curr == 'n':
                self.verify('not')
                return Token(TokenType.NOT, 'not')
            else:
                raise Exception('Caracter no reconocido')
        return None

    def scanAll(self):
        tokens = []
        while True:
            token = self.scan()
            if token is None:  # Si terminamos de leer toda la cadena
                break
            tokens.append(token)
        return tokens

    # Verificar que el caracter que en el que estamos no sea el simbolo final
    def verify(self, text):
        for c in text:
            if self.curr is None:
                raise Exception('Token no reconocido')
            if self.curr != c:
                raise Exception('Token no reconocido')
            self.advance()


