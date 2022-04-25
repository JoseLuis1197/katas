def solution(roman):
    nums = []
    ans = 0
    for char in roman:
        if char == 'M':
            nums.append(1000)
        elif char == 'D':
            nums.append(500)
        elif char == 'C':
            nums.append(100)
        elif char == 'L':
            nums.append(50)
        elif char == 'X':
            nums.append(10)
        elif char == 'V':
            nums.append(5)
        elif char == 'I':
            nums.append(1)
    for i, n in enumerate(nums[:-1]):
        if n >= nums[i + 1]:
            ans += n
        else:
            ans -= n
    return ans + nums[-1]