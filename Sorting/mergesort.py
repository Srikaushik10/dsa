class Solution:
    def mergeSort(self, nums):
        n = len(nums)
        self.mergeSortHelper(nums, 0 , n - 1)
        return nums
    
    def mergeSortHelper(self,nums,low,high):
        if low >= high:
            return 
        mid = (low + high) // 2
        self.mergeSortHelper(nums,low, mid)
        self.mergeSortHelper(nums,mid + 1, high)
        self.merge(nums, low, mid, high)
    
    def merge(self, nums, low, mid, high):
        temp_arr = []
        left = low
        right = mid + 1
        while left <= mid and right <= high:
            if nums[left] <= nums[right]:
                temp_arr.append(nums[left])
                left+= 1
            else:
                temp_arr.append(nums[right])
                right+= 1
        while left <= mid:
            temp_arr.append(nums[left])
            left+= 1
        while right <= high:
            temp_arr.append(nums[right])
            right+=1
        
        for i in range(low, high + 1):
            nums[i] = temp_arr[i - low]


if __name__ == "__main__":
    nums = [9, 4, 7, 6, 3, 1, 5]
    solution = Solution()
    print("MergeSort", solution.mergeSort(nums))