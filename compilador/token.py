

class Token:
    TK_IDENTIFIER  = 0
    TK_NUMBER      = 1
    TK_OPERATOR    = 2
    TK_OTHER       = 3
    TK_ASSIGN      = 4

    namesType = {
        0: 'TK_IDENTIFIER',
        1: 'TK_NUMBER',
        2: 'TK_OPERATOR',
        3: 'TK_OTHER',
        4: 'TK_ASSIGN'
    }

    def __init__(self) -> None:
        self.__type = None
        self.__nameType = None
        self.__lexema = None
        self.__line = None
        self.__column = None


    def __str__(self) -> str:
        
        return '%s[%04d, %04d] (%04d, %20s) (%s)' % (' '*14,self.__line,self.__column,self.__type, self.__nameType, self.__lexema)

    def getType(self) -> int:
        return self.__type

    def setType(self, type) -> None:
        self.__type = type
        self.__nameType = self.namesType[type]

    def getNameType(self) -> str:
        return self.__nameType

    def setNameType(self, text) -> None:
        self.__nameType = text

    def getLexema(self) -> str:
        return self.__lexema

    def setLexema(self, text) -> None:
        self.__lexema = text

    def getLine(self) -> str:
        return self.__line

    def setLine(self, text) -> None:
        self.__line = text

    def getColumn(self) -> str:
        return self.__column

    def setColumn(self, text) -> None:
        self.__column = text

    