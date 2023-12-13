import csv
import datetime

def read_questions_from_csv(csv_file):
    """
    Читает вопросы и варианты ответов из CSV-файла.
    """
    questions = []
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            question, *options = row
            questions.append((question, options))
    questions.pop(0)
    return questions

def get_user_gender():
    """
    Запрашивает у пользователя пол (м/ж) и возвращает корректное значение.
    """
    while True:
        user_gender = input("Введите ваш гендер (м/ж): ").lower()
        if user_gender in ['м', 'ж']:
            return user_gender
        else:
            print("Некорректный ввод. Введите 'м' для мужского пола или 'ж' для женского пола.")

def get_user_age():
    """
    Запрашивает у пользователя возраст и возвращает корректное значение.
    """
    while True:
        user_age = input("Введите ваш возраст: ")
        if user_age.isdigit() and 5 < int(user_age) < 199:
            return user_age
        else:
            print("Некорректный ввод. Введите возраст цифрами в пределах от 6 до 198.")

def ask_questions(questions, user_name, user_surname, user_gender, user_age):
    """
    Задает вопросы и записывает ответы в CSV-файл.
    """
    user_answers = []
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"{user_name}_{user_surname}_{timestamp}.csv"

    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Фамилия", user_surname])
        writer.writerow(["Имя", user_name])
        writer.writerow(["Пол", user_gender])
        writer.writerow(["Возраст", user_age])
        writer.writerow(["Вопрос", "Ответ"])

        for question, options in questions:
            print(question)
            for i, option in enumerate(options, 1):
                print(f"{i}. {option}")

            while True:
                try:
                    user_input = int(input("\nВыберите вариант ответа (введите номер): "))
                    if 1 <= user_input <= len(options):
                        break
                    else:
                        print("Пожалуйста, введите допустимый номер варианта ответа.")
                except ValueError:
                    print("Пожалуйста, введите номер варианта ответа.")

            selected_option = options[user_input - 1]
            user_answers.append((question, selected_option))
            writer.writerow([question, selected_option])

    return user_answers

if __name__ == "__main__":
    input_csv_file = "questions_psm.csv"
    
    user_name = input("Введите ваше имя: ")
    user_surname = input("Введите вашу фамилию: ")
    user_gender = get_user_gender()
    user_age = get_user_age()

    questions = read_questions_from_csv(input_csv_file)
    user_answers = ask_questions(questions, user_name, user_surname, user_gender, user_age)

    print("Спасибо за ответы!")
