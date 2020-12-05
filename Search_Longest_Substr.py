#return the specified string's longest substring without repeated character and its length
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub=''
        sublen=0
        for i in range(len(s)):
            sub_temp=''
            sublen_temp=0
            j=i
            while ((j<len(s) and (s[j] not in sub_temp))):
                sub_temp+=s[j]
                sublen_temp+=1
                j+=1
            if sublen_temp>sublen:
                sublen=sublen_temp
                sub=sub_temp
        return sub,sublen

if __name__ == "__main__":
    s=Solution()
    print(s.lengthOfLongestSubstring('abcabcbb'))
