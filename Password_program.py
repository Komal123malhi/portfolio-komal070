
print('\tWelcome to ATM')
customerId = int(input('Enter Your CustomerId\n'))


if customerId == 1234:
    print('\n\tWecome Sandeep')
    password = int(input('Enter Your Password/Pin\n'))
    if password == 2222:
        print('\tLogin Successfully')
        print('Your Account Balance : $1000')
    else:
        print('Your Entered wrong Password')
elif customerId == 5678:
     print('\n\tWecome Gagan')
     password = int(input('Enter Your Password/Pin\n'))
     if password == 3333:
         print('\n\tLogin Successfully')
         print('Your Account Balance : $1000')
     else:
        print('Your Entered wrong Password')
else:
    print('Your Entered wrong CustomerId')