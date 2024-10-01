def withdraw(balance, money):
    print("새로운 계좌를 개설합니다.")
    print("{}원을 출금했습니다. 잔액은 {}원입니다." .format(money, balance-money))

withdraw(1000, 500)