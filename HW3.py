# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.

# list_1 = [1, 2, 3, 3, 5, 6, 3]
# k = int(input("Введите цифру: "))
# count = 0
# for i in range (0, len(list_1)):
#     if k == list_1[i]:
#         count += 1
# print(count)

# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k 
# и вывести его.

# list_1 = [5, 6, 1, 2, 4]
# k = int(input("Введите цифру: "))
# number = 0
# min = (k - list_1[0])**2
# for i in range (len(list_1)):
#     if (k-list_1[i])**2 <= min:
#         min = (k-list_1[i])**2
#         number=i
# print(list_1[number])

# m = abs(k - list_1[0])  # модуль числа
# number = list_1[0]
# for i in range(1, len(list_1)):
#     if m > abs(list_1[i] - k):
#         m = abs(list_1[i] - k)
#         number = list_1[i]
# print(number)

# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.

# В случае с английским алфавитом очки распределяются так:

# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:

# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова k 
# и выводит его. Будем считать, что на вход подается только одно слово, которое содержит 
# либо только английские, 
# либо только русские буквы.

list_English = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP', 4:'FHVWY', 5:"K" , 8:'JX', 10:'QZ'}
list_ru = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ', 4:'ЙЫ', 5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФШЪ'}
k = input('Введите слово на русском или английском: ')
list_word = []
summa = 0

for dict in list_ru:
   for i in k:
      for key, value in list_ru.items():
           if i.upper() in value:
              summa += key
print(summa)

for dict in list_English:
   for i in k:
      for key, value in list_English.items():
           if i.upper() in value:
              summa += key
print(summa)
