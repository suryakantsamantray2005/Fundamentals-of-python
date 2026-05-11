#we have to store frequency of the given number in dictionary
nums=[5,6,7,7,1,9,111,1,1,5,1,1]
freq_map={}
for i in range(0,len(nums)):
    if nums[i] in freq_map:
        freq_map[nums[i]]=freq_map[nums[i]]+1
    else:
        freq_map[nums[i]]=1
print(freq_map)
#method 2
for i in range(0,len(nums)):
    freq_map[nums[i]]=freq_map.get(nums[i], 0) + 1
print(freq_map)