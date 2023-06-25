#四、 資料排序-正序
#今有一陣列資料 77,5,5,22,13,55,97,4,796,1,0,9 請寫出正序排列處理程式碼 
#本題需自行完成演算法,不可使用現成排序函式


def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

data = [77, 5, 5, 22, 13, 55, 97, 4, 796, 1, 0, 9]

sorted_data = bubble_sort(data)

print(sorted_data)