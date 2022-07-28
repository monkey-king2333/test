i = 1
while i != 0:
    print('''现在有4种模式
         1.一元二次方程求根
         2.海伦公式
         3.增长率问题
         4.a的b次方
         0.退出
         
                                                                                           by :sao猴子（sml）''')
    xx = int(input('请输入模式'))
    if xx == 1 :
        a = float(input('输入a的值'))
        b = float(input('输入b的值'))
        c = float(input('输入c的值'))
        de = (b ** 2 - 4 * a * c)
        print(de)
        answer_1 = ((-1 * b + de ** 0.5) / 2 * a)
        answer_2 = ((-1 * b - de ** 0.5) / 2 * a)
        print(answer_1)
        print(answer_2)
    elif xx == 2:
        a = float(input('输入a的值'))
        b = float(input('输入b的值'))
        c = float(input('输入c的值'))
        p = (a+b+c)/2
        S = (p*(p-a)*(p-b)*(p-c))**0.5
        print(S)
    elif xx == 3:
        a = float(input('请输入原量'))
        b = float(input('请输入增长率（小数）'))
        c = float(input('输入增长次数'))
        answer = a*(1+b)**c
    elif xx == 4:
        a = float(input('输入a'))
        b = float(input('输入b'))
        print(a**b)
    elif xx == 0:
        print('''感谢使用
              by；sao猴子（sml）''')
        i=0
    else:
        print('请检查输入是否正确')