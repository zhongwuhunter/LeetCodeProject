#   给定一个字符串，找出不含有重复字符的最长子串的长度
#
#
# ord() 函数是 chr() 函数   它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值
# 滑动窗口
# 时间复杂度: O(len(s))
# 空间复杂度: O(len(charset))


def alengthOfLongestSubString(string):
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
            cur_len += 1
        else:
            if cur_len > max_len :
                max_len = cur_len

            cur_len = i - prev_index

        visited[ord(string[i])] = i

    if cur_len > max_len :
        max_len = cur_len

    return max_len


# def testLen(string):
#     freq = [0] * 256
#     # 滑动窗口 s[l....r]
#     l = 0
#     r = -1
#     res = 0
#
#     num = ord(string[r + 1])
#
#     while ( l < len(string) ) :
#         num = ord(string[r+1])
#         data = freq[num]
#         if ( r+1 < len(string) and data  == 0 ):
#             r += 1
#         else:
#             l += 1
#
#         res = max(res, r-l+1)
#
#     return res



def testsub(string):
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
        # if  prev_index == -1 or (i - cur_len > prev_index):
        if prev_index == -1 :
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
    # str = 'aabbccaa'
    str = 'abcaaab'
    # max = lengthOfLongestSubstring(str)
    max = testLen(str)

    print( max )

test()






