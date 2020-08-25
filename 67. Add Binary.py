class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)
        return (bin(x + y))[2:]


print("Convert decimal to Binary 0-1", bin(10))
print("Convert decimal to Hex 0-15", hex(20))
print("Convert decimal to OCT 0-7", oct(10))
print(f"To int int('0b1011',2)=>{int('0b1011', 2)}\nTo int('0x20',16)=>{int('0x20', 16)}")
print(f"chr(110)=>{chr(110)} or ord('A')=>{ord('A')}")
for i in range(50, 100, 3):
    print(f"chr({i})=> {chr(i)}")
