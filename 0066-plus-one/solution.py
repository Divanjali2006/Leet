class Solution:
    def plusOne(self, digits):
        s=''.join(map(str,digits))
        num=int(s)+1
        result=list(map(int,str(num)))
        return result
    
        
