class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        arr = []
        
        for i in num:        
            while k > 0 and arr and arr[-1] > i:         
                k -= 1
                arr.pop()         
            arr.append(i)
        
        arr = arr[:len(arr) - k] 
        
        res = "".join(arr).lstrip('0')
        
        return res if res else "0"