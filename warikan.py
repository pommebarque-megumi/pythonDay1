price=input('料金を入力')
number=input('人数を入力')
print(type(price))
payment = int(price)/int(number)
print(f'お支払いは{payment:.0f}円です')
#JS `お支払いは${payment}です`
