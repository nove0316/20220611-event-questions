for num in range(1, 101):
    string = ''
    
    # 3の倍数　かつ　5の倍数
    if num % 3 == 0 and num % 5 == 0:
        string = 'FizzBuzz'

    # 3の倍数　かつ　5の倍数でない
    elif num % 3 == 0:
        string = 'Fizz'

    # 3の倍数でない　かつ 5の倍数
    elif num % 5 == 0:
        string = 'Buzz'

    # 3の倍数でない かつ 5の倍数でない
    else:
        string = num

    print(string)
