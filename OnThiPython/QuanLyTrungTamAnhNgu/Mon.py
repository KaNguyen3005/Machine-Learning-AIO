class Mon:
    def __init__(self, maMon, tenMon, soTiet):
        self.__maMon = maMon
        self.__tenMon = tenMon
        self.__soTiet = soTiet

    def getMaMon(self):
        return self.__maMon
    def getTenMon(self):
        return self.__tenMon
    def getSoTiet(self):
        return self.__soTiet

    def setMaMon(self, maMon):
        self.__maMon = maMon
    def setTenMon(self, tenMon):
        self.__tenMon = tenMon
    def setSoTiet(self, soTiet):
        self.__soTiet = soTiet

    def nhap(self):
        maMon = input('Ma mon: ')
        tenMon = input('Ten mon: ')
        soTiet = int(input('So Tiet: '))
        self.maMon = maMon
        self.tenMon = tenMon
        self.soTiet = soTiet

    def __str__(self):
        return f'Ma mon: {self.maMon}, Ten: {self.tenMon}, So tiet: {self.soTiet}'
