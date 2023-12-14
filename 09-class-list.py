"""
    CLASS-09 For tsikli

"""
#1-mashq
#Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, 
#ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
ismlar = ['Anvar', 'Akbar', 'Munisbek', 'Jasurbek', 'Muzaffar', 'Hosilbek']
for ism in ismlar:
    print(f"{ism} tabriklayman siz talabalikka tavsiya etildingiz \n")

#2-mashq
#Yuqoridagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring 
#(n o'rniga kod necha marta takrorlanganini yozing)
for ism in ismlar:
    print(f"{ism} tabriklayman siz talabalikka tavsiya etildingiz \n")
print('Kod', len(ismlar), 'marta takrorlandi')

#3-mashq
#10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. 
#Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
t_sonlar = list(range(11, 100,2))
for kub in t_sonlar:
    print(f"{kub} ning kubi {kub**3} ga teng")

#4-mashq
#Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang,
#va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
kinolar = []
print('Sevimli kinoyingiz nomini kiriting:')
for n in range(5):
    kinolar.append(input(f"{n+1} sevimli kinoyingiz nomini kiriting: "))
print('Siz yotirgan kinolar: ', kinolar)

#5-mashq
#Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang,
#va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing.
#Ro'yxatni konsolga chiqaring.
suhbatlashganlar = []
n = int(input('Bugun nechta odam bilan suhbatlashdingiz?'))
for n in range(n):
    suhbatlashganlar.append(input(f"{n+1}-subhat qilgan odamingiz kim edi?"))
print(f"Siz bugun {suhbatlashganlar} lar bilan suhbatlashgansiz.")

    