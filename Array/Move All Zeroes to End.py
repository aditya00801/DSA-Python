class Solution:
    def pushZerosToEnd(self, arr):  # indentation for method
        count = 0                   # inside the method
        n = len(arr)

        for i in range(n):
            if arr[i] != 0:
                arr[count] = arr[i]
                count += 1

        while count < n:
            arr[count] = 0
            count += 1

        return arr


if __name__ == "__main__":
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(Solution().pushZerosToEnd(arr))
