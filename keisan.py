a=10
b=3
ans=a+b
print(a,'+',b,'=',ans)
ans=a-b
print(a,'-',b,'=',ans)
ans=a*b
print(a,'*',b,'=',ans)
ans=a/b
print(a,'/',b,'=',ans)
ans=a//b
print(a,'/',b,'=',ans)
ans=a%b
print(a,'/',b,'=',ans)
ans='Hello'*3
print(ans)

a='ねこ'
x=10
x=x+100
print(x)#110

y=type(a)(x)
print(type(y))
print(type(x))

print(isinstance(x,int))#true
print(isinstance(x,str))#false
print(type('hello')is str)#true
print(type('hello')is int)#false

if x>0 :
    print('x=正の数です')

score=64

if score>80:
    print('Excelent')
elif score>60:
    print('Good')
elif score>40:
    print('normal')
else:
    print('Bad')

n=0
while n<10:
    print(n)
    n=n+1
print('終了')

for i in range(5):
    print(i)

for i in range(1,11):
    print(i,end=' ')
print()

for i in range(1,4):
    for j in range(1,11):
        print(i*j,end=" ")
    print()
print(type(a))
