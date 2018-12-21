#   给定一个字符串，找出不含有重复字符的最长子串的长度
#
#

def testsub(string):
    count = len(string)
    cur_len = 1
    rightIndex = 0
    leftIndex = 0
    max_len = 1
    visited = [-1] * 256
    visited[ord(string[0])] = 0

    for rightIndex in range(1, count) :
        leftIndex = visited[ord(string[rightIndex])]

        if leftIndex == -1 or (rightIndex - cur_len > leftIndex):
            cur_len += 1
        else:
            if cur_len > max_len :
                max_len = cur_len
            cur_len = rightIndex - leftIndex
        visited[ord(string[rightIndex])] = rightIndex

    if cur_len > max_len :
        max_len = cur_len

    return max_len




def lengthOfLongestSubString(string):
    if len(string) == 0 :
        return 0

    n = len(string)
    cur_len = 1
    max_len = 1
    prev_index = 0
    i = 0

    # prev_index == -1 表示 visited 没有重复的字符
    visited = [-1] * 256
    visited[ord(string[0])] = 0

    for i in range(1, n):
        prev_index = visited[ord(string[i])]
        if  prev_index == -1 or (i - cur_len > prev_index):
        # if prev_index == -1 :
            cur_len += 1
        else:
            if cur_len > max_len :
                max_len = cur_len

            cur_len = i - prev_index

        visited[ord(string[i])] = i

    if cur_len > max_len :
        max_len = cur_len

    return max_len




def test():
    # str = 'aba1b21a3a4';
    str = '1234';
    # max = lengthOfLongestSubString(str)
    max = testsub(str)

    # print( max )

test()






