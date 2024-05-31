
ccy = input('which ccy you want to convert into EUROs?')

amount=float(input('What amount do you like to convert : '))
rate = float(input('What is the conversion rate to EUR : '))

print('You like to convert the currency: ' , ccy , ' to EUR')
euro=amount/rate;
print('Converting ', amount, ' with conversion rate of ', rate, ' amounts to ', euro, ' EUROs')
