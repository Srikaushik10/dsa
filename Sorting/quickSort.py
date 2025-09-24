import random
class Solution:
    def quickSort(self,nums):
        n = len(nums)
        self.quickSortHelper(nums,0, n - 1)
        return nums
    def quickSortHelper(self, nums, low, high):
        if low < high:
            pIndex = self.partition(nums,low,high)
            self.quickSortHelper(nums,low,pIndex - 1)
            self.quickSortHelper(nums,pIndex + 1, high)
    def partition(self,nums,low,high):
        randomIndex = low + random.randint(0, high - low)
        nums[low], nums[randomIndex] = nums[randomIndex], nums[low]
        pivot = nums[low]
        i = low
        j = high
        while i < j:
            while nums[i] <= pivot and i <= high - 1:
                i += 1
            while nums[j] > pivot and j >= low + 1:
                j -=1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        nums[low], nums[j] = nums[j], nums[low]
        return j 


if __name__ == "__main__":
    nums = [4,6,2,5,7,9,1,3]
    sol = Solution()
    print("Quick Sort", sol.quickSort(nums))