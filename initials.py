def initials():


    name = input('Type your name and press ENTER. ')
    name_list = name.split()

    first = name_list[0][0]
    second = name_list[1][0]
    last = name_list[2][0]

    print(first.upper() + '.' + second.upper() +'.' + last.upper()) 


initials()