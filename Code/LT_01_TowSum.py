# 给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
#
# 你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
#
# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]





# 答案
def towSum(nums, target):
    dict = {};
    for value in nums:
        index = nums.index(value);
        complement = target - value;
        if str(complement) in dict :
            return (index, nums.index(complement));
        dict[str(value)] = index;
    return (0,0)






def cus_towSum(nums, target):
    dict = {}

    for value in nums:
        index = nums.index(value)
        complement = target - value
        if str(complement) in dict :
            return (index, nums.index(complement))
        dict[str(value)] = index

    return (0, 0)

def start():
    nums = [2, 7, 11, 15, 90, 78];
    traget = 18;

    tup = cus_towSum(nums, traget);
    print(tup[0], tup[1]);

start()