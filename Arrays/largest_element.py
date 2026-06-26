# Find the Largest Element in an Array

class Solution:
    def largest(self, arr):
        # Assume first element is the largest
        largest = arr[0]

        # Traverse the array
        for num in arr:
            if num > largest:
                largest = num

        # Return the largest element
        return largest


# Example
arr = [10, 20, 5, 40, 15]

obj = Solution()
print(obj.largest(arr))

"""
Output:
40
"""
