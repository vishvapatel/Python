string=input()
def isPlindrome(s):
    def tochars(s):
        ans=""
        for char in string:
            if char in "abcdefghijklmnopqrstuvwxyz0123456789":
                ans=ans+char
            return ans
    def ispal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[1] and ispal(s[1: -1])
    return ispal(tochars(s))

