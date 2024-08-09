from datetime import datetime, date

# Функция для определения дня недели
def get_weekday(day, month, year):
    date_obj = date(year, month, day)
    return date_obj.strftime("%A")

# Функция для определения високосного года
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# Функция для определения возраста пользователя
def calculate_age(day, month, year):
    today = date.today()
    birth_date = date(year, month, day)
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

# Функция для отображения даты в формате с цифрами, прорисованными звёздочками
def display_digit_style(number):
    digits = {
        '0': [" *** ", "*   *", "*   *", "*   *", " *** "],
        '1': ["  *  ", " **  ", "  *  ", "  *  ", " *** "],
        '2': [" *** ", "*   *", "   * ", "  *  ", "*****"],
        '3': ["*****", "   * ", " *** ", "   * ", "*****"],
        '4': ["*   *", "*   *", "*****", "    *", "    *"],
        '5': ["*****", "*    ", "**** ", "    *", "**** "],
        '6': [" *** ", "*    ", "**** ", "*   *", " *** "],
        '7': ["*****", "    *", "   * ", "  *  ", "  *  "],
        '8': [" *** ", "*   *", " *** ", "*   *", " *** "],
        '9': [" *** ", "*   *", " ****", "    *", " *** "],
        ' ': ["     ", "     ", "     ", "     ", "     "],
        '/': ["  *  ", "  *  ", "  *  ", "     ", "  *  "]
    }

    digit_lines = ["", "", "", "", ""]
    for char in number:
        for i in range(5):
            digit_lines[i] += digits[char][i] + " "
    
    return "\n".join(digit_lines)

# Основная программа
def main():
    # Запрашиваем у пользователя дату рождения
    day = int(input("Введите день вашего рождения (дд): "))
    month = int(input("Введите месяц вашего рождения (мм): "))
    year = int(input("Введите год вашего рождения (гггг): "))

    # Определяем день недели
    weekday = get_weekday(day, month, year)
    print(f"Вы родились в {weekday}.")

    # Определяем, был ли год високосным
    if is_leap_year(year):
        print(f"{year} был високосным годом.")
    else:
        print(f"{year} не был високосным годом.")

    # Определяем возраст пользователя
    age = calculate_age(day, month, year)
    print(f"Вам сейчас {age} лет.")

    # Выводим дату в формате электронного табло
    formatted_date = f"{day:02}/{month:02}/{year}"
    print("Дата вашего рождения:")
    print(display_digit_style(formatted_date))

if __name__ == "__main__":
    main()