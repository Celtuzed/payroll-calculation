def predict_rub_salary(payment_from, payment_to):

    if payment_from and payment_to:
        return (payment_from + payment_to)/2

    elif not payment_to:
        return payment_from*1.2

    elif not payment_from:
        return payment_to*0.8
