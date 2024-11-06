import json

# Початкові дані про команди та очки
teams = {
    "Team A": 25,
    "Team B": 32,
    "Team C": 28,
    "Team D": 21,
    "Team E": 30,
    "Team F": 24,
    "Team G": 29,
    "Team H": 22,
    "Team I": 27,
    "Team J": 31
}

# Запис початкових даних у файл JSON (створення файлу teams.json)
with open("teams.json", "w") as file:
    json.dump(teams, file, indent=4)
print("Файл 'teams.json' створено з початковими даними.")


# Функція для виведення вмісту JSON файлу
def display_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        print(json.dumps(data, indent=4))


# Функція для додавання нової команди у JSON файл
def add_team(filename, team_name, points):
    with open(filename, 'r') as file:
        data = json.load(file)

    data[team_name] = points

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Команду {team_name} додано з {points} очками.")


# Функція для видалення команди з JSON файлу
def delete_team(filename, team_name):
    with open(filename, 'r') as file:
        data = json.load(file)

    if team_name in data:
        del data[team_name]
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Команду {team_name} видалено.")
    else:
        print("Команду не знайдено.")


# Функція для пошуку даних у JSON файлі за назвою команди
def search_team(filename, team_name):
    with open(filename, 'r') as file:
        data = json.load(file)

    if team_name in data:
        print(f"{team_name}: {data[team_name]} очок")
    else:
        print("Команду не знайдено.")


# Функція для визначення чемпіона і команд на призових місцях
def find_top_teams(filename):
    with open(filename, 'r') as file:
        teams_scores = json.load(file)

    # Сортуємо команди за очками у спадному порядку
    sorted_teams = sorted(teams_scores.items(), key=lambda x: x[1], reverse=True)
    champion = sorted_teams[0][0]
    second_place = sorted_teams[1][0]
    third_place = sorted_teams[2][0]

    results = {
        "champion": champion,
        "second_place": second_place,
        "third_place": third_place
    }

    # Записуємо результат у інший JSON файл
    with open("results.json", 'w') as file:
        json.dump(results, file, indent=4)

    print("Результати збережено у 'results.json'.")
    print(f"Чемпіон: {champion}")
    print(f"Друге місце: {second_place}")
    print(f"Третє місце: {third_place}")


# Основне меню для взаємодії з користувачем
def main():
    filename = "teams.json"

    while True:
        print("\nВиберіть дію:")
        print("1 - Вивести вміст JSON файлу")
        print("2 - Додати нову команду")
        print("3 - Видалити команду")
        print("4 - Пошук команди за назвою")
        print("5 - Визначити чемпіона та команди на призових місцях")
        print("6 - Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            display_json(filename)

        elif choice == "2":
            team_name = input("Введіть назву команди: ")
            points = int(input("Введіть кількість очок: "))
            add_team(filename, team_name, points)

        elif choice == "3":
            team_name = input("Введіть назву команди для видалення: ")
            delete_team(filename, team_name)

        elif choice == "4":
            team_name = input("Введіть назву команди для пошуку: ")
            search_team(filename, team_name)

        elif choice == "5":
            find_top_teams(filename)

        elif choice == "6":
            print("Вихід.")
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")


# Запуск програми
if __name__ == "__main__":
    main()
