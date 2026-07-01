class Solution:
    def isPalindrome(self, s: str) -> bool:
        t =[]
        for i in s:
            if i.isalnum():
                t.append(i)
        print(t)

        left = 0
        right = len(t)-1

        while left <= right:
            if t[left].lower() != t[right].lower() :
                return False

            left += 1
            right -= 1
        
        return True

        