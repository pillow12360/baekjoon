# A = int(input())
num = 11
ans = 0


# if num % 3 == 0 and num % 5 == 0 :
#   while (num >= 5):
#     num -= 5
#     ans += 1
#   while (num >= 3):
#     num -= 3 
#     ans += 1 
# else:
#     while (num >= 3):
#       num -= 3
#       ans += 1 

# if num == 0:
#   print(ans)
# else:
#   print(-1)

if num // 5 > 0:
    ans += num // 5
    num = num - ans*5

print(num)
print(ans)