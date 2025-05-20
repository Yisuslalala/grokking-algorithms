numbers = [3, 6, 2, 1]

def max_number(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return max(arr[0], max_number(arr[1:]))

def main():
    print(max_number(numbers))

if __name__ == "__main__":
    main()
