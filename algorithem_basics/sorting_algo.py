from timeit import timeit
import random



class Sorting:

    def __init__(self, max_array_length, number_of_array):
        int_array = []
        for i in range(number_of_array):
            temp_array = []
            for j in range(random.randint(0, max_array_length)):
                temp_array.append(random.randint(0, 500))
            int_array.append(temp_array)
        self.int_array = int_array

    @staticmethod
    def bubble_sort(int_array):
        for i in range(1, len(int_array)):
            for idx in range(1, len(int_array)):
                if int_array[idx] < int_array[idx - 1]:
                    int_array[idx], int_array[idx - 1] = int_array[idx - 1], int_array[idx]
        return int_array

    @staticmethod
    def selection_sort(int_array):

        def find_min(result_array, temp_array):
            result_array = result_array
            if len(temp_array) > 2:
                min = 0
                for idx in range(1, len(temp_array)):
                    if int_array[idx] < int_array[min]:
                        min = idx
                result_array.append(temp_array.pop(min))
                return result_array, temp_array
            else:
                return None

        sorted_array = []
        while find_min(sorted_array, int_array) != None:
            sorted_array, int_array = find_min(sorted_array, int_array)

        return sorted_array

    @staticmethod
    def insert_sort(int_array):
        for i in range(1, len(int_array)):
            key = int_array[i]
            j = i - 1

            while j >= 0 and key < int_array[j]:
                int_array[j + 1] = int_array[j]
                j -= 1
            int_array[j + 1] = key
        return int_array

    @staticmethod
    def merge_sort(int_array):
        n=len(int_array)
        if n <2:
            return int_array
        mid= n//2
        left= Sorting.merge_sort(int_array[:mid])
        right=Sorting.merge_sort(int_array[mid:])
        left_pointer,right_pointer=0,0
        result=[]
        while left_pointer<len(left) and right_pointer <len(right):
            if left[left_pointer]<right[right_pointer]:
                result.append(left[left_pointer])
                left_pointer+=1
            else:
                result.append(right[right_pointer])
                right_pointer+=1
        result+=left[left_pointer:]
        result+=right[right_pointer:]
        return result






######################################### Auto Testing#########################################################
test = Sorting(10, 10)

for item in test.int_array:
    print(f'{item}=====>{Sorting.merge_sort(item)}\n')

