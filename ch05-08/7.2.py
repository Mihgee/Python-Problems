class Stock:

    def __init__(self, symbol, name, prev, current):
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = prev
        self.__currentPrice = current

    def getName(self):
        return self.__name

    def getSymbol(self):
        return self.__symbol

    def getPreviousPrice(self):
        return self.__previousClosingPrice

    def geCurrentPrice(self):
        return self.__currentPrice

        def setPreviousPrice(self, p):
            self.__previousClosingPrice = p

    def setCurrentPrice(self, p):
        self.__currentPrice = p

    def getChangePercent(self):
        return (self.__currentPrice - self.__previousClosingPrice) * 100.0 / (self.__previousClosingPrice)

s = Stock('INTC', 'Intel Corporation', 20.5, 20.35)

print("Price change percentage is=  "'%.2f%%' % s.getChangePercent())