import csv
import os

PHONEBOOK = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'contacts.csv')


def load_contacts():
    """Метод загрузки контактов из файла в список."""
    contact_list = []
    try:
        with open(PHONEBOOK, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                contact_list.append(row)
    except FileNotFoundError:
        raise FileNotFoundError("Файл не найден")
    return contact_list


def save_contacts(contact_list):
    """Метод сохранения контактов из списка в файл.
    :param contact_list: список контактов"""
    with open(PHONEBOOK, 'w', newline='') as file:
        writer = csv.writer(file)
        for entry in contact_list:
            writer.writerow(entry)


def print_entry(entry):
    """Метод вывода информации о контакте.
    :param entry: контакт"""
    if len(entry) >= 6:
        print(f"Фамилия: {entry[0]}")
        print(f"Имя: {entry[1]}")
        print(f"Отчество: {entry[2]}")
        print(f"Название организации: {entry[3]}")
        print(f"Рабочий телефон: {entry[4]}")
        print(f"Личный телефон: {entry[5]}")
        print()


def display_entries(entries):
    """Метод вывода списка контактов.
    :param entries: список контактов"""
    for entry in entries:
        print_entry(entry)


def add_entry(contact_list):
    """Метод добавления новой записи в список контактов.
    :param contact_list: список контактов"""
    entry = []
    entry.append(input("Введите фамилию: "))
    entry.append(input("Введите имя: "))
    entry.append(input("Введите отчество: "))
    entry.append(input("Введите название организации: "))
    entry.append(input("Введите рабочий телефон: "))
    entry.append(input("Введите личный телефон: "))
    contact_list.append(entry)
    save_contacts(contact_list)
    print("Запись успешно добавлена.")


def edit_entry(contact_list, index):
    """Метод редактирования записи в списке контактов по индексу.
    :param contact_list: список контактов
    :param index: индекс записи для редактирования"""
    if 1 <= index <= len(contact_list):
        entry = contact_list[index - 1]
        print("Введите новые значения (оставьте пустым, чтобы не изменять):")
        entry[0] = input(f"Фамилия ({entry[0]}): ") or entry[0]
        entry[1] = input(f"Имя ({entry[1]}): ") or entry[1]
        entry[2] = input(f"Отчество ({entry[2]}): ") or entry[2]
        entry[3] = input(f"Название организации ({entry[3]}): ") or entry[3]
        entry[4] = input(f"Рабочий телефон ({entry[4]}): ") or entry[4]
        entry[5] = input(f"Личный телефон ({entry[5]}): ") or entry[5]
        save_contacts(contact_list)
        print("Запись успешно отредактирована.")
    else:
        print("Записи с таким индексом не существует.")


def search_entries(contact_list, search_criteria):
    """Метод поиска записи по заданным критериям.
    :param contact_list: список контактов
    :param search_criteria: критерии поиска
    :return: список найденных записей"""
    search_results = []
    criteria_list = [
        criteria.strip().lower() for criteria in search_criteria.split(",")]
    for entry in contact_list:
        entry_values = [str(value).lower() for value in entry]
        criteria_matched = True
        for criteria in criteria_list:
            if not any(criteria in value for value in entry_values):
                criteria_matched = False
                break
        if criteria_matched:
            search_results.append(entry)
    if search_results:
        display_entries(search_results)
    else:
        print("Записи не найдены.")
    return search_results


def main():
    """Основной метод для взаимодействия с программой."""
    contact_list = load_contacts()
    while True:
        print("1. Вывести записи")
        print("2. Добавить новую запись")
        print("3. Редактировать запись")
        print("4. Поиск записей")
        print("5. Выход")
        choice = input("Выберите действие: ")
        if choice == "1":  # Вывод записей
            display_entries(contact_list)
        elif choice == "2":  # Добавление записи
            add_entry(contact_list)
        elif choice == "3":  # Редактирование записи
            index = int(input("Введите индекс записи для отредактирования: "))
            edit_entry(contact_list, index)
        elif choice == "4":  # Поиск записей
            search_criteria = input(
                "Введите критерии поиска через запятую: ").split(",")
            search_entries(contact_list, ",".join(search_criteria))
        elif choice == "5":  # Выход
            break
        else:
            print("Некорректный выбор.")


if __name__ == "__main__":
    main()
