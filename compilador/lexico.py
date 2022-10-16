from calendar import c
from token import Token

class Lexico:

    def __init__(self, filename) -> None:
        self.__content = self.readFile(filename)
        self.__state = 0
        self.__position = 0
        self.__nextpostion = 0

    def readFile(self, filename) -> list:
        temp = []
        try:
            with open(filename) as f:
                temp = [character for line in f.readlines() for character in line]
            f.close()
        except:
            print('Error')

        return temp

    def getToken(self) -> Token:
        current = None
        while True:
            if self.__isEOF(): 
                self.__position += 1
                token = self.__match(current)
                print(token)
                break

            current = self.__next()
            token = self.__match(current)
            if token != None:
                print(token)

    def __match(self, current: str) -> Token:
        match self.__state:
            case 0:
                self.__nextpostion = self.__position-1

                if self.__isNumber(current):
                    self.__state = 3
                elif self.__isChar(current):
                    self.__state = 1
                elif self.__isOperator(current):
                    self.__state = 5
                else:
                    print("UNRECOGNIZED SYMBOL")
                return None
            case 1:
                if not self.__isChar(current) and not self.__isNumber(current) or self.__isEOF():
                    self.__state = 2
                else:
                    self.__state = 1
                return None
            case 2:
                return self.__createToken(Token.TK_IDENTIFIER)
            case 3:
                if self.__isChar(current):
                    print('ERROR', current, self.__content[self.__nextpostion:self.__position])
                
                if not self.__isChar(current) and not self.__isNumber(current):
                    self.__state = 4
            case 4:
                return self.__createToken(Token.TK_NUMBER)
    
    def __createToken(self, type):
        token = Token()
        token.setType(type)
        token.setText(self.__content[self.__nextpostion:self.__position])

        self.__state = 0
        return token

    def __next(self) -> str:
        self.__position += 1
        return self.__content[self.__position]

    def __isEOF(self) -> bool:
        return self.__position+1 == len(self.__content)

    def __isChar(self, c: str) -> bool:
        return (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z')

    def __isNumber(self, c: str) -> bool:
        return c >= '0' and c <= '9'

    def __isOperator(self, c: str) -> bool:
        return c == '>' or c == '<' or c == '=' or c == '!'

    def __ignore(self, c: str) -> bool:
        return c == '\t' or c == '\n' or c == ' ' or c == '\r'


test = Lexico("file.txt")
test.getToken()