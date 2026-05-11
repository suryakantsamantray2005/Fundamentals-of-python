#finding the median of the numbers in list 
nums1 = list(map(int, input("Enter elements nums1: ").split()))
nums2 = list(map(int, input("Enter elements nums2: ").split()))
M=nums1+nums2
M.sort()
if len(M)%2!=0:
    a=M[len(M)//2]
    print('median is ',a)
else:
    b=M[len(M)//2]
    c=M[len(M)//2 - 1]
    print('median is ',(b+c)/2)