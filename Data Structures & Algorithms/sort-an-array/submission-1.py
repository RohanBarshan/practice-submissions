class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def quickSort(arr: list[int], s: int, e: int):
            if e - s + 1 <= 1:
                return arr

            # Randomize pivot to avoid O(n^2) on sorted/reverse-sorted data
            import random
            pivot_idx = random.randint(s, e)
            arr[e], arr[pivot_idx] = arr[pivot_idx], arr[e]
            
            pivot = arr[e]
            left = s

            # partition element smaller than the pivot
            for i in range(s, e):
                if arr[i] < pivot:
                    tmp = arr[left]
                    arr[left] = arr[i]
                    arr[i] = tmp
                    left += 1
            
            # move pivot in between left side and right side
            arr[e] = arr[left]
            arr[left] = pivot

            # quickSort left half
            quickSort(arr, s, left - 1)

            # quickSort right half
            quickSort(arr, left + 1, e)

            return arr

        return quickSort(nums, 0 , len(nums) - 1)