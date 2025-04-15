#LUG'AT BILAN TANISHUV


otam = {'ism':'Dilshod','familiya':'Kasimbekov','tug_yili':1968,'shahri':'Toshkent'}
print(f"Otamning ismi {otam['ism']}, {otam['tug_yili']}-yilda {otam['shahri']} shaharda tavallud topganlar.")


taomlar = {'otam':'osh','onam':'shilpildoq','ukam':'manti','ayolim':'shashlik'}
print(f"Otamning sevimli taomlari {taomlar['otam']}.\n"
      f"Onamning sevimli taomlar {taomlar['onam']}.\n"
      f"Ukamning sevimli taomlari {taomlar['ukam']}.\n"
      f"Ayolimning sevimli taomi {taomlar['ayolim']}.\n")


atamalar = {'str':'matn shakl','int':'butun son','float':'kasr yoki manfiy son','if':'agarda','else':'yokida','or':'yoki'}


atamalar = {'str':'matn shakl','int':'butun son','float':'kasr yoki manfiy son','if':'agarda','else':'yokida','or':'yoki'}
kalit = input("Kalit so'zni kiriting: ").lower()
print(atamalar.get(kalit, "Bunday so'z mavjud emas."))


atamalar = {'str':'matn shakl','int':'butun son','float':'kasr yoki manfiy son','if':'agarda','else':'yokida','or':'yoki'}
kalit = input("Kalit so'zni kiriting: ").lower()
tarjima =atamalar.get(kalit)
if tarjima == None:
    print("Bunday atama mavjud emas.")
else:
    print(f"{kalit.title()} ning ma'nosi {tarjima} deyiladi.")