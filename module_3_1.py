calls = 0 #переменная, в которую будут записываться все вызовы функций
def count_calls(): #функция, которая будет подсчитывать
    global calls #делаем переменную глобальной
    calls += 1 #вызвали функцию, значит прибавили в переменную
def string_info(string): #функция по условию
    count_calls() #вызов функции на подсчёт
    return len(string), string.upper(), string.lower() #вывести длину, в верхнем регистре, в нижнем регистре
def is_contains(string, list_to_search): #функция по условию
    count_calls() #вызов функции на посчёт
    string = string.lower() #делаем слово в нижнем регистре
    register = [] #список, в который будут добавляться слова в нижнем регистре
    for i in list_to_search: #цикл
        register.append(i.lower()) #берём слова из списка и переводим их в нижний регистр, а затем добавляем в список с нижним регистром
    if string in register: #если слово найдено, то
        return True #вернуть значение
    else: #иначе
        return False #вернуть значение
print(string_info('Capybara')) #вывод на экран
print(string_info('Armageddon')) #вывод на экран
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # вывод на экран
print(is_contains('cycle', ['recycling', 'cyclic'])) # вывод на экран
print(calls) #вывод на экран