import qrcode
qr = qrcode.QRCode()

while True:
    data = input('Enter the link to be converted, or 0 to exit: ')
    if data == '0':
        break
    else:
        filename = input('Enter the filename (no need to include file extension): ')
        print('\n')
        filename = filename + ".png"
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(filename)
print('Otsukare')