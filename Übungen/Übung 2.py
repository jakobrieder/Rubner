def values_above_average(numbers):
    result = []
    avg =  sum(numbers)/len(numbers)
    for n in numbers:
        if n > avg:
            result.append(n)
    return result

def main():
    numbers = [2,4,6,8]
    ergebnis = values_above_average(numbers)
    print(ergebnis)

if __name__ == '__main__':
    main()



