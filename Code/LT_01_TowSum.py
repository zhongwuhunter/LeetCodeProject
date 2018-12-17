




def towSum(nums, target):
    dict = {};
    for value in nums:
        index = nums.index(value);
        complement = target - value;
        if str(complement) in dict :
            return (index, nums.index(complement));
        dict[str(value)] = index;
    return (0,0)
def start():
    nums = [2, 7, 11, 15, 90, 78];
    traget = 91;

    tup = towSum(nums, traget);
    print(tup[0], tup[1]);

start()