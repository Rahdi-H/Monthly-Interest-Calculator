def main():
    print('Monthly Interest Rate Calculator \n')

    principal = float(input("Enter the principal amount: "))
    air = float(input('Enter the Interest Rate: '))
    number_of_years = int(input('Enter the number of years you have for paying: '))

    monthly_interest_rate = air / 1200
    amount_of_months = number_of_years * 12
    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-amount_of_months))
    
    print('you have to pay monthly : ', monthly_payment)

main()