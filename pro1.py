try:
    y=0
    a = int(input('vvedite A: '))
    b = int(input('vvedite B: '))
    x = int(input('vvedite X: '))
    d = int(input('vvedite D:'))
    c = int(input('vvedite C:'))
    try:
        if x > 5:
            y = (x**2)+5
        elif x <= 5:
            y = (a**2)*(c+(b**2))-d
        print('y=', y)
    except:
        print('net vernogo resheniya')
except:
    print('nevernye vxodnye dannie')
