# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成
#
# 例子
# 给定 nums = [0,0,1,1,1,2,2,3,3,4],
#
# 函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
#
# 你不需要考虑数组中超出新长度后面的元素。



nums = [0,0,1,1,1,2,2,3,3,4,5, 11, 11, 28,28,30,33,33,33,33]

# 自己的思路
def custom_delDuplicates(nums):

    index = 1
    tempValue = nums[0];
    repIndex = -1
    count = len(nums)

    for index in range(index, count):
        value = nums[index]
        if value == tempValue:
            if repIndex == -1:
                repIndex = index
        elif value != tempValue and repIndex != -1:
            nums[repIndex] = value
            repIndex += 1
            tempValue = value

    return repIndex

# 答案
def delDuplicates(nums):
    if len(nums) == 0 :
        return  0

    pre = 0
    cur = 0
    count = len(nums)

    while cur < count :
        if nums[pre] == nums[cur]:
            cur += 1
        else:
            pre += 1
            nums[pre] = nums[cur]
            cur += 1

    return pre+1


# 练习
def delteNums(nums):
    pre = 0;
    cur = 0;
    count = len(nums);

    while cur < count:

        if nums[pre] == nums[cur]:
            cur += 1;
        else:
            pre += 1;
            nums[pre] = nums[cur];
            cur += 1

    return pre+1


def test():
    ret = delteNums(nums)
    # ret = delDuplicates(nums)

    for value in nums:
        print(value)

    print('len =', ret)

test()


































