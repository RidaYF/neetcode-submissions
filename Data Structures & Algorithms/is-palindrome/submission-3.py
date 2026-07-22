import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cpt = 0
        s = s.translate(str.maketrans("", "", string.punctuation)).replace(" ", "").lower()
        print(s)
        for i in range((len(s)//2)):
            if s[i] == s[len(s)-i-1]:
                cpt+=1
        print("cpt = :",cpt)
        print("length of s: ",len(s)//2)
        if cpt == len(s)//2:
            return True
        else:
            return False