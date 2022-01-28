import requests
from statistics import mean


def predict_rub_salary_for_headhunter(salary):

    if salary['from'] and not salary['to']:
        salary_from_the_vacancy = salary['from']*1.2
    elif salary['to'] and not salary['from']:
        salary_from_the_vacancy = salary['to']*0.8
    else:
        salary_from_the_vacancy = salary['from']

    return salary_from_the_vacancy


def get_vacancies_for_headhunter(hh_url, languages):

    vacancies = {}

    for language in languages:

        params = {
            "text": f"Программист {language}",
            "area": "1",
            "per_page": "100"
            }

        response = requests.get(hh_url, params)
        salaries = []

        for item in response.json()['items']:
            salary = item['salary']

            if salary and salary['currency'] == "RUR":
                predict_salary = predict_rub_salary_for_headhunter(salary)
                salaries.append(predict_salary)
            else:
                print(None)

        vacancies[language] = {
            "vacancies_found": response.json()['found'],
            "vacancies_processed": len(salaries),
            "average_salary": int(mean(salaries))
        }

    return(vacancies)
