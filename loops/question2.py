#finding the in-hand salary after deductions of taxes and hra -10%,da-5%,pf-3%
#tax slab below 5lakhs-0%,5-10 lakhs-10%,10-20 lakhs-20%,above 20 lakhs-30%
#taking the salary input from the user
a=int(input('enter your salary '))
if a<=500000:
    ihs=a-0.1*a-0.05*a-0.03*a
    print('your in hand salary is ',ihs)
elif a>500000 and a<=1000000:
    ihs1=a-0.2*a-0.05*a-0.03*a
    print('your in hand salary is ',ihs1)
elif a>1000000 and a<=2000000:
    ihs2=a-0.3*a-0.05*a-0.03*a
    print('your in hand salary is ',ihs2)
else:
    ihs3=a-0.4*a-0.05*a-0.03*a
    print('your in hand salary is ',ihs3)