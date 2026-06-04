#finding the indices of the two numbers in the list that add to the target.

n=int(input())
nums = list(map(int, input().split()))
target = int(input())
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])
            break
    
