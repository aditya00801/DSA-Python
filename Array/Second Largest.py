class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        Largest = 0
        SecondLargest = 0
        for i in range(len(arr)):
            if Largest < arr[i]:
                SecondLargest = Largest
                Largest = arr[i]

            if Largest > arr[i] and SecondLargest < arr[i]:
                SecondLargest = arr[i]

        return SecondLargest
