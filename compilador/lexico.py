from symbols import Symbols

class Lexico:
    symbols_lex = Symbols()
    def __init__(self, filename) -> None:
        self.__content = ''
        self.__fileLines = self.readFile(filename)
        self.__state = 0
        self.__position = 0
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
            for column, character in enumerate(content):
                self.__column = column
                self.__match(character)

    def __match(self, current: str) -> None:
        match self.__state:
            case 0:
                if self.symbols_lex.isChar(current):
                    self.__state = 0
                elif self.symbols_lex.isNumber(current):
                    self.__state = 0
                elif self.symbols_lex.isOperator(current):
                    self.__state = 0
                elif self.symbols_lex.other(current):
                    self.__state = 0
                elif current == '"':
                    self.__state = 0
                else:
                    if not self.symbols_lex.ignore(current):
                        print('Error',current,self.__line, self.__column)

            

lexical = Lexico("file.txt")
lexical.readLines()

