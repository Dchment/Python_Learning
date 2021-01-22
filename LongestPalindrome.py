# Giving a string, find out its longest palindrome.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        # 枚举子串的长度 l+1
        for l in range(n):
            # 枚举子串的起始位置 i，这样可以通过 j=i+l 得到子串的结束位置
            for i in range(n):
                j = i + l # j为子串结束位置
                if j >= len(s): # 若结束位置超出原串位置，跳出此次循环
                    break
                if l == 0: # 若子串长度仅为1，必为回文
                    dp[i][j] = True
                elif l == 1:# 若子串长度为2，首尾相同即为回文
                    dp[i][j] = (s[i] == s[j])
                else: # 子串长度大于2时，使用动态规划法，将判断子串的任务划分成判断子串去掉头尾的子串的任务进行“递归式判断”！（若子串的去头尾子串不为回文，子串必不为回文！）最后再判断首尾是否相同。
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and l + 1 > len(ans): # 发现更长的回文子串时，更新结果。
                    ans = s[i:j + 1]
        return ans

S=Solution()
print(S.longestPalindrome("abac"))
