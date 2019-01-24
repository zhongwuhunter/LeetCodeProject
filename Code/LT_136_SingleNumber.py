


def singleNumber(nums):

    res = 0
    count = len(nums)
    if count % 2 != 1:
        return  -1;


    for val in nums:
        res ^= val

    return res



def test():
    nums = [0,2,1,1,0]

    res =  singleNumber(nums)
    print(res)

test()