import requests
from statistics import mean

from predict_salary import predict_rub_salary


def get_sj_salary(vacancy, salaries):

    if vacancy['currency'] == "rub":

        payment_from = vacancy['payment_from']
        payment_to = vacancy['payment_to']
        salary = predict_rub_salary(payment_from, payment_to)

        return salary


def get_vacancies_for_one_language(language, sj_url, headers):

    params = {
        "keyword": f"Программист {language}",
        "town": 4, #id Москвы у SuperJob API
        "count": 100
    }
    salaries = []

    response = requests.get(sj_url, params=params, headers=headers)
    response.raise_for_status()
    response_json = response.json()
    objects = response_json['objects']

    for vacancy in objects:
        salary = get_sj_salary(vacancy, salaries)
        if salary:
            salaries.append(salary)

    vacancies_found = response_json['total']

    return vacancies_found, salaries


def get_vacancies_for_superjob(sj_token, languages):

    sj_url = "https://api.superjob.ru/2.0/vacancies/"

    vacancies = {}

    headers = {
        "X-Api-App-Id": sj_token
    }

    for language in languages:

        vacancies_found, salaries = get_vacancies_for_one_language(language, sj_url, headers)

        for vacancy in objects:
            salary = get_sj_salary(vacancy, salaries)
            if salary:
                salaries.append(salary)

        vacancies[language] = {
            "vacancies_found": vacancies_found,
            "vacancies_processed": len(salaries),
            "average_salary": int(mean(salaries))
        }

    return vacancies
