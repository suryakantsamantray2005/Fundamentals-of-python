#Write a program, which will find all such numbers between 1000 and 3000 (both included)
#  such that each digit of the number is an even number. The numbers obtained
#  should be printed in a space-separated sequence on a single line.
for i in range(1000,3201):
    a=i
    b=a%10
    a=a//10
    c=a%10
    a=a//10
    d=a%10
    a=a//10
    e=a%10
    if b%2==0 and c%2==0 and d%2==0 and e%2==0:
        print(i,end=' ')