import requests
from statistics import mean


def predict_rub_salary_for_headhunter(payment_from, payment_to):

    if payment_from and not payment_to:
        salary_from_the_vacancy = payment_from*1.2
    elif payment_to and not payment_from:
        salary_from_the_vacancy = payment_to*0.8
    elif payment_to and payment_from:
        salary_from_the_vacancy = (payment_from + payment_to)/2

    return salary_from_the_vacancy


def get_hh_salary(item, salaries):

    salary = item['salary']

    if salary and salary['currency'] == "RUR":
        payment_from = salary['from']
        payment_to = salary['to']
        predict_salary = predict_rub_salary_for_headhunter(payment_from, payment_to)
        return predict_salary


def get_vacancies_for_headhunter(hh_url, languages):

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
