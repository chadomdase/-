#二、 資料處理-字串


string = "人易科技:上機測驗-演算法"

# 1. 将字元 ":" 改成全型
string = string.replace(":", "：")

# 2. 去掉中文字间的空白（保留 "-" 号两侧的空白）
string = "".join(string.split())

# 3. 列印出符号 ":" 到 "-" 之间的字元
start_index = string.index("：") + 1
end_index = string.index("-")
substring = string[start_index:end_index]
print(substring)
