import os

from dotenv import load_dotenv
from terminaltables import SingleTable

from superjob import get_vacancies_for_superjob
from headhunter import get_vacancies_for_headhunter


def print_table(vacancies, title, languages):

    table_data = [
        (
            'Язык программирования',
            'Вакансий найдено',
            'Вакансий обработано',
            'Средняя зарплата'
        )
    ]

    for language in languages:

        table_data.append(
            (
                language,
                vacancies[language]['vacancies_found'],
                vacancies[language]['vacancies_processed'],
                vacancies[language]['average_salary']
            )
        )

    table = SingleTable(table_data, title)

    print(table.table)


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

    sj_title = "SuperJob Moscow"
    hh_title = "HeadHunter Moscow"

    hh_vacancies = get_vacancies_for_headhunter(languages)
    sj_vacancies = get_vacancies_for_superjob(sj_token, languages)

    print_table(hh_vacancies, hh_title, languages)
    print_table(sj_vacancies, sj_title, languages)
