class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        arr = []
        
        for i in num:        
            while k > 0 and arr and arr[-1] > i:         
                k -= 1
                arr.pop()         
            arr.append(i)
        print(arr[:len(arr) - k])
        arr = arr[:len(arr) - k] #case for single digit input
        
        res = "".join(arr).lstrip('0')
        
        return res if res else "0"