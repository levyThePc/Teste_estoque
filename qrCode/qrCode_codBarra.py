from barcode import EAN13
from barcode.writer import ImageWriter
from time import sleep

#Programa para gerar codigo de barras
# codigo_barra = EAN13("100185589631", writer= ImageWriter())
# codigo_barra.save('Codigo_barra')

# codigo_produtos  = {
#     "Arroz": "123456789000",
#     "Feijao": "123455558888",
#     "Macarrão": "123456789000"
# }

# for produtos in codigo_produtos:
#     codigo = codigo_produtos[produtos]
#     codigo_barra = EAN13(codigo, writer= ImageWriter())
#     codigo_barra.save(f'Codigo_barra_{produtos}')


import qrcode

#img_qrCode = qrcode.make("https://www.instagram.com/levy_aofficial/")
#img_qrCode.save("Instagram_qr.png")


while True:
    qr_code =input('Seu codigo aqui(\33[32m link,Url,etc....\33[0m ): ')
    nome = input('Nome do arquivo: ')
    img_qrCode = qrcode.make(f'{qr_code}')
    img_qrCode.save(f"{nome}.png")
    res =' '
    while res not in 'SN':
        res = str(input('Deseja adcionar mais algum? [S/N]')).strip().upper()[0]
    if res =='N':
        break


input()






