import requests
from statistics import mean


def predict_rub_salary_for_SuperJob(vacancy):

    if vacancy['payment_from'] and not vacancy['payment_to']:
        salary_from_the_vacancy = vacancy['payment_from']*1.2
    elif vacancy['payment_to'] and not vacancy['payment_from']:
        salary_from_the_vacancy = vacancy['payment_to']*0.8
    elif not vacancy['payment_from'] and not vacancy['payment_to']:
        salary_from_the_vacancy = None
    else:
        salary_from_the_vacancy = vacancy['payment_from']

    return salary_from_the_vacancy


def get_vacancies_for_SuperJob(sj_url, sj_token, languages):

    vacancies = {}

    headers = {
        "X-Api-App-Id": sj_token
    }

    for language in languages:

        params = {
            "keyword": f"Программист {language}",
            "town": 4,
            "count": 100
        }
        salaries = []

        response = requests.get(sj_url, params=params, headers=headers)
        response.raise_for_status()
        for vacancy in response.json()['objects']:
            if vacancy['currency'] == "rub":
                predict_salary = predict_rub_salary_for_SuperJob(vacancy)
                if predict_salary != None:
                    salaries.append(predict_salary)

        vacancies[language] = {
            "vacancies_found": response.json()['total'],
            "vacancies_processed": len(salaries),
            "average_salary": int(mean(salaries))
        }

    return(vacancies)
