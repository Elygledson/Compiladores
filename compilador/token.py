

class Token:
    TK_IDENTIFIER  = 0
    TK_NUMBER      = 1
    TK_OPERATOR    = 2
    TK_PONCTUATION = 3
    TK_ASSIGN      = 4
    __type = None
    __text = None

    def __str__(self) -> str:
        return f'Token [Type: {self.__type}, Text: {self.__text}]'

    def getType(self) -> int:
        return self.__type

    def setType(self, type) -> None:
        self.__type = type

    def getText(self) -> str:
        return self.__text

    def setText(self, text) -> None:
        self.__text = text

    
