from datetime import datetime # Импорт библиотеки для работы с датами.

notes_list = [] # Список словарей заметок.

# Читаемые для пользователя имена ключей словаря.
key_translation = {
    "id": "Идентификатор заметки (ID)",
    "username": "Имя пользователя",
    "title": "Заголовок",
    "content": "Описание",
    "status": "Статус",
    "created_date": "Дата создания",
    "issue_date": "Дата дедлайна"
}

# Функция создания новой заметки.
def create_note():
    # Словарь для хранения информации о заметке.
    note = {"id": len(notes_list) + 1, "username": input("\nВведите имя пользователя: ") }



    # Цикл ввода заголовка.
    while True:
        # Запрашиваем у пользователя ввод заголовка заметки.
        title_add = input("Введите заголовок заметки : ")
        # Проверка на пустой ввод.
        if title_add == "":
            print("Заголовок не может быть пустым. Пожалуйста, введите заголовок.")
            continue
        break
    note["title"] = title_add


    # Ввод описания заметки и цикл проверки пустого значения.
    while True:
        content = input("Введите описание заметки: ")
        if content == "":
            print("Описание не может быть пустым. Пожалуйста, введите описание.")
            continue
        else:
            note["content"] = content
            break

    # Ввод статуса заметки и цикл проверки пустого значения.
    while True:
        status = input("Введите статус заметки 'Выполнено', 'В процессе', 'Отложено' или введите свой статус): ")
        # Проверка на пустую строку.
        if status == "":
            print("Вы ввели некорректное значение")
            continue
        else:
            note["status"] = status
            break

    # Форматирование даты создания заметки и даты дедлайн.
    temp_created_date = datetime.today()  # Присвоение переменной сегодняшней даты.
    note["created_date"] = datetime.strftime(temp_created_date, "%d.%m.%Y")  # Форматирование в строку.

    # Цикл для проверки верного ввода даты дедлайна.
    while True:
        temp_issue_date = input("Дата дедлайн в формате дд.мм.гггг - ")

        try:
            # Дата до форматирования в строку для проверки дедлайна.
            issue_date = datetime.strptime(temp_issue_date, "%d.%m.%Y")
            # Преобразование даты в строку для записи в словарь.
            note["issue_date"] = datetime.strptime(temp_issue_date, "%d.%m.%Y").strftime("%d.%m.%Y")
            break  # Выход из цикла, если дата введена правильно.

        except ValueError:
            # Если возникает ошибка, значит дата введена неправильно.
            print("Вы ввели дату в неверном формате. Пожалуйста, используйте формат дд.мм.гггг.")

    # Вывод собранных данных о заметке.
    print("\nСобранная информация о заметке:")
    for key, value in note.items():
        translated_key = key_translation.get(key, key) # Присвоение ключам читаемых значений.
        print(f"{translated_key}: {value}")

    # Проверка дедлайна.
    current_date = datetime.today().date()  # Присвоение текущей даты без времени.
    # Используем объект timedelta, вычитаем текущую дату из даты дедлайна.
    days_difference = (issue_date.date() - current_date).days  # Присвоение разницы в днях без времени.
    # Цикл для проверки дедлайна.
    if days_difference < 0:
        print(f"\nВнимание! Дедлайн истёк {-days_difference} дней назад.")
    elif days_difference == 0:
        print("\nДедлайн сегодня!")
    else:
        print(f"\nДо дедлайна осталось {days_difference} дней.")

    # Добавление заметки в список заметок.
    notes_list.append(note)
    return note # Выход из функции


# Функция удаления заметок.
def delete_note():
    # Проверка пустого значения списка словарей заметок.
    if not notes_list:
        print("Список заметок пуст.")
        return

    # Цикл удаления заметки.
    while True:
        # Ввод пользователем критерия удаления заметки.
        criterion = input("Если вы хотите удалить заметку по идентификатору(ID) введите цифру '1',"
                          "\nесли хотите удалить заметку по заголовку нажмите '2',"
                          "\nесли хотите удалить заметку по имени пользователя введите '3':, \n")

        # Проверка, что пользователь ввел число.
        try:
            criterion = int(criterion)
        except ValueError:
            print("Пожалуйста, введите число (1, 2 или 3).")
            continue
        # Удаление заметки по ID.
        if criterion == 1:
            note_id_del = input("Введите ID заметки, которую хотите удалить: ")
            # Проверка, что пользователь ввел число.
            try:
                note_id_del = int(note_id_del)
            except ValueError:
                print("ID заметки должен быть числом")
                continue

            for note in notes_list: # Поиск заметки в списке словарей.
                if note["id"] == note_id_del:
                    confirm = input("Вы уверены, что хотите удалить эту заметку? (да/нет): ").lower()
                    if confirm == "да":
                        notes_list.remove(note) # Удаление заметки.
                        print("Заметка удалена")
                        break
            else:
                print("Заметка с указанным ID не найдена.")

        # Удаление заметки по заголовку.
        elif criterion == 2:
            note_title_del = input("Введите заголовок заметки, которую хотите удалить: ").lower()
            for note in notes_list: # Поиск заметки в списке словарей.
                if note["title"].lower() == note_title_del:
                    confirm = input("Вы уверены, что хотите удалить эту заметку? (да/нет): ").lower()
                    if confirm == "да":
                        notes_list.remove(note) # Удаление заметки.
                        print("Заметка удалена")
                        break
            else:
                print("Заметка с указанным заголовком не найдена.")

        # Удаление заметки по имени пользователя.
        elif criterion == 3:
            note_name_del = input("Введите имя пользователя для удаления заметки: ").lower()
            for note in notes_list: # Поиск заметки в списке словарей.
                if note["name"].lower == note_name_del:
                    confirm = input("Вы уверены, что хотите удалить эту заметку? (да/нет): ").lower()
                    if confirm == "да":
                        notes_list.remove(note) # Удаление заметки
                        print("Заметка удалена")
                        break
            else:
                print(f"Заметка пользователя {note_name_del} не найдена.")

        else:
            print("Некорректный критерий удаления. Попробуйте снова.")

        # Вывод оставшихся заметок после удаления.
        if notes_list:
            print("\nТекущий список заметок:")
            print("_" * 40)
            for note in notes_list:
                for key, value in note.items():
                    translated_key = key_translation.get(key, key)
                    print(f"{translated_key}: {value}")
                print("_" * 40)
        else:
            print("Список заметок пуст.")

        # Предложение продолжить удаление или вернуться в меню.
        next_action = input("Хотите продолжить удаление? (да/нет): ").lower()
        if next_action != "да":
            break



# Функция вывода всех заметок с дедлайном.
def notes_print():
    if notes_list:
        print("Список заметок")
        print("_" * 40)
        for note in notes_list:
            for key, value in note.items():
                translated_key = key_translation.get(key, key)
                print(f"{translated_key}: {value}")

            # Выводим строку с дедлайном.
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
    else:
        print("Список заметок пуст")



# Основной код программы.
print("Добро пожаловать в 'Менеджер заметок'! Вы можете добавить новую заметку")

# Цикл для добавления, удаления и просмотра заметок.
while True:
    action = input('Выберите действие: добавить заметку (1), удалить заметку (2), '
                   'посмотреть все заметки (3) или выйти (4): ')
    # Проверка, что пользователь ввел число.
    try:
        action = int(action)
    except ValueError:
        print("Пожалуйста, введите число (1, 2, 3 или 4).")
        continue
    # Если пользователь ввел число, проверяем.
    if action == 1:
        note = create_note()
        continue
    elif action == 2:
        delete_note()
        continue
    elif action == 3:
        notes_print()
        continue
    elif action == 4:
        break
    else:
        print("Вы ввели некорректное значение")

