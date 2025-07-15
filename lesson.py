
shifr_or_de_shifr = input('Шивровать или Дешифровать:  ').lower()
while shifr_or_de_shifr != 'шифровать' and shifr_or_de_shifr != 'дешифровать': # Проверка на правильность ввода
    shifr_or_de_shifr = input('ой !!! Что то не то ты ввел. Напиши шифровать либо дешифровать:  ').lower()

whats_step = input('На сколько сдвигаем алфавит, введи целое число:  ')
while whats_step.isdigit() != True: # Проверка на правильность ввода
    whats_step = input('ой !!! Что то не то ты ввел. Напиши шифровать либо дешифровать:  ').lower()


enter = input('введите текст:  ')
conclusion = ''

if shifr_or_de_shifr == 'шифровать':
    for i in enter:
        if i.isalpha():
            conclusion += chr(ord(i) + whats_step)
        else:
            conclusion += i
    print(conclusion)


if shifr_or_de_shifr == 'дешифровать':
    for i in enter:
        if i.isalpha():
            conclusion += chr(ord(i) - whats_step)
        else:
            conclusion += i
    print(conclusion)











