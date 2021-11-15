
vows = ['у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю', 'ё']
cons = ['й', 'ц', 'к', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ', 'ф', 'в', 'п', 'р', 'л', 'д', 'ж', 'ч', 'с', 'м', 'т', 'ь', 'б']


def vowels(string):
    summ_vows = 0
    summ_cons = 0
    string = string.lower()
    for vow in string:
        if vow in vows:
            summ_vows += 1
        
        else:
            summ_cons += 1
    
            


    print('vows: ', summ_vows, 'cons:', summ_cons)
    return ''

print(vowels(input()))