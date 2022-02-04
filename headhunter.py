import requests
from statistics import mean

from predict_salary import predict_rub_salary


def get_hh_salary(item, salaries):

    salary = item['salary']

    if salary and salary['currency'] == "RUR":
        payment_from = salary['from']
        payment_to = salary['to']
        predict_salary = predict_rub_salary(payment_from, payment_to)
        return predict_salary


def get_vacancies_for_headhunter(languages):

    hh_url = "https://api.hh.ru/vacancies"

    vacancies = {}

    for language in languages:

        params = {
            "text": f"Программист {language}",
            "area": "1", #id Москвы у HeadHunter API
            "per_page": "100"
            }

        response = requests.get(hh_url, params)
        salaries = []
        items = response.json()['items']

        for item in items:
            predict_salary = get_hh_salary(item, salaries)
            if predict_salary:
                salaries.append(predict_salary)

        vacancies_found = response.json()['found']
        vacancies[language] = {
            "vacancies_found": vacancies_found,
            "vacancies_processed": len(salaries),
            "average_salary": int(mean(salaries))
        }

    return vacancies