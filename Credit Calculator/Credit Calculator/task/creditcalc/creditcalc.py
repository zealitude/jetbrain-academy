
import sys, math

def get_number(options, key):
    n = float(get_parameter(options, key))
    if n <= 0:
        raise
    return n

def get_parameter(options, key):
    if key in options:
        payment_type = options[key]
        # print(payment_type)
        return payment_type
    else:
        raise

def differentiated_payments(options):
    p = get_number(options, '--principal')
    n = get_number(options, '--periods')
    interest = get_number(options, '--interest')
    i = interest / (12 * 100)

    overpay = 0
    for m in range(1, int(n) + 1):
        d = p / n + i * (p - (p * (m - 1)) / n)
        d = math.ceil(d)
        overpay += d - (p / n)
        print("Month {}: paid out {}".format(m, d))
    print()
    print("Overpayment = {}".format(int(overpay)))


def get_credit_principal(payment, i, m):
    return  math.floor(payment / ((i * (1 + i) ** m) / ((1 + i) ** m - 1)))

def get_count_of_months(payment, p, i):
    return math.ceil(math.log((payment / (payment - i * p)), i + 1))

def get_annuity_monthly_payment(p, m, i):
    return math.ceil(p * (i * (1 + i) ** m) / ((1 + i) ** m - 1))

def annuity_payments(options):
    overpay = 0

    payment = get_number(options, '--payment') if '--payment' in options else None
    i = get_number(options, '--interest') / (12 * 100) if '--interest' in options else None
    p = get_number(options, '--principal')     if '--principal' in options else None
    m = get_number(options, '--periods')     if '--periods' in options else None

    if p and m and i:
        annuity_monthly_payment = get_annuity_monthly_payment(p, m, i)
        print("Your annuity payment = {}!".format(annuity_monthly_payment))
        overpay = (annuity_monthly_payment * m) - p

    elif payment and p and i:
        n = get_count_of_months(payment, p, i)
        year = n // 12
        month = n % 12
        if year > 0:
            period_str = str(year) + ' years' if year > 1 else ' year'
        if month > 0:
            if year > 0:
                period_str += ' and '
            period_str += str(month) + ' months' if month > 1 else ' month'
        print("You need {} to repay this credit!".format(period_str))
        overpay = (payment * n) - p

    elif payment and m and i:
        credit_principal = get_credit_principal(payment, i, m)
        print("Your credit principal = {}!".format(credit_principal))
        overpay = (payment * m) - credit_principal

    else:
        raise

    print("Overpayment = {}".format(int(overpay)))

options = {}
for arg in sys.argv[1:]:
    key, value = arg.split('=')
    options[key] = value

try:
    if len(options) == 4:
        payment_type = get_parameter(options, '--type')
        if payment_type == "annuity":
            annuity_payments(options)
        elif payment_type == "diff":
            differentiated_payments(options)
    else:
        raise
except Exception:
    print("Incorrect parameters")


