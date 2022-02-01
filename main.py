import os

from dotenv import load_dotenv
from terminaltables import SingleTable

from superjob import get_vacancies_for_superjob
from headhunter import get_vacancies_for_headhunter


def get_sj_table(sj_vacancies, languages):

    sj_table_data = [
        (
            'Язык программирования',
            'Вакансий найдено',
            'Вакансий обработано',
            'Средняя зарплата'
        )
    ]

    sj_title = "SuperJob Moscow"

    for language in languages:
        sj_table_data.append(
            (
                language,
                sj_vacancies[language]['vacancies_found'],
                sj_vacancies[language]['vacancies_processed'],
                sj_vacancies[language]['average_salary']
            )
        )

    sj_table = SingleTable(sj_table_data, sj_title)
    return sj_table.table


def get_hh_table(hh_vacancies, languages):

    hh_table_data = [
        (
            'Язык программирования',
            'Вакансий найдено',
            'Вакансий обработано',
            'Средняя зарплата'
        )
    ]
    hh_title = "HeadHunter Moscow"

    for language in languages:
        hh_table_data.append(
            (
                language,
                hh_vacancies[language]['vacancies_found'],
                hh_vacancies[language]['vacancies_processed'],
                hh_vacancies[language]['average_salary']
            )
        )

    hh_table = SingleTable(hh_table_data, hh_title)
    return hh_table.table


if __name__ == '__main__':
    load_dotenv()

    languages = [
        "Java",
        "JavaScript",
        "Python",
        "C++",
        "Swift",
        "TypeScript",
        "Ruby",
        "PHP",
        "C#"
    ]

    sj_token = os.getenv('SJ_TOKEN')
    sj_url = "https://api.superjob.ru/2.0/vacancies/"
    hh_url = "https://api.hh.ru/vacancies"

    hh_vacancies = get_vacancies_for_headhunter(hh_url, languages)
    sj_vacancies = get_vacancies_for_superjob(sj_url, sj_token, languages)
    hh_table = get_hh_table(hh_vacancies, languages)
    sj_table = get_sj_table(sj_vacancies, languages)

    print(sj_table)
    print(hh_table)
