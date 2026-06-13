class Solution:
    def countBits(self, n: int) -> List[int]:

        bag = []

        for i in range( n + 1):
            num = i

            count = 0

            while num > 0:
                if num & 1 == 1:
                    count += 1

                num = num >> 1
            bag.append(count)
        return bag

            
        