# 80점 (5번 입력 오답)

N = int(input())
nums = tuple(map(int, input().split()))
nums1 = []
nums2 = []
nums3 = []

# 3으로 나눈 나머지에 따라 숫자들을 나눔
for num in nums:
    if num % 3 == 1:
        nums1.append(num)
    elif num % 3 == 2:
        nums2.append(num)
    else:
        nums3.append(num)

# 나머지가 1인 숫자만 혹은 나머지가 2인 숫자만 있는 경우 그냥 정렬만 하면 됨
if len(nums3) == 0 and (len(nums1) == 0 or len(nums2) == 0):
    print(*sorted(nums))
# 나머지가 1인 숫자와 나머지가 2인 숫자가 존재하는데 3의 배수인 숫자가 없으면 불가능
# - 나머지 1인 숫자와 나머지 2인 숫자가 인접하는 경우가 생김 -> 합치면 3의 배수
# 3의 배수의 개수가 나머지 1인 숫자, 나머지 2인 숫자 개수의 합보다 1개를 초과해서 더 많으면 불가능
# - 3의 배수끼리 인접하는 경우가 생김 -> 합치면 3의 배수
# 이 조건이 아닌 경우 모두 가능함
elif len(nums3) > len(nums1) + len(nums2) + 1 or len(nums3) == 0:
    print(-1)
# 3의 배수의 개수가 나머지 1인 숫자, 나머지 2인 숫자 개수의 합보다 1개 더 많은 경우
# - 3의 배수 사이에 다른 숫자들이 1개씩 들어감
elif len(nums3) == len(nums1) + len(nums2) + 1:
    result = []
    nums3.sort()
    k = 0
    for num in sorted(nums1 + nums2):
        result.append(nums3[k])
        result.append(num)
        k += 1
    result.append(nums3[-1])
    print(*result)
# 나머지 1인 숫자가 없거나 나머지 2인 숫자가 없는 경우
# - 3의 배수끼리만 인접하지 않도록 잘 배열
elif len(nums1) == 0 or len(nums2) == 0:
    result = []
    if len(nums1) == 0:
        nums1 = nums2
    nums1.sort()
    nums3.sort()
    i = 0
    k = 0
    if nums3[0] < nums1[0]:
        result.append(nums3[0])
        k += 1
    while len(nums1) - i > len(nums3) - k > 0:
        result.append(nums1[i])
        i += 1
        while len(nums1) - i >= len(nums3) - k > 0 and nums1[i] < nums3[k]:
            result.append(nums1[i])
            i += 1
        result.append(nums3[k])
        k += 1
    while len(nums3) > k:
        result.append(nums1[i])
        result.append(nums3[k])
        i += 1
        k += 1
    result += nums1[i:]
    print(*result)
# 모든 종류의 숫자가 존재하는 경우
# - 3의 배수를 칸막이로 생각하고 3의 배수 사이에는 같은 종류의 숫자만 들어가도록 잘 배열
else:
    result = []
    nums1.sort()
    nums2.sort()
    nums3.sort()
    i = 0
    j = 0
    k = 0
    if len(nums3) != 1 and nums3[0] < nums1[0] and nums3[0] < nums2[0]:
        result.append(nums3[0])
        k += 1
    while len(nums1) + len(nums2) - i - j > len(nums3) - k > 0:
        if k == len(nums3) - 1 and len(nums1) > i and len(nums2) > j:
            if nums1[i] < nums2[j]:
                result += nums1[i:]
                result.append(nums3[k])
                result += nums2[j:]
            else:
                result += nums2[j:]
                result.append(nums3[k])
                result += nums1[i:]
            i = len(nums1)
            j = len(nums2)
            k = len(nums3)
            break
        elif len(nums2) == j or nums1[i] < nums2[j]:
            result.append(nums1[i])
            i += 1
            while len(nums1) + len(nums2) - i - j >= len(nums3) - k > 0 and nums1[i] < nums3[k]:
                result.append(nums1[i])
                i += 1
            result.append(nums3[k])
            k += 1
        elif len(nums1) == i or nums1[i] > nums2[j]:
            result.append(nums2[j])
            j += 1
            while len(nums1) + len(nums2) - i - j >= len(nums3) - k > 0 and nums2[j] < nums3[k]:
                result.append(nums2[j])
                j += 1
            result.append(nums3[k])
            k += 1
    while k < len(nums3):
        if len(nums2) == j or nums1[i] < nums2[j]:
            result.append(nums1[i])
            i += 1
            result.append(nums3[k])
            k += 1
        elif len(nums1) == i or nums1[i] > nums2[j]:
            result.append(nums2[j])
            j += 1
            result.append(nums3[k])
            k += 1
    result += nums1[i:]
    result += nums2[j:]
    print(*result)