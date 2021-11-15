def loshu(lisst):
    for i in lisst:
        for j in lisst:
            d1 = lisst[0][0] + lisst[1][1] + lisst[2][2]
            d2 = lisst[0][2] + lisst[1][1] + lisst[2][0]
            x1 = sum(lisst[0]) 
            x2 = sum(lisst[1])
            x3 = sum(lisst[2])
            y1 = lisst[0][0] + lisst[1][0] + lisst[2][0]
            y2 = lisst[0][1] + lisst[1][1] + lisst[2][1]
            y3 = lisst[0][2] + lisst[1][2] + lisst[2][2]
           
    if d1 == d2 == x1 == x2 == x3 == y1 == y2 == y3:
        return 'it is a Lo Shu square!'
    else:
        return 'it is not a Lo Shu square'


                
           
print(loshu([[4,9,2], [3,5,7], [8,1,6]]))