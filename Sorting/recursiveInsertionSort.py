class Solution:
    def insertSort(self,nums):
        self.insertSortHelper(nums,len(nums))
        return nums
    def insertSortHelper(self, nums, n):
        if n <= 1:
            return
        self.insertSortHelper(nums, n - 1)
        last = nums[n - 1]
        j = n - 2

        while j >= 0 and nums[j] > last:
            nums[j + 1] = nums[j]
            j-=1
        nums[j+1] = last

if __name__ == "__main__":
    arr = [5,2,9,1,5,6]
    sol = Solution()
    print("Recursive Sort", sol.insertSort(arr))