from timeit import timeit
class Sorting:

    @staticmethod
    def bubble_sort(int_array):
        for i in range(1,len(int_array)):
            for idx in range(1,len(int_array)):
                if int_array[idx]<int_array[idx-1]:
                    int_array[idx], int_array[idx-1]=int_array[idx-1],int_array[idx]
        return int_array


    @staticmethod
    def selection_sort(int_array):

        def find_min(result_array, temp_array):
            result_array = result_array
            if len(temp_array) > 2:
                min=0
                for idx in range(1, len(temp_array)):
                    if int_array[idx] < int_array[min]:
                        min = idx
                result_array.append(temp_array.pop(min))
                return result_array,temp_array
            else:
                return None

        sorted_array = []
        while find_min(sorted_array,int_array)!=None:
            sorted_array,int_array=find_min(sorted_array,int_array)

        return sorted_array








array=[9,4,32,2,5,8,1,4,3,2,5,0]

print(Sorting.selection_sort(array))
