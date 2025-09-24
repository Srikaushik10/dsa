class Solution:
    def insertSort(self, nums):
        n = len(nums)
        for i in range(1, n):
            curr = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > curr:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j] = curr
        return nums
    
if __name__ == "__main__":
    nums = [14,9,15,12,6,8,13]
    solution = Solution()
    print("Insertion Sort:", solution.insertSort(nums))
