# Maimuna Murad
# 2065973

print('Birthday Calculator\nCurrent day')
m1 = int(input('Month: '))
d1 = int(input('Day: '))
y1 = int(input('Year: '))
print('Birthday')
m2 = int(input('Month: '))
d2 = int(input('Day: '))
y2 = int(input('Year: '))
years = y1-y2-1
if(m2<m1):
    years+=1
elif(m1==m2):
    if(d2<d1):
        years+=1
if(m1==m2 and d1==d2):#printing happy Birthday if current day is his birthda
    print('Happy Birthay')
print('You are '+str(years)+" years old.")