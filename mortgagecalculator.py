#====================================
#Hassan El-Haddad
#Lab3
#Mortage Calculator
#2/17/20
#=====================================





#Asking user to enter the loan amount.
loanamount= float(input("Enter the loan amount:\n"))
#Asking the user to enter how many years for the loan.
loanyears= int(input("Enter how many years to repay the loan:\n"))
#Asking the user to input the interest rate.
interestrate= float(input("Enter the yearly interest rate for the loan:\n"))

#Formula for monthly interest rate.
monthlyrate= interestrate/12/100
#Number of payments of the life of the loan.
numberofpayments= loanyears*12

#Formula for monthly payments for the loan.
paymentamount= loanamount * (monthlyrate +monthlyrate / ((1 + monthlyrate) ** (numberofpayments) -1))
#Rounding the payment amount to two decimal places.
paymentamount = round(paymentamount, 2)
print(paymentamount)

#Asking the user if the calculations are finished, if not calculate again.
monthlybalance=1
while monthlybalance:
    done= input("Are you sure you want to exit? yes/no:\n")
    if done =="no":
        loanamount= float(input("Enter the loan amount:\n"))
        loanyears= int(input("Enter how many years to repay the loan:\n"))
        interestrate= float(input("Enter the yearly interest rate for the loan:\n"))
        monthlyrate= interestrate/12/100
        numberofpayments= loanyears*12
        paymentamount= loanamount * (monthlyrate +monthlyrate / ((1 + monthlyrate) ** (numberofpayments) -1))
        paymentamount = round(paymentamount, 2)
        print(paymentamount)
    
    elif done== "yes":
#The user did not want to make another calculation, so the program is closing.
        print("Thank you for using the loan payment calculator.")
        break
    else:
        print()
