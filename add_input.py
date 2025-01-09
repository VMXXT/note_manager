from datetime import datetime # импортируем библиотеку для работы с датами

# Запрашиваем у пользователя информацию
username = input("Введите имя пользователя: ")

# Запрашиваем несколько заголовков и добавляем их в список
title1 = input("Введите первый заголовок заметки: ")
title2 = input("Введите второй заголовок заметки: ")
title3 = input("Введите третий заголовок заметки: ")
titles = [title1, title2, title3]

content = input("Введите описание заметки: \n")
status = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")

# Форматируем дату создания заметки и дату дэдлайна
created_date = datetime.today() # присваиваем переменной сегодняшнюю дату
temp_created_date = datetime.strftime(created_date, "%d.%m") # форматируем, убираем год

#создадим цикл для проверки верного ввода даты дэдлайна
while True:
    issue_date = input("Дата дэдлайна в формате дд.мм.гггг - ")

    try:
        temp_issue_date = datetime.strptime(issue_date, "%d.%m.%Y").strftime("%d.%m") # убираем год
        break  # Выход из цикла, если дата введена правильно

    except ValueError:
    # Если возникает ошибка, значит дата введена неправильно
        print("Вы ввели дату в неверном формате. Пожалуйста, используйте формат дд.мм.гггг.")

#Вывод данных
print("\nВы ввели следующие данные:")
print("Имя пользователя:", username)
print("Заголовок заметки:", titles)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", temp_created_date)
print("Дата истечения заметки:", temp_issue_date)