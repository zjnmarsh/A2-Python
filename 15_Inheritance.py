class StockItem:
    def __init__(self,title,onloan,dateacquired):
        self._title = title
        self._onLoan = onloan
        self._dateAcquired = dateacquired

    def setloan(self,):
        pass

    def displaydetails(self):
        pass

class Books(StockItem):
    def __init(self,_title,_onLoan,_dateAcquired):
        super().__init__(_title,_onLoan,_dateAcquired)

class CD(StockItem):
    def __init(self,_title,_onLoan,_dateAcquired):
        super().__init__(_title,_onLoan,_dateAcquired)
