
shifr_or_de_shifr = input('Шивровать или Дешифровать:  ').lower()
while shifr_or_de_shifr != 'шифровать' and shifr_or_de_shifr != 'дешифровать': # Проверка на правильность ввода
    shifr_or_de_shifr = input('Не корректный ввод. Напиши Шифровать либо Дешифровать:  ').lower()



while True: # Проверка на правильность ввода целого числа
    whats_step = input('На сколько сдвигаем алфавит? Введите целое число: ')
    if whats_step.isdigit():  # Если ввод корректен
        whats_step = int(whats_step)
        break
    else:
        print("Ошибка! Введите целое число.")


enter = input('введите текст:  ')
conclusion = ''

if shifr_or_de_shifr == 'шифровать':
    for i in enter:
        if i.isalpha(): # если i является буквой, то к Unicode данной буквы + шаг сдвига
            conclusion += chr(ord(i) + whats_step)
        else:
            conclusion += i # все символы (кроме буквенных) добавляются без изменений
    print(conclusion)


if shifr_or_de_shifr == 'дешифровать':
    for i in enter:
        if i.isalpha(): # если i является буквой, то к Unicode данной буквы - шаг сдвига
            conclusion += chr(ord(i) - whats_step)
        else:
            conclusion += i # все символы (кроме буквенных) добавляются без изменений
    print(conclusion)

