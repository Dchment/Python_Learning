# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def romanToInt(s: str) -> int:
    total = 0
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, '':0}
    i=0
    while i<(len(s)):
        a=s[i]
        b=(s[i + 1] if i+1<len(s) else '')
        if  d[a] >= d[b] :
            total += d[a]
            i=i+1
        else:
            total += (d[b] - d[a])
            i = i + 2

    return total

if __name__ == '__main__':
    s='XIV'
    print(romanToInt(s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
