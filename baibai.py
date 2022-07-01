n=1
minute=0
days=1
daysMin=days*60*24

while minute < daysMin:
    n *= 2
    minute += 5
    print(minute,'分後',n,'個')
