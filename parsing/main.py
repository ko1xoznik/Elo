import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

URL_TEMPLATE = "https://www.sport-express.ru/football/L/russia/premier/2022-2023/calendar/tours/"
FILE_NAME = "my.csv"

def parse(url=URL_TEMPLATE):
    result_list = {'Команда №1': [], 'Команда №2': [], 'Счёт': []}
    r = requests.get(URL_TEMPLATE)
    soup = bs(r.text, "html.parser")
    vacancies_name = soup.find_all('span', class_='link-underline')
    vacancies_count = soup.find_all('p', class_='score_time')

    count = 1
    for name in vacancies_name:
        if count % 2 != 0:
            result_list['Команда №1'].append(name.text)
        else:
            result_list['Команда №2'].append(name.text)
        count += 1
    for counter in vacancies_count:
        result_list['Счёт'].append(counter.text)

    return result_list



df = pd.DataFrame(data=parse())
df.to_csv(FILE_NAME)
