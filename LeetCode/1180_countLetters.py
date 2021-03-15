"""
Given a string S, return the number of substrings that have only one distinct letter.
Example 1:
Input: S = "aaaba"
Output: 8
Explanation: The substrings with one distinct letter are "aaa", "aa", "a", "b".
"aaa" occurs 1 time.
"aa" occurs 2 times.
"a" occurs 4 times.
"b" occurs 1 time.
So the answer is 1 + 2 + 4 + 1 = 8
"""
def countLetters(S):
    begin = 1
    nSub = 0
    pre = S[0]
    for i in range(1,len(S)):
        if(S[i]!=pre):
            nSub += (begin)*(begin+1)/2
            begin=1
            pre = S[i]
        else:
            begin+=1
    nSub += (begin)*(begin+1)/2
    return nSub
