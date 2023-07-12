from googletrans import Translator
tarjimon = Translator()

while True:
    print("Matn kiriting (exit - q)")
    qiymat = input(">>>")
    if qiymat=='q':
        break
    else:
        tarjima = tarjimon.translate(qiymat, src='uz', dest='en')
        print(tarjima.text)