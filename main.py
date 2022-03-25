import os

from dotenv import load_dotenv
from terminaltables import SingleTable

from superjob import get_vacancies_for_superjob
from headhunter import get_vacancies_for_headhunter


def get_table(sj_vacancies, hh_vacancies, languages):

    title = "HeadHunter and SuperJob Moscow"

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
                f"sj_{language}",
                sj_vacancies[language]['vacancies_found'],
                sj_vacancies[language]['vacancies_processed'],
                sj_vacancies[language]['average_salary']
            )
        )

        table_data.append(
            (
                f"hh_{language}",
                hh_vacancies[language]['vacancies_found'],
                hh_vacancies[language]['vacancies_processed'],
                hh_vacancies[language]['average_salary']
            )
        )

    table = SingleTable(table_data, title)

    return table.table


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
    table = get_table(sj_vacancies, hh_vacancies, languages)

    print(table)
