#Remove elements with value specified in parameter(without additional list space)
def removeElement(nums, val: int) -> int:
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i = i + 1
    return i

if __name__ == '__main__':
    print(removeElement([1,1,3,4,2,3,5,3],3))