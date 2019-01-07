#
# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
#
# 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
#
# 注意:
# 不能使用代码库中的排序函数来解决这道题。
#
# 示例:
#
# 输入: [2,0,2,1,1,0]
#
# 输出: [0,0,1,1,2,2]

# // 三路快速排序的思想
#  2// 对整个数组只遍历了一遍
#  3// 时间复杂度: O(n)
#  4// 空间复杂度: O(1)


def sortColors(nums):
    zero = -1
    tow = len(nums)
    i = 0
    while i < tow :
        if (nums[i] == 1):
            i += 1
        elif nums[i] == 2:
            tow -= 1
            swap(nums, i, tow)
        else:
            zero += 1
            swap(nums, zero, i)
            i += 1




def swap(nums, i, j):
    tempNum = nums[i]
    nums[i] = nums[j]
    nums[j] = tempNum


def test():
    nums = [1,1,1,2,2,1,2,0,2]
    sortColors(nums);

    for value in nums:
        print(value)


test()





