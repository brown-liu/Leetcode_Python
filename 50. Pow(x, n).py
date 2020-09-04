from multiprocessing import Process
import time
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            x = 1 / x
            n = -n

        curProduct = x
        res = 1
        while n > 0:
            if n % 2 == 1:
                res *= curProduct

            curProduct *= curProduct
            n //= 2

        return res



    def myPow2(self, x: float, n: int) -> float:
        total = 1
        if x == 0:
            return 0
        if n==0:
            return 1
        if x>0 or n%2==0:
            for _ in range(1, abs(n) + 1):
                total *= x
            if n > 0:
                return abs(total)
            else:
                return 1.0 / (abs(total))
        else:
                for _ in range(1, abs(n) + 1):
                    total *= x
                if n > 0:
                    return -abs(total)
                else:
                    return -1.0 / (abs(total))

if __name__=="__main__":

    solution=Solution()
    a1=print(solution.myPow(3,9100),'A1',time.time())
    a2=print(solution.myPow2(3,9100),'A2',time.time())
    process1=Process(target=a1)
    process2=Process(target=a2)
    process1.start()
    process2.start()


