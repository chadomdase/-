 #給定一個整數陣列 nums 和一個整數 target,當兩數總和為target時,返回兩數的索引。 
#您可以假設每個輸入都只有一個解決方案,並且您可能不會兩次使用相同的元素。 
#您可以按任何順序返回答案。 
#限制條件: 
#2 <= nums.length <= 103 
#-109 <= nums[i] <= 109 
#-109 <= target <= 109 
#僅存在一個有效答案。


def two_sum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i

nums = [2, 7, 11, 15]
target = 9

result = two_sum(nums, target)

print(result)
