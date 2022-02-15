import os

from dotenv import load_dotenv
from terminaltables import SingleTable

from superjob import get_vacancies_for_superjob
from headhunter import get_vacancies_for_headhunter


def get_tables(sj_vacancies, hh_vacancies, languages):

    hh_title = "HeadHunter Moscow"
    sj_title = "SuperJob Moscow"

    sj_table_data = [
        (
            'Язык программирования',
            'Вакансий найдено',
            'Вакансий обработано',
            'Средняя зарплата'
        )
    ]

    hh_table_data = [
        (
            'Язык программирования',
            'Вакансий найдено',
            'Вакансий обработано',
            'Средняя зарплата'
        )
    ]

    for language in languages:

        sj_table_data.append(
            (
                language,
                sj_vacancies[language]['vacancies_found'],
                sj_vacancies[language]['vacancies_processed'],
                sj_vacancies[language]['average_salary']
            )
        )

        hh_table_data.append(
            (
                language,
                hh_vacancies[language]['vacancies_found'],
                hh_vacancies[language]['vacancies_processed'],
                hh_vacancies[language]['average_salary']
            )
        )

    sj_table = SingleTable(sj_table_data, sj_title)
    hh_table = SingleTable(hh_table_data, hh_title)

    return sj_table.table, hh_table.table


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

    hh_vacancies = get_vacancies_for_headhunter(languages)
    sj_vacancies = get_vacancies_for_superjob(sj_token, languages)
    sj_table, hh_table = get_tables(sj_vacancies, hh_vacancies, languages)

    print(sj_table)
    print(hh_table)
