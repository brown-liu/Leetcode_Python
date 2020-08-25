class Binary_Algo:
    def basic_binary_search(self, target, array):
        target = 18
        pool = [x for x in range(20)]
        min = 0
        max = len(pool)
        mid = (min + max) // 2
        count = 0
        while target != pool[mid]:
            mid = (min + max) // 2
            count += 1
            print(mid)
            if target > pool[mid]:
                min = mid
            else:
                max = mid

        print(f'{target} index in {pool} is {mid}')


class One_D_Array_Handling:
    # in place operation Time: O(n^2)  Space :O(1)
    @staticmethod
    def sorting_array_back_to_front_scan(array):
        for i in range(1, len(array)):
            for j in range(len(array)):
                if array[j] > array[i]:
                    array[j], array[i] = array[i], array[j]
        return array

    # devide and conquer
    @classmethod
    def V1quick_sorting(cls, array):
        if len(array) >= 2:
            mid = array[-1]
            left, right = [], []
            array.remove(mid)
            for num in array:
                if num >= mid:
                    right.append(num)
                else:
                    left.append(num)
            return cls.V1quick_sorting(left) + [mid] + cls.V1quick_sorting(right)


        else:
            return array

    @staticmethod
    def V2quick_sorting(self, array):
        if len(array) < 2:
            return array
        else:
            mid = array[-1]
            left, right = [], []
            array.remove(mid)
            for num in array:
                if num > mid:
                    right.append(num)
                else:
                    left.append(num)
            return self.V2quick_sorting(self, left) + [mid] + self.V2quick_sorting(self, right)

    @classmethod
    def merge_sort(cls, array):
        if len(array) < 2:
            return array
        middle = len(array) // 2
        left, right = array[0:middle], array[middle:]
        return cls.merge(cls.merge_sort(left), cls.merge_sort(right))

    @staticmethod
    def merge(left, right):
        result = []
        while left and right:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0));
        while left:
            result.append(left.pop(0))
        while right:
            result.append(right.pop(0));
        return result


print(One_D_Array_Handling.V2quick_sorting(self=One_D_Array_Handling, array=[3, 6, 1, 2, 9, 4, 6]))
print(One_D_Array_Handling.merge_sort([2, 5, 3, 2, 45, 7, 4]))
