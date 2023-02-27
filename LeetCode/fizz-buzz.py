class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ret = [str(i+1) for i in range(n)]
        for i in range(n):
            if (i+1)%3==0:
                ret[i]="Fizz"
                if (i+1)%5==0:
                    ret[i]+="Buzz"
            elif (i+1)%5==0:
                ret[i]="Buzz"
        
        return ret