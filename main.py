class Solution:
    def findComplement(self, num: int) -> int:
        a=list(bin(num)[2:])
        for i in range(len(a)):
            if a[i]=='1':
                a[i]='0'
            else: a[i]='1'
        return (int(''.join(a),2))


