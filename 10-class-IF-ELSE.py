"""
    10-CLASS IF-ELSE operatori
    
"""

#1-mashq Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing,
# ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. 
# GM uchun ikkala harfni katta qiling.
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars: #mashinalar ichidagi har bitta mashinalar uchun
    if car == 'gm':print(car.upper()) # agar mashina gm ga teng bo'lsa katta harfda chiqsin
    else: print(car.title()) # aks xolda bosh harfi katta bo'lsin

#2-mashq  Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring. 
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars: #mashinalar ichidagi har bitta mashinalar uchun
    if car != 'gm':print(car.title()) # agar mashina gm ga teng bo'lsa katta harfda chiqsin
    else: print(car.upper()) # aks xolda bosh harfi katta bo'lsin

#3-mashq Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin.
#  Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. 
#  Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring.
login = input(f"Loginingizni kiriting: ")
if login.lower() == "admin":
    print(f"Xush kelibsiz, {login.title()}. Foydalanuvchilar ro'yhatini ko'rasizmi?")
else: print(f"Xush kelibsiz, {login.title()}! ")

#4-mashq Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa,
#  "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
x = float(input('Birinchi sonni kiriting: '))
y = float(input('Ikkinchi sonni kiriting: '))
if x == y:
    print('Sonlar teng') #sonlar teng bo'lsa "Sonlar teng" yozuvi konsoolga chiqadi

#5-mashq Foydalanuvchidan istalgan son kiritishni so'rang. 
# Agar son manfiy bo'lsa konsolga "Manfiy son", 
# agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.
x = float(input('Istalgan son kiriting: '))
if x > 0:
    print('Musbat son')
elif x < 0:
    print('Manfiy son')
else: print('Manfiy ham musbat ham emas!')

#6-mashq Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring.
#  Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring. 
x = float(input('Son kiriting: '))
if x >= 0:
    print(f"Kiritilgan sonning ildizi {x**(1/2)} ga teng.")
else: print('Musbat son kiriting')








