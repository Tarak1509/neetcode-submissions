#class Solution:
    #def reverseString(self, s: List[str]) -> None:
        #Time complexity is O(n) because we are iterating through a string of size n
        #Space complexity is O(1) because we are not using any extra space
        #leftpointer=0
        #rightpointer=len(s)-1
        #while leftpointer < rightpointer:
            #s[leftpointer], s[rightpointer] = s[rightpointer], s[leftpointer]
            #leftpointer+=1
            #rightpointer= rightpointer-1



# more intuitive solution using a stack
# Time complexity O(n) and Space Complexity O(n)
#class Solution:
    #def reverseString(self, s: List[str]) -> None:
        #stack = []
        #for c in s:
            #stack.append(c)
        #i = 0
        #while stack:
            #s[i] = stack.pop()
           # i = i+ 1



# Recursive Approach
class Solution:
    def reverseString(self, s: List[str]) -> None:
        def reverse(l, r):
            if l < r:
                s[l], s[r] = s[r], s[l]
                reverse(l+1, r-1)
        reverse(0, len(s)-1)

        

        