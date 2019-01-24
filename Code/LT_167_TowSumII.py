



def towSum(nums, target):

    left = 0
    right = len(nums) - 1

    while left != right :
        temp = nums[left] + nums[right]
        if temp == target :
            return [left, right]

        if temp > target :
            right -= 1
        else:
            left += 1

    return [0, 0]





def test():

    nums = [1, 5, 9, 11, 20, 41];
    target = 42
    index = towSum(nums, target)

    print(index[0], index[1]);


test()


