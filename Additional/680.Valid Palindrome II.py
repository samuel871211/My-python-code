class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s[0] != s[-1]:
            head , tail = s[1:] , s[:-1]
            return self.deletehead(head,tail)
        else:
            while s[0] == s[-1]:
                s = s[1:-1]
                if 0 <= len(s) <= 2:
                    return True    
            if len(s) > 2:
                return self.validPalindrome(s)
            
    def deletehead(self,head,tail):
        while head[0] == head[-1]:
            head = head[1:-1]
            if len(head) == 1 or len(head) == 0:
                return True    
        if len(head) > 1:
            return self.deletetail(tail)
        
    def deletetail(self,tail):
        while tail[0] == tail[-1]:
            tail = tail[1:-1]
            if len(tail) == 1 or len(tail) == 0:
                return True    
        if len(tail) > 1:
            return False
