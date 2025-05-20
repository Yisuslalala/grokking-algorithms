arr = [2, 4, 3, 5]

def recursive_sum(arr):
    print(f"in sum function: {arr}")
    if len(arr) == 0:
        return 0
    else: 
        return arr[0] + recursive_sum(arr[1:])

def main():
    print(recursive_sum(arr))


if __name__ == "__main__":
    main()
