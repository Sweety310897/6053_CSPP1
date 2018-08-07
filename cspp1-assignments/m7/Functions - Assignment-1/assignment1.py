'''This is main pgm'''
# Functions | Assignment-1 - Paying Debt off in a Year
# Write a program to calculate the credit card balance
# after one year if a person only pays the minimum monthly payment required by the
# credit card company each month.
# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal
# monthlyPaymentRate - minimum monthly payment rate as a decimal
# For each month, calculate statements on the monthly paymen
#t and remaining balance.
#At the end of 12 months, print out the remaining
# balance. Be sure to print out no more than two decimal digits of accuracy - so print
# Remaining balance: 813.41
# instead of
# Remaining balance: 813.4141998135
# So your program only prints out one thing:
#the remaining balance at the end of the year in the format:
# Remaining balance: 4784.0
# A summary of the required math is found below:
# Monthly interest rate= (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
# Updated balance each month = (Monthly unpaid balance) +
#(Monthly interest rate x Monthly unpaid balance)
def payingdebtoffina_year(balanc_e, annualinterest_rate, monthlypayment_rate):
    ''' This function is to calculate remaining bal'''
    i = 0
    while i < 12:
        balanc_e = balanc_e - (monthlypayment_rate * balanc_e)
        balanc_e = balanc_e + (annualinterest_rate / 12) * balanc_e
        i += 1
    return round(balanc_e, 2)
def main():
    ''' This is main function'''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print('Remaining balance', payingdebtoffina_year(data[0], data[1], data[2]))
if __name__ == "__main__":
    main()
