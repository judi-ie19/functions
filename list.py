from ast import Continue


nums=[1,2,3,4,5,6]
for num in nums:
    if num==3:
        print('found!')
        Continue
    print (num)