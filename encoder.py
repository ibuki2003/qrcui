# -*- coding: utf-8 -*-
import qrcode
def make_qr(data):
    return qrcode.make(data)

def show_ascii_qr(data):
    img = qrcode.make(data)
    print('*')
