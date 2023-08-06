# Работа с файлами - работа с телефонной книгой
import random


def open_file():
    while True:
        file_path = input("Введите путь к файлу: ")
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file_path, file.readlines()
        except FileNotFoundError:
            print("Файл не найден. Пожалуйста, проверьте путь и попробуйте снова.")
        except UnicodeDecodeError:
            print("Ошибка при чтении файла. Попробуйте другой файл или убедитесь, что файл имеет правильную кодировку.")

def replace_line_in_content(file_content, line_number, new_content):
    file_content[line_number - 1] = new_content + '\n'
    return file_content

def search_in_file(file_content, search_word):
    matched_lines = []
    for line_number, line in enumerate(file_content, 1):
        if search_word in line:
            matched_lines.append((line_number, line))
    return matched_lines

def write_to_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(content)


file_path, lines = open_file()
print("Содержимое файла:")
print("".join(lines))

search_word = input("Введите слово для поиска: ")
matched_lines = search_in_file(lines, search_word)

if not matched_lines:
    print("Слово не найдено в файле.")
else:
    for line_number, line in matched_lines:
        print(f"Строка {line_number}: {line.strip()}")

chosen_line = int(input("Введите номер строки для замены: "))
new_data = input("Введите новые данные для выбранной строки: ")
updated_lines = replace_line_in_content(lines, chosen_line, new_data)

write_to_file(file_path, updated_lines)
print(f"Строка {chosen_line} обновлена.")

# # Генератор файла

# def generate_data(names, surnames, phone_length, entry_count):
#     entries = []
#     for _ in range(entry_count):
#         name = random.choice(names)
#         surname = random.choice(surnames)
#         phone = ''.join(random.choice('0123456789') for _ in range(phone_length))
#         entry = f"{name},{surname},{phone}\n"
#         entries.append(entry)
#     return entries

# # Пример использования:
# names = ["Иван", "Петр", "Анна", "Ольга", "Архип", "Стархип", "Федор", "Армен", "Георгий", "Наталья", "Зинаида", "Немезида", "ЖюльВерн"]
# surnames = ["Иванов", "Петров", "Сидоров", "Николаев", "Артамонов", "Пушкин", "Васеччкин", "Жюльен", "Поросенков", "Моросенков"]
# phone_length = 11
# entry_count = 1000

# entries = generate_data(names, surnames, phone_length, entry_count)
# file_path = "phon.txt"
# write_to_file(file_path, entries)