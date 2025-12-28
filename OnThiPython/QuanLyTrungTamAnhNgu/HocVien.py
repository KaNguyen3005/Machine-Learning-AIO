from Mon import *

class HocVien:
    def __init__(self, msv, tenSV, namSinh, dsMon = []):
        self.__msv = msv
        self.__tenSV = tenSV
        self.__namSinh = namSinh
        self.__dsMon = dsMon if dsMon is not None else []

    def getMSV(self):
        return self.__msv
    def getTenSV(self):
        return self.__tenSV
    def getNamSinh(self):
        return self.__namSinh
    def getDsMon(self):
        return self.__dsMon
    def setMSV(self, msv):
        self.__msv = msv
    def setTenSV(self, tenSV):
        self.__tenSV = tenSV
    def setNamSinh(self, namSinh):
        self.__namSinh = namSinh
    def setDsMon(self, dsMon):
        self.__dsMon = dsMon

    def xuat(self):
        print(self.__str__())

    def nhap(self):
        self.__msv = input('msv: ')
        self.__tenSV = input('tenSV: ')
        self.__namSinh = input('namSinh: ')
        soLuongMon = int(input('Nhap vao so luong mon muon dang ky: '))
        for i in range(soLuongMon):
            mon = Mon()
            mon.nhap()
            self.__dsMon.append(mon)


    def __str__(self):
        hocVienStr = f'ma sinh vien: {self.msv}, ten: {self.tenSV}, nam sinh: {self.namSinh}\n'
        for mon in self.dsMon:
            hocVienStr += '\t' + mon.__str__() + '\n'
        return hocVienStr