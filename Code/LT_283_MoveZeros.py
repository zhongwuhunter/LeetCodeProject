

# 空间n, 时间n
def moveZeros1(nums):
    res = []
    count = 0
    for i in range(len(nums)):
        if nums[i] == 0 :
            count += 1;
        else:
            res.append(nums[i])

    for i in range(count):
        res.append(0)


    return res


# 时间复杂度: O(n),  空间复杂度: O(1)
def moveZeros2(nums):
    k = 0
    for index in range(len(nums)):
        val = nums[index]
        if 0 != val :
            nums[k] = nums[index]
            k += 1

    for i in range(k, len(nums)) :
        nums[i] = 0

    return nums




def test():
    nums = [ 0, 1, 0 , 2, 11, 0 , 6, 0 , 5]

    res = moveZeros2(nums);

    for val in res :
        print(val)

test()





































