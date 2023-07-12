from googletrans import Translator
tarjimon = Translator()

matn_uz = "Boyka - haytidan zerikkan mushuk"

tarjima = tarjimon.translate(matn_uz)

# print(tarjima.origin)
# print(tarjima.text)
# print(tarjima.src)

tarjima_ru = tarjimon.translate(matn_uz, dest='ru')
# print(tarjima_ru.text)

matn_en = "Boyka is the most dangerous cat in the world"
tarjima_uz = tarjimon.translate(matn_en, dest='uz')