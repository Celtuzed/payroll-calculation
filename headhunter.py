import requests
from statistics import mean

from predict_salary import predict_rub_salary


def get_hh_salary(item, salaries):

    salary = item['salary']

    if salary and salary['currency'] == "RUR":
        payment_from = salary['from']
        payment_to = salary['to']
        salary = predict_rub_salary(payment_from, payment_to)
        return salary

def get_vacancies_for_one_language(language, hh_url):

    params = {
        "text": f"Программист {language}",
        "area": 1, #id Москвы у HeadHunter API
        "per_page": "100"
        }

    response = requests.get(hh_url, params)
    salaries = []
    response_json = response.json()
    items = response_json['items']

    for item in items:
        salary = get_hh_salary(item, salaries)
        if salary:
            salaries.append(salary)

    vacancies_found = response_json['found']

    return vacancies_found, salaries

def get_vacancies_for_headhunter(languages):

    hh_url = "https://api.hh.ru/vacancies"

    vacancies = {}

    for language in languages:

        vacancies_found, salaries = get_vacancies_for_one_language(language, hh_url)

        for item in items:
            salary = get_hh_salary(item, salaries)
            if salary:
                salaries.append(salary)

        vacancies[language] = {
            "vacancies_found": vacancies_found,
            "vacancies_processed": len(salaries),
            "average_salary": int(mean(salaries))
        }

    return vacancies
