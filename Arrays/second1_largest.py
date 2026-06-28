# Find the Second Largest Element in an Array

class Solution:
    def getSecondLargest(self, arr):
        # Initialize largest and second largest
        largest = float('-inf')
        second = float('-inf')

        # Traverse the array
        for num in arr:

            # If current number is greater than largest
            if num > largest:
                second = largest
                largest = num

            # If current number is between largest and second largest
            elif num > second and num != largest:
                second = num

        # If second largest does not exist
        if second == float('-inf'):
            return -1

        return second


# Example
arr = [12, 35, 1, 10, 34, 1]

obj = Solution()
print(obj.getSecondLargest(arr))

"""
Output:
34
"""
