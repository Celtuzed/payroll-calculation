def predict_rub_salary(payment_from, payment_to):

    if payment_from and payment_to:
        salary_from_the_vacancy = (payment_from + payment_to)/2
        return salary_from_the_vacancy

    elif payment_from and not payment_to:
        salary_from_the_vacancy = payment_from*1.2
        return salary_from_the_vacancy

    elif payment_to and not payment_from:
        salary_from_the_vacancy = payment_to*0.8
        return salary_from_the_vacancy
