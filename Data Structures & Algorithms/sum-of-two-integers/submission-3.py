class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Handle negative numbers properly in Python
        mask = 0xFFFFFFFF  # 32-bit mask
        
        while b != 0:
            carry = (a & b) & mask
            a = (a ^ b) & mask
            b = (carry << 1) & mask
        
        # If the result should be negative (MSB is set)
        if a > 0x7FFFFFFF:
            a = ~(a ^ mask)
        
        return a