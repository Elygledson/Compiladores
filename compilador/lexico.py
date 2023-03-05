from symbols import Symbols

class Lexico:
    symbols_lex = Symbols()
    def __init__(self, filename) -> None:
        self.__content = ''
        self.__fileLines = self.readFile(filename)
        self.__state = 0
        self.__currentTokenPosition = 0
        self.__column = 0
        self.__line = 0


    def readFile(self, filename) -> None:
        lines = []
        try:
            with open(filename) as f:
                lines = [line for line in f.readlines()]
            f.close()
        except:
            print('Error')

        return lines
    

    def readLines(self):
        for line, content in enumerate(self.__fileLines):
            self.__line = line
            self.__content = content
            
            self.__column = 0
            self.__currentTokenPosition = 0
            while self.__column < len(self.__content):
                self.__match(self.__content[self.__column])

                if self.symbols_lex.ignore(self.__content[self.__column]):
                    self.__currentTokenPosition += 1

                self.__column += 1
        
        if self.__state != 0:
            self.createToken()


    def __match(self, current: str) -> None:
        match self.__state:
            case 0:
                if self.symbols_lex.isChar(current):
                    self.__state = 1
                elif self.symbols_lex.isNumber(current):
                    self.__state = 2
                elif self.symbols_lex.isOperator(current):
                    self.__state = 3
                elif self.symbols_lex.other(current):
                    self.__state = 4
                elif current == '"':
                    self.__state = 5
                else:
                    if not self.symbols_lex.ignore(current):
                        print('Error',current,self.__line, self.__column)

            case 1:
                if self.symbols_lex.isChar(current) or self.symbols_lex.isNumber(current):
                    self.__state = 1
                else:
                    self.createToken()
                    if not self.symbols_lex.ignore(current):
                        self.back()

            case 2:
                if self.symbols_lex.isNumber(current):
                    self.__state = 2
                else:
                    self.createToken()
                    if not self.symbols_lex.ignore(current):
                        self.back()

            case 3:
                if self.symbols_lex.isOperator(current):
                    self.__state = 3
                else:
                    self.createToken()
                    if not self.symbols_lex.ignore(current):
                        self.back()

            case 4:
                self.createToken()
                

    def createToken(self):
        print(self.__content[self.__currentTokenPosition: self.__column])

        self.__currentTokenPosition = self.__column
        self.__state = 0
    

    def back(self):
        self.__column -= 1


            

lexical = Lexico("file.txt")
lexical.readLines()

