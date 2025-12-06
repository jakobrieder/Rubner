import numbers
def transform_numbers(numbers):
    even = [x*2 for x in numbers if x % 2 == 0]
    odd = [x/2 for x in numbers if x % 2 == 1]
    return even, odd

#numbers = [2,3,4,5,6,7,8,9]
#result = transform_numbers(numbers)
# print(result)


def find_local_maxima(numbers):
    maxima = []
    for x in range(1, len(numbers) - 1):
        if numbers[x] > numbers[x - 1] and numbers[x] > numbers[x + 1]:
            maxima.append(numbers[x])
    return maxima


numbers2 = [3, 7, 5, 4, 10, 12]
#result = find_local_maxima(numbers2)
#print(result)

def find_increasing_segments(numbers):
    segments = []
    current_segment = [numbers[0]]

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            current_segment.append(numbers[i])
        else:
            if len(current_segment) > 1:
                segments.append(current_segment)
            current_segment = [numbers[i]]

    if len(current_segment) > 1:
        segments.append(current_segment)

    return segments


numbers = [2, 3, 5, 1, 4, 7, 6]
result = find_increasing_segments(numbers)
print(result)

def bigger_10(numbers):
    result = []
    for n in range(1, len(numbers)-1):
        if numbers[n] + numbers[n-1] > 10:
            result.append(numbers[n])
    return result

numbers3 = [5,6,9,8,1]
result2 = bigger_10(numbers3)
print(result2)














