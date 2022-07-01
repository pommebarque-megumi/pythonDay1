import random
num = random.randint(1,100)
maxCount=5
print('1~100までの数字をひとつ選んだよ')
print('その数字を',maxCount,'回以内に当ててね')
for i in range(1,maxCount+1):
    print(i,'回目です。いくつかな？')
    ans = int(input())
    if ans == num:
        print('正解！')
        break
    elif i == maxCount:
        pass
    elif ans>num:
        print('もっと下だよ')
    else:
        print('もっと上だよ')
else:
    print('残念！正解は',num,'でした')
