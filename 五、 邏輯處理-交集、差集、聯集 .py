#五、 邏輯處理-交集、差集、聯集
#今有二陣列,請寫出資料處理程式碼，陣列a:77,5,5,22,13,55,97,4,796,1,0,9 
#陣列b:0,1,2,3,4,5,6,7,8,9 
#本題需自行完成演算法,不可使用現成交集/差集/聯集函式

array_a = [77, 5, 5, 22, 13, 55, 97, 4, 796, 1, 0, 9]
array_b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

array_c = [x for x in array_a if x in array_b]

array_d = [x for x in array_a if x not in array_b]

array_e = array_a + [x for x in array_b if x not in array_a]

# 列印結果
print("陣列c:", array_c)
print("陣列d:", array_d)
print("陣列e:", array_e)