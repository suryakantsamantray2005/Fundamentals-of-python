#Write a program to add two lists index-wise. Create a new
#list that contains the 0th index item from both the list,
#then the 1st index item, and so on till the last element. 
#any leftover items will get added at the end of the new list.
list1 = ["M", "na", "i", "Kh"]
list2 = ["y", "me", "s", "an"]
L=[]
j=-1
for i in list1:
    j=j+1
    a=i+list2[j]
    print(a)