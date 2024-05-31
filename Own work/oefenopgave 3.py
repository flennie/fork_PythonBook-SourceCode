x = 14
print('x')
print(x)
print(x + 1)
print("x + 1")
print(x + 1.0)

#
a= (8 / (2 ** 5)) + 3
print('a ', a)

b=100 +( 20 // 6) - (5 * 3)
print ('b ', b)

c=((256 / 8) / 4) + (28 / 7)
print('c ', c)

d=(40 / 8) *( 3 ** 2)
print('d ', d)

e=(40 // 8) * (3 ** 2)
print('e ', e)

## deel 4
aantal = 50
prijs= 19.95
korting = 0.42
verzending=4
volgende =0.8

bruto=aantal*prijs
print('bruto kosten bestelling : ', bruto)
bestelling = aantal * prijs * (1-korting)
print('bestelling met korting: ', bestelling)
prijsverzending = (verzending + (aantal-1)*volgende)+bestelling
print('bestelling incl korting en verzending:', prijsverzending)


