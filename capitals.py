import random

d = {
    'Netherlands' : 'Amsterdam',
    'Italy' : 'Rome',
    'Spain' : 'Madrid',
    'China' : 'Beijing',
    'Japan' : 'Tokyo',
    'Russia' : 'Moscow',
    'US' : 'Washington DC',
    'Great Britain' : 'London',
    'France' : 'Paris',
    'Portugal' : 'Lisbon',
    'Chile' : 'Santiago' 
}
r = 0
w = 0
k = random.choice(list(d.keys()))
print(k)
city = input()
while city != 'stop':

    if city == d[k]:
        r += 1
        k = random.choice(list(d.keys()))
        print(k)
        city = input()
    else:
        w += 1
        k = random.choice(list(d.keys()))
        print(k)
        city = input()
        
print('right answers:', r, 'wrong answers:', w)