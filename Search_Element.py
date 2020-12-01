#Search the specified element in the ordered list,if it exists,print the index,if not, print this element's supposed positioh
def searchInsert(nums, target: int) -> int:
    pos = 0
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        if nums[i] < target:
            pos += 1
    return pos

if __name__ == '__main__':
    print(searchInsert([1,3,4,6],3))