# 给出⼀个整形数组nums和⼀个整数k，是否存在索引i和j，使得nums[i] == nums[j] 且i和j之间的差不超过k
# 时间复杂度: O(n)
# 空间复杂度: O(k)

def containsDuplicate2(nums, k):

    count = len(nums)
    if count <= 1 :
        return False

    if k <= 0 :
        return True

    record = set()
    index = 0
    for index in range(index, count):
        val = nums[index]
        if val in record:
            return  True
        record.add(val)

        if len(record) == k + 1 :
            record.remove(nums[index-k])

    return False


def test():
    # Input: nums = [1, 2, 3, 1], k = 3        true
    # Input: nums = [1, 0, 1, 1], k = 1        true
    # Input: nums = [1, 2, 3, 1, 2, 3], k = 2  false
    nums = [1, 2, 3, 4, 1, 2, 3, 4, 6]
    k = 4

    flag = containsDuplicate2(nums, k)

    print(flag)


test()
































