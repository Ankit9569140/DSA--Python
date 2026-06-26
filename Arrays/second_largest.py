# Find the Second Largest Element in an Array

class Solution:
    def getSecondLargest(self, arr):
        # Assume no largest elements yet
        largest = -1
        second = -1

        # Traverse the array
        for num in arr:

            # Update largest and second largest
            if num > largest:
                second = largest
                largest = num

            # Update second largest only
            elif num > second and num != largest:
                second = num

        # Return second largest element
        return second


# Example
arr = [10, 20, 5, 40, 15]

obj = Solution()
print(obj.getSecondLargest(arr))

"""
Output:
20
"""
