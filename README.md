# Телефонный справочник контактов

## Логика программы.
Пользователю программы телефонный справочник контактов предлагается выбрать действие:

  - для вывода записей,
  - для добавления новой записи,
  - для редактирования существующей записи,
  - для поиска записей по заданным критериям,
  - для выхода из программы.

Программа выполняет соответствующее действие в зависимости от выбора пользователя.

После выполнения действия программа возвращается к началу цикла и снова предлагает выбрать действие.

В файле contacts.csv представлен список случайных контактов в качестве примера для проверки работы программы.


## Описание функционала программы:

1. Код начинается с импорта модулей csv и os, которые используются для чтения и записи CSV файлов и взаимодействия с операционной системой.

2. Переменная PHONEBOOK определяется как путь к файлу "contacts.csv". Она использует модуль os.path для получения абсолютного пути к текущему скрипту (__file__) и dirname для получения имени директории скрипта.

3. В програме используется функция logging.basicConfig() для настройки основных параметров системы логирования. Во время вызова программы создается журнал main.log, в который записываются сообщения логов.

4. Функция load_contacts() считывает контакты из файла CSV, указанного в переменной PHONEBOOK. Она открывает файл с использованием csv.reader и добавляет каждую строку в contact_list как список.

5. Функция save_contacts(contact_list) записывает контакты из contact_list в файл CSV, указанный в PHONEBOOK. Она открывает файл с использованием csv.writer и записывает каждую новую строку с помощью writer.writerow().

6. Функция print_entry(entry) принимает контакт как параметр и выводит информацию о заданном контакте на экран, если контакт содержит как минимум 6 элементов.

7. Функция display_entries(entries) принимает список контактов в качестве параметра и вызывает функцию print_entry для каждого контакта в списке, выводя детали каждого контакта на экран.

8. Функция add_entry(contact_list) позволяет пользователю добавить новый контакт в contact_list. Она запрашивает у пользователя данные нового контакта и добавляет их в список. Затем вызывается функция save_contacts для сохранения обновленного списка в файле CSV.

9. Функция edit_entry(contact_list, index) позволяет пользователю изменить существующий контакт в contact_list по индексу. Она запрашивает у пользователя новые значения для каждого поля контакта, и изменения сохраняются с помощью функции save_contacts.

10. Функция search_entries(contact_list, search_criteria) принимает список критериев поиска в качестве параметров. Она ищет контакты, которые содержат все указанные критерии поиска, игнорируя регистр. Результаты поиска хранятся в списке search_results и отображаются с помощью функции display_entries.

11. Функция main() является точкой входа в программу. Это главная функция, которая обрабатывает основной цикл программы и предоставляет пользователю возможность взаимодействовать с программой через команды:
- загружает контакты из файла CSV
- отображает пользователю меню с вариантами действий
- выполняет соответствующие действия на основе выбора пользователя

12. Блок кода if __name__ == "__main__": гарантирует, что функция main будет выполнена только при запуске скрипта напрямую, а не при его импорте в качестве модуля.

    
## Как запустить программу.

### Клонируйте репозиторий:

git clone git@github.com:LiubovPerchuk/phonebook.git

### Перейдите в него в командной строке:

cd phonebook

### Запустите программу с помощью клавиши:
- run python file
### или команды:
- python phonebook.py
