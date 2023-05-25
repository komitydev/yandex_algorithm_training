orig = input().rstrip().split()

operators = "+-*"

nums = []

for o in orig:
    if o not in operators:
        nums.append(int(o))
    else:
        if o == '+':
            res = nums[-2] + nums[-1]
        if o == '-':
            res = nums[-2] - nums[-1]
        if o == '*':
            res = nums[-2] * nums[-1]
        del nums[-1]
        del nums[-1]
        nums.append(res)        

print(nums[0])
