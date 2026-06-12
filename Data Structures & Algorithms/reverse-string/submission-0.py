class Solution:
    def reverseString(self, s: List[str]) -> None:
        #Time complexity is O(n) because we are iterating through a string of size n
        #Space complexity is O(1) because we are not using any extra space
        leftpointer=0
        rightpointer=len(s)-1
        while leftpointer < rightpointer:
            s[leftpointer], s[rightpointer] = s[rightpointer], s[leftpointer]
            leftpointer+=1
            rightpointer= rightpointer-1
        

        