"""
    CLASS 11 IF_ELIF 
"""
#1-mashq Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!",
#  agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring
son = float(input('Juft son kiriting! '))
if son%2:
    print('Bu son juft son emas!')
else: print('Rahmat')

#2-mashq Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
# Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
# Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
# Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
yosh = int(input('Yoshingizni kiriting: '))
if yosh <=4 or yosh>= 60:
    narh = 0
elif yosh <= 18:
    narh = 10000
else: narh = 20000
print(f"Chipta narxi siz uchun {narh} so'm")

#3-mashq Foydalanuvchidan ikita son kiritishni so'rang, 
# sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring
x = float(input('Birinchi sonni kiriting: '))
y = float(input('Ikkinchi sonni kiriting: '))
if x > y:
    print(f"{x} katta {y}")
elif x == y:
    print(f"{x} teng {y}")
else: print(f"{x} kichkina {y} dan")

# 4-mashq mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting.
#  Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta 
# mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring
#  va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda,
#  "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
mahsulotlar = ['olma', 'anor', 'uzum', 'banan', 'saryog\'', 'yog\'', 'guruch', 'un', 'choy', 'non']
savat = []
for n in range(5): #kod 5 marta qayta qayta ishlaydi
    savat.append(input(f"{n+1}-mahsulotni kiriting: ")) #foydalanuvchi qo'shgan har bir mahsulot savatga qo'shiladi
for mahsulot in savat: #savatdagi har bir mahsulot uchun ishlasin!
    if mahsulot in mahsulotlar: print(f"{mahsulot} do'konda bor") #agar savatdagi mahsulot do'kondagi mahsulotlar bn mos kelsa, kodni shu qismi ishlaydi
    else: print(f"{mahsulot} do'konimizda yo'q") #agar mahsulot mos kelmasa "ELSE" qismi ishlaydi

#5-mashq Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. 
# Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, do'konda yo'q 
# mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing. Agar mavjud_emas ro'yxati bo'sh bo'lsa,
# "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa 
# "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring
mahsulotlar = ['olma', 'anor', 'uzum', 'banan', 'saryog\'', 'yog\'', 'guruch', 'un', 'choy', 'non']
savat = []
bor_mahsulotlar = []
mavjud_emas = []
for n in range(5): #kod 5 marta qayta qayta ishlaydi
    savat.append(input(f"{n+1}-mahsulotni kiriting: "))
for mahsulot in savat:
    if mahsulot in mahsulotlar: bor_mahsulotlar.append(mahsulot)
    else: mavjud_emas.append(mahsulot)
if len(mavjud_emas) == 0:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor.")
else: 
    print(f"Quyidagi mahsulotlar do\'konimizda yo\'q: ")
    for mahsulot in mavjud_emas:
        print(mahsulot)


#6-mashq foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing.
#  Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan
#  ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa, 
# "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring
foydalanuvchilar = ['anvar', 'asilbek', 'admin', 'umid', 'hosilbek']
login = input('Yangi login tanlang!')
if login.lower() in foydalanuvchilar:
    print('Bu login band, Iltimos boshqa login kiriting!')
else: print(f"Xush kelibsiz! {login.title()}")

#7-mashq Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha
#  bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring. 
son = float(input('Biror son kiriting!'))
sonlar = [2, 3, 4, 5, 6, 7, 8, 9, 10]
for son1 in sonlar:
    if son%son1: print(f"{son} soni {son1} ga qoldiqsiz bo'linadi")










