arr = [2, 4, 3, 5]

def recursive_sum(arr):
    print(f"in sum function: {arr}")
    left_arr = arr[:1]
    sum = [x for x in left_arr if arr[:1]]
    print(f"sum : {sum}")

    right_arr = arr[1:]
    print(f"sliced: {right_arr}")
    if len(arr) <= 1:
        print("length menor o igual a 1")
        return sum
    else:
        print("length más de 0")
        return sum + recursive_sum(right_arr)

def main():
    print(sum(arr))


if __name__ == "__main__":
    main()
