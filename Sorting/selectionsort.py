class Solution:
    def selectionSort(self,arr):
        n = len(arr)
        for i in range(0,n - 1):
            min = i
            for j in range(i + 1, n):
                if arr[j] < arr[min]:
                    min = j
            arr[i], arr[min] = arr[min], arr[i]
        return arr
    
if __name__ == "__main__":
    arr = [13,46,24,52,20,9]
    solution = Solution()
    print("Sorted :", solution.selectionSort(arr))
    
        
    
    