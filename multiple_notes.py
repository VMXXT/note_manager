from datetime import datetime # импортируем библиотеку для работы с датами

# зададим читаемые для пользователя имена ключей словаря
key_translation = {
    "id": "Идентификатор",
    "username": "Имя пользователя",
    "titles": "Заголовки",
    "content": "Описание",
    "status": "Статус",
    "created_date": "Дата создания",
    "issue_date": "Дата дедлайна"
}

# Функция создания новой заметки.
def create_note():
    # Создаем словарь для хранения информации о заметке и записываем имя пользователя
    note = {"id": len(notes_list) + 1, "username": input("\nВведите имя пользователя: "), "titles": []}

    # создаем цикл для множественного ввода заголовков
    while True:
        # Запрашиваем у пользователя ввод заголовка заметки
        title = input("Введите заголовок заметки (для завершения кода введите 'стоп'): ")

        # Проверяем команду завершения ввода
        if title.lower() == "стоп":
            break
        if title == "":
            print("Заголовок не может быть пустым. Пожалуйста, введите заголовок.")
            continue

        # Добавляем только новые значения в список заголовков
        if title not in note["titles"]:  # если такого заголовка нет, добавляем
            note["titles"].append(title)
        elif title in note["titles"]:  # если заголовок есть, просим ввести другой
            print("Этот заголовок уже был добавлен. Введите другой.")

    # ввод описания заметки и цикл проверки пустого значения.
    while True:
        content = input("Введите описание заметки: ")
        if content == "":
            print("Описание не может быть пустым. Пожалуйста, введите описание.")
            continue
        else:
            note["content"] = content
            break

    # ввод статуса заметки и цикл проверки пустого значения.
    while True:
        status = input("Введите статус заметки 'Выполнено', 'В процессе', 'Отложено' или введите свой статус): ")
        # Проверка на пустую строку
        if status == "":
            print("Вы ввели некорректное значение")
            continue
        else:
            note["status"] = status
            break

    # Форматируем дату создания заметки и дату дедлайн.
    temp_created_date = datetime.today()  # присваиваем переменной сегодняшнюю дату.
    note["created_date"] = datetime.strftime(temp_created_date, "%d.%m.%Y")  # форматируем в строку.

    # Создаем цикл для проверки верного ввода даты дедлайна.
    while True:
        temp_issue_date = input("Дата дедлайн в формате дд.мм.гггг - ")

        try:
            # дата до форматирования в строку для проверки дедлайна.
            issue_date = datetime.strptime(temp_issue_date, "%d.%m.%Y")
            # преобразуем дату в строку для записи в словарь
            note["issue_date"] = datetime.strptime(temp_issue_date, "%d.%m.%Y").strftime("%d.%m.%Y")
            break  # Выход из цикла, если дата введена правильно

        except ValueError:
            # Если возникает ошибка, значит дата введена неправильно
            print("Вы ввели дату в неверном формате. Пожалуйста, используйте формат дд.мм.гггг.")

    # Выводим собранные данные
    print("\nСобранная информация о заметке:")
    for key, value in note.items():
        translated_key = key_translation.get(key, key)
        if key == "titles":  # делаем читаемыми заголовки путем объединения через запятую
            value = ", ".join(value)
        print(f"{translated_key}: {value}")

    # Проверка дедлайна
    current_date = datetime.today().date()  # присваиваем текущую дату без времени
    # используем объект timedelta, вычитаем текущую дату из даты дедлайна
    days_difference = (issue_date.date() - current_date).days  # присваиваем разницу в днях без времени
    # задаем цикл для проверки истек ли дедлайн
    if days_difference < 0:
        print(f"\nВнимание! Дедлайн истёк {-days_difference} дней назад.")
    elif days_difference == 0:
        print("\nДедлайн сегодня!")
    else:
        print(f"\nДо дедлайна осталось {days_difference} дней.")

    # добавляем заметку в список заметок
    notes_list.append(note)
    return note

# Основной код программы.
print("Добро пожаловать в 'Менеджер заметок'! Вы можете добавить новую заметку")
notes_list = [] # список словарей заметок
note = create_note() # запрашиваем ввод первой заметки.

# создаем цикл запроса на добавление новой заметки
while input("\nХотите добавить ещё одну заметку? (да/нет или Enter для остановки ввода): ").lower() == 'да':
        note = create_note()

# Выводим собранные данные
print("\nВаши заметки:")
print("_" * 20)
for note in notes_list:
    for key, value in note.items():
        translated_key = key_translation.get(key, key)
        if key == "titles": # делаем читаемыми заголовки путем объединения через запятую
            value = ", ".join(value)
        print(f"{translated_key}: {value}")

        # Цикл для обновления статуса заметки
    statuses = ["Выполнено", "В процессе", "Отложено"]

    while True:
        status_new = input("\nВыберите новый статус заметки "
                            "(1. Выполнено, 2. В процессе, 3. Отложено или введите свой статус): ")
        # Проверка на пустую строку
        if status_new == "":
            print("Вы ввели некорректное значение")
            continue  # Возврат к началу цикла для нового ввода
        # Конвертация ввода в число
        try:
            status_new = int(status_new)
        except ValueError:
            note["status"] = status_new
            break  # Выход из цикла после корректного пользовательского ввода
        # Если пользователь ввел число, проверяем
        if status_new == 1:
            note["status"] = statuses[0]
            break
        elif status_new == 2:
            note["status"] = statuses[1]
            break
        elif status_new == 3:
            note["status"] = statuses[2]
            break
        else:
            print("Вы ввели некорректное значение")
    # Выводим новый статус заметки
    print(f"Статус заметки успешно обновлён на: {note['status']}")

    # Добавляем строку с дедлайном.
    current_date = datetime.today().date()
    issue_date_note = datetime.strptime(note['issue_date'], "%d.%m.%Y")
    days_difference = (issue_date_note.date() - current_date).days
    if days_difference < 0:
        print(f"Дедлайн истёк {-days_difference} дней назад.")
    elif days_difference == 0:
        print("Дедлайн сегодня!")
    else:
        print(f"\nДо дедлайна осталось {days_difference} дней.")
    print("_" * 40)