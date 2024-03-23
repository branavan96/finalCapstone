# this is a interest calculator for bond(mortgage) and simple/compound interest on an investment.

import math

while True:
    print("""
investment - to calculate the amount of interest you'll earn on your investment
bond - to calculate the amount you'll have to pay on a home loan""")
    selection = input("""Enter either 'investment' or 'bond' from the menu above to proceed:
                     type in exit to terminate: """).strip().lower()

    if selection == 'investment':
  
    # amount deposited, interest rate, years of investment
    # P = the amount deposited
      P = float(input("Please enter the amount you would like to deposit : "))

    # interest = the amount of interest
      interest = int(input("Please enter the amount of interest : "))

    # r = rate of interest (%)
      r = float(interest)/100
    
    # t = amount of years of investment
      t = int(input("Please enter the years for investment : "))

      calculation_selection = input("Please select either simple or compound interest : ").strip().lower()

      if calculation_selection == 'simple':
      # A = total amount once the interest has been applied for simple interest
        A = round(P*(1+r*t),2)
        print(A)
        print(" with simple interest, your interest(plus deposit) after ", t, " years on an initial deposit of £", P, " is £",A)
        continue

      elif calculation_selection == 'compound':
      # A = total amount once the interest has been applied for compound interest
        A = round(P*math.pow((1+r),t),2)
        print(A)
        print(" with compound interest, your interest (plus deposit) after ", t, " years on an initial deposit of £", P, " is £",A)
        continue
      
      else:
         print("Invalid selection")
         continue
    
    elif selection == 'bond':
       
     # present value of house, interest rate, monthly rate interest, years of investment
     # P = the present value of the house
       P = float(input("Enter the present value of your house : "))

     # interest = the amount of interest
       interest = int(input("Please enter the amount of interest : "))

     # r = rate of interest (%)
       r = float(interest)/100
       
     # i = the monthly rate interest
       i = r/12

     # t = amount of years of investment
       t = int(input("Please enter the amount of months planned for repayment : "))

     # A = the bond repayment formula
       A = round(((i*P)/(1-(1+i)**(-t))),2)

       print("The monthly repayments on your house over" ,t,"months is £",A)
       continue
    
    elif selection == 'exit':
       print("Exiting. . . ")
       break

    else:
       print('Invalid input')

# If we ask the user to input the selection as investment, 
# the amount of money they are depositing as £25,000, 
# the amount of interest as 8% and the years for investment as 20, 
# we ask them to choose 'simple' or compound as the type of interest.
# If the user chose 'simple', the total amount is £65000.
# If the user chose 'compound', the total amount s £116523.93.
# There is a difference when we choose a different type of interest.

# If we ask the user to input the selection as 'bond',
# the present value of house as £100000,
# the interest rate as 7% and the amount of months planned for repayment as 120,
# the monthly repayments on the house would be £1161.08.