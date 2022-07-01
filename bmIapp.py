height=input('身長を入力してください(cm)')
weight=input('体重を入力してください(kg)')
height=float(height)/100 #height=160...160.0/100=1.6#
weight=float(weight)
bmi = weight/(height*height)
print('BMI:',bmi)
bodyType=''
if bmi>25:
    bodyType='肥満'
elif bmi>18.5:
    bodyType='標準'
else:
    bodyType='痩せ型'
print(bodyType)
