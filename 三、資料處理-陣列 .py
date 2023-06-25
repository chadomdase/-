#三、資料處理-陣列 
#今有陣列資料 0,1,2,3,4,5,6,7,8,9請寫出資料處理程式碼 


data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 1. 計算出「奇數值總和」減去「偶數值總和」
odd_sum = 0
even_sum = 0
for num in data:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num
difference = odd_sum - even_sum

# 2. 分割成二陣列,分別存放「偶數值」及「奇數值」
even_array = []
odd_array = []
for num in data:
    if num % 2 == 0:
        even_array.append(num)
    else:
        odd_array.append(num)

# 列印結果
print("奇數值總和減去偶數值總和:", difference)
print("偶數值陣列:", even_array)
print("奇數值陣列:", odd_array)
