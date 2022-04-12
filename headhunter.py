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


def get_vacancies_for_language(language):

    hh_url = "https://api.hh.ru/vacancies"
    params = {
        "text": f"Программист {language}",
        "area": 1,  # id Москвы у HeadHunter API
        "per_page": "100"
        }
    salaries = []

    page = 0
    pages = 1


    while page < pages:

        response = requests.get(hh_url, params)
        vacancies_info = response.json()
        pages = vacancies_info["pages"]
        page = page+1
        params["page"] = page
        items = vacancies_info['items']

        for item in items:
            salary = get_hh_salary(item, salaries)
            if salary:
                salaries.append(salary)

    vacancies_found = vacancies_info['found']

    return vacancies_found, salaries


def get_vacancies_for_headhunter(languages):

    vacancies = {}

    for language in languages:

        vacancies_found, salaries = get_vacancies_for_language(
            language)

        if salaries:
            average_salary = int(mean(salaries))
        else:
            average_salary = 0

        vacancies[language] = {
            "vacancies_found": vacancies_found,
            "vacancies_processed": len(salaries),
            "average_salary": average_salary
        }

    return vacancies
