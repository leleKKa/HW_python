# Задача 2: Найдите сумму цифр трехзначного числа.
#a = int(input('a = '))
#if a < 1000  and a > 99:
 #   sum = 0
  #  while a > 0:
   #    m = a % 10
    #   sum = sum + m
     #  a = a // 10
    # print(sum)
# else:
#   print("Это не 3х значное число. Введите трехзначное число")

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# a + a + 2 (a+a) = 6*a  a = s/6

# n = int(input('n = '))
# if n % 6 == 0 and n > 0:
#    c = 0
#    p = n//6
#    c = p
#    k = (p + c)*2
#    print(p, k, c)
# else:
#    print("Введите другое число")

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек 
# отломить k долек, если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

# a = int(input("Введите число долек шоколадки с одной стороны: "))
# b = int(input("Введите число долек шоколадки с другой стороны: "))
# c = int(input("Введите число долек шоколадки, которое хотим съесть: "))
# a = 3
# b = 2
# c = 6

# if c <= a * b and c % a == 0:
#     print("yes")
# elif  c <= a * b and c % b == 0:
#     print("yes")
# else:
#     print("no")

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались 
# за проезд и получали билет с номером. Счастливым билетом называют такой билет 
# с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
   
# n = str(input("Введите шестизначный номер билета: ")) 
# if len(n) == 6:
#    sum1=int(n[0])+int(n[1])+int(n[2])
#    sum2=int(n[3])+int(n[4])+int(n[5])
#    if sum1 == sum2:
#       print('Счастливый')
#    else:
#       print('Обычный') 
# else:
#    print('Номер билета не шестизначный')