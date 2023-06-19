import csv

def rating_elo_win(rating_a, rating_b):
    points = 1 // (1 + 10 ** ((rating_b - rating_a) // 400))
    if rating_a < 1400:
        new_rating = rating_a + 30 * (1 - points)
    elif 1400 < rating_a < 1800:
        new_rating = rating_a + 15 * (1 - points)
    else:
        new_rating = rating_a + 10 * (1 - points)
    return int(new_rating)

def rating_elo_lose(rating_a, rating_b):
    points = 1 // (1 + 10 ** ((rating_b - rating_a) // 400))
    if rating_a < 1400:
        new_rating = rating_a + 30 * (-1 - points)
    elif 1400 < rating_a < 1800:
        new_rating = rating_a + 15 * (-1 - points)
    else:
        new_rating = rating_a + 10 * (-1 - points)
    return int(new_rating)

def rating_elo_draw(rating_a, rating_b):
    points = 1 // (1 + 10 ** (rating_b - rating_a // 400))
    if rating_a < 1800:
        new_rating = rating_a + 30 * (0.5 - points)
    elif 1800 < rating_a < 2200:
        new_rating = rating_a + 15 * (0.5 - points)
    else:
        new_rating = rating_a + 10 * (0.5 - points)
    return int(new_rating)

with open("Results.csv") as r_file:
    file_reader = csv.DictReader(r_file, delimiter=";")
    preparatory = {}
    count = []


    for row in file_reader:
        preparatory[row["Команда №1"]] = 1000
        preparatory[row["Команда №2"]] = 1000
        count.append(row["Счёт"])

    data_base = {}
    for key, value in preparatory.items():
        if key.strip() not in data_base:
            data_base[key.strip()] = value


with open("Results.csv") as r_file:
    file_reader = csv.DictReader(r_file, delimiter=";")


    for i in range(0, len(count)):
        for wor in file_reader:
            if int(count[i].split(" ")[0]) > int(count[i].split(" ")[2]):
                data_base[wor["Команда №1"]] = rating_elo_win(data_base[wor["Команда №1"]], data_base[wor["Команда №2"]])
                data_base[wor["Команда №2"]] = rating_elo_lose(data_base[wor["Команда №2"]], data_base[wor["Команда №1"]])
                break
            elif int(count[i].split(" ")[0]) < int(count[i].split(" ")[2]):
                data_base[wor["Команда №2"]] = rating_elo_win(data_base[wor["Команда №2"]], data_base[wor["Команда №1"]])
                data_base[wor["Команда №1"]] = rating_elo_lose(data_base[wor["Команда №1"]], data_base[wor["Команда №2"]])
                break
            else:
                data_base[wor["Команда №2"]] = rating_elo_draw(data_base[wor["Команда №2"]], data_base[wor["Команда №1"]])
                data_base[wor["Команда №1"]] = rating_elo_draw(data_base[wor["Команда №1"]], data_base[wor["Команда №2"]])
                break

print(data_base)
