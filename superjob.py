import requests
from statistics import mean

from predict_salary import predict_rub_salary


def get_sj_salary(vacancy, salaries):

    if vacancy['currency'] == "rub":

        payment_from = vacancy['payment_from']
        payment_to = vacancy['payment_to']
        salary = predict_rub_salary(payment_from, payment_to)

        return salary


def get_vacancies_for_language(language, headers):

    sj_url = "https://api.superjob.ru/2.0/vacancies/"
    params = {
        "keyword": f"Программист {language}",
        "town": 4,  # id Москвы у SuperJob API
        "count": 100
    }
    salaries = []

    page = 0
    pages = 1

    while page < pages:

        response = requests.get(sj_url, params=params, headers=headers)
        vacancies_info = response.json()

        pages = (vacancies_info["total"]//100)+1
        page = page+1
        params["page"] = page
        objects = vacancies_info['objects']

        for vacancy in objects:
            salary = get_sj_salary(vacancy, salaries)
            if salary:
                salaries.append(salary)

    vacancies_found = vacancies_info['total']

    return vacancies_found, salaries


def get_vacancies_for_superjob(sj_token, languages):

    vacancies = {}

    headers = {
        "X-Api-App-Id": sj_token
    }

    for language in languages:

        vacancies_found, salaries = get_vacancies_for_language(
            language, headers)

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
