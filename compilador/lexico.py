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
        current = self.__content[self.__position]
        while True:
            if not self.__isEOF():
                current = self.__content[self.__position]

            if self.__isEOF() and self.__state == 0: 
                break

            self.__match(current)
            self.__next()
            

    def __match(self, current: str) -> Token:
        match self.__state:
            case 0:
                if self.__isChar(current):
                    self.__state = 1
                elif self.__isNumber(current):
                    self.__state = 2
                elif self.__isOperator(current):
                    self.__state = 3
                elif self.__other(current):
                    self.__state = 4
            case 1:
                if not self.__isChar(current) and not self.__isNumber(current):
                    self.__createToken(Token.TK_IDENTIFIER)
            case 2:
                if not self.__isChar(current) and not self.__isNumber(current):
                    self.__createToken(Token.TK_NUMBER)
            case 3:
                if not self.__isOperator(current):
                    self.__createToken(Token.TK_OPERATOR)
            case 4:
                self.__createToken(Token.TK_OTHER)
            
    
    def __createToken(self, type):
        token = Token()
        token.setType(type)
        token.setText(''.join(self.__content[self.__nextpostion:self.__position]).strip())

        self.__nextpostion = self.__position
        self.__back()
        self.__state = 0
        print(token)

    def __next(self) -> str:
        self.__position += 1

    def __isEOF(self) -> bool:
        return self.__position == len(self.__content)

    def __isChar(self, c: str) -> bool:
        return (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z')

    def __isNumber(self, c: str) -> bool:
        return c >= '0' and c <= '9'

    def __isOperator(self, c: str) -> bool:
        return c == '>' or c == '<' or c == '=' or c == '!'

    def __ignore(self, c: str) -> bool:
        return c == '\t' or c == '\n' or c == ' ' or c == '\r'
    
    def __other(self, c: str) -> bool:
        return c == ';' or c =='(' or c == ')' or c == '{' or c == '}'
    
    def __back(self) -> None:
        self.__position -= 1


test = Lexico("file.txt")
test.getToken()