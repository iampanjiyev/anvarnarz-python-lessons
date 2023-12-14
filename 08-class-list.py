"""
#08-dars: Ro'yxatlar bilan ishlash

"""
#1-mashq
davlatlar = ["O'zbekiston", 'Amerika Qo\'shma shtatlari', 'Rassiya', 'Ruminiya', 'Vengriya', 'Qozog\'iston', 'Fransiya']
print(len(davlatlar))

#2-mashq
print(sorted(davlatlar))

#3-mashq sorted() yordamida ro'yhatni teskari tartibda konsolga chiqaring
print(sorted(davlatlar, reverse=True))

#4-mashq Asl ro'yhatni qaytadan konsolga chiqaring
print(davlatlar)

#5-mashq reverse() yordamida ro'yhatni ortidan boshlab chiqaring
davlatlar.reverse()
print(davlatlar)

#6-mashq sort() metodi yordamida ro'yhatni avval alifbo bo'yicha keyin esa alifboga teskari tartibda konsolga chiqaring.
davlatlar.sort()
print('Alifbo tartibida: ', davlatlar)
davlatlar.sort(reverse=True)
print('Alifboga teskari: ', davlatlar)

#7-mashq 120 dan 1200 gacha bo'lgan juft sonlar ro'yhatini tuzing.
juft_sonlar = list(range(120, 1200, 2))
print(juft_sonlar)

#8-mashq sonlar yig'indisi
sonlar_y = sum(juft_sonlar)
print(sonlar_y)

#9-mashq Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
print(max(juft_sonlar) - min(juft_sonlar))

#10-mashq Ro'yxatdagi elementlar sonini hisoblang
print(len(juft_sonlar))

#11-mashq Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
print(juft_sonlar[:20], juft_sonlar[265:285], juft_sonlar[-20:])

#12-mashq taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar = ['osh', 'shurva', 'somsa', 'tandir', 'manti']

#13-mashq nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta = taomlar[:]

#14-mashq Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
nonushta.remove('manti')
nonushta.remove('shurva')
nonushta.append('Tuxum')
nonushta.append('norin')

#15-mashq Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
print(taomlar)
print(nonushta)

#16-mashq Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
nonushta = tuple(nonushta)
nonushta[0] = 'qaymoq va non'
print(nonushta)
# ERROR beradi, sababi tuplega aylangandan keyin uni o'zgartirib bo'lmaydi





