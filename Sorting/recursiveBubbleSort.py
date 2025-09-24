class Solution:
    def bubbleSort(self,nums):
        self.recursiveBubbleSortHelper(nums, len(nums))
        return nums
    def recursiveBubbleSortHelper(self, nums, n):
        if n == 1:
            return 
        for i in range(n-1):
            if nums[i] > nums[i + 1]:            
                nums[i],nums[i+1] = nums[i + 1], nums[i]
        self.recursiveBubbleSortHelper(nums, n - 1)
    

if __name__ == "__main__":
    nums = [13,46,24,52,20,9]
    solution = Solution()
    print("Regular Bubble Sort", solution.bubbleSort(nums))