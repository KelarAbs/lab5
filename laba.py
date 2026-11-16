# Задание 1

while True:
    text = input("Введите исходный текст: ")
    ind = False
    for digit in '0123456789':
        if digit in text:
            ind = True
            continue
            
    if ind:
        print("Введен не текст!/частично не текст!")
        continue
    if text == '':
        print("Введен пустой текст!")
        continue
    break
    


print(f"Исходный текст: {text}")

textArr = text.lower().replace(',','').replace('.','').split()
final = []
for word in textArr:
    word = word[-1] + word[:len(word)-1]
    final.append(word)    
            
print(f'Новый вариант текста: {final}')


# задание 2


while True:
    text1 = input("Введите исходный текст: ")
    ind1 = False
    for digit1 in '0123456789':
        if digit1 in text1:
            ind1 = True
            continue
            
    if ind1:
        print("Введен не текст!/частично не текст!")
        continue
    if text1 == '':
        print("Введен пустой текст!")
        continue
    break

print(f'Исходный текст : {text1}')

text1Arr = text1.lower().split()
mx = len(text1Arr[0])
fword = text1Arr[0]
for word in text1Arr:
    if mx < len(word):
        mx = len(word)
        fword = word
        break

print(f'Самое длинное слово: {fword} ({mx} букв)')

# Задание 3

import random
while True:
    try:
        n = int(input("Введите размер массива: "))
    except ValueError:
        print("Некорректный ввод")
        continue
    break

arr = [random.randint(1,500) for i in range(n)]
mx = arr[0]
indexmx = 0
for i in range(n):
    if mx<arr[i]:
        mx = arr[i]
        indexmx = i

sumarr = 0

for i in range(indexmx+1,n,1):
    sumarr += arr[i]

finalArr = [i for i in arr]

for i in range(n):
    for j in range(0,n-i-1,1):
        if abs(finalArr[j])<abs(finalArr[j+1]):
            finalArr[j] , finalArr[j+1] = finalArr[j+1] , finalArr[j]

print(f'Исходный размер массива: {n}')
print(f'Исходный массив: {arr}')
print(f'Сумма элементов массива, стоящих после максимального эл-та: {sumarr}')
print(f'Отсортированный массив: {finalArr}')

