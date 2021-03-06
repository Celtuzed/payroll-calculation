# Сравниваем вакансии программистов

Этот код нужен для сравнивания вакансий программистов по зарплатам и с удобным выводом в виде таблицы.

### Как установить

Python3 должен быть уже установлен.
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
  pip install -r requirements.txt
```

### SuperJob

Для использования данной платформы вам потребуется получить токен на [данном сайте](https://api.superjob.ru/).
Для использования токена нужно будет создать `.env` файл и по примеру ввести токен.
```
SJ_TOKEN=ВАШ_ТОКЕН
```

### Использование

Для запуска скрипта нужно ввести:

```
python main.py
```

Данный скрипт выводит зарплаты программистов на разных языках программирования в Москве.
Зарплаты рассчитаны исходя из вакансий взятых с сервисов HeadHunter и SuperJob.

| Язык программирования | Вакансий найдено | Вакансий обработано | Средняя зарплата |
|:---------------------:|:----------------:|:-------------------:|:----------------:|
|          C++          |        40        |         25          |       172000     |
|         python        |        66        |         40          |       130000     |

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
