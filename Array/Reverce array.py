class Solution:
    def reverseArray(self, arr):
        # code here
        n = len(arr)

        for i in range(n // 2):
            temp = arr[i]
            arr[i] = arr[n - i - 1]
            arr[n - i - 1] = temp

        return arr

class Solution:
    def reverseArray(self, arr):
        # code here
        n = len(arr)

        for i in range(n // 2):
            temp = arr[i]
            arr[i] = arr[n - i - 1]
            arr[n - i - 1] = temp

        return arr


# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print("Original array:", arr)

    result = Solution().reverseArray(arr)
    print("Reversed array:", result)


