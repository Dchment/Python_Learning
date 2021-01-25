#Return the length of a string's last word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:#核心：不要从头开始判断，要逆向思维从尾部开始判断！！！！
        count=0
        end=len(s)-1
        if(end<0):
            return 0
        while(s[end]==' ' and end>=0):
            end-=1
        while(s[end]!=' ' and end>=0):
            count+=1
            end-=1
        return count

s=Solution()
print(s.lengthOfLastWord('Hello World'))
