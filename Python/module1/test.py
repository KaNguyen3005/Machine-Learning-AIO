def tax_bill(quangDuong, thoiGian):
    phiChoDoi = 20000*thoiGian

    if quangDuong < 1:
        return 9000 + quangDuong*11000 + phiChoDoi

    if quangDuong <= 30:
        return 11000*quangDuong + phiChoDoi

    return 30*11000 + (quangDuong - 30)*9500 + phiChoDoi

print(tax_bill(50,0))