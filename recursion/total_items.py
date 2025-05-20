# Write a recursive function to count the numbers of items in a list

items = [3, 5, 7]

def total_items(arr):
    if len(arr) == 0:
        return 0
    else:
        return 1 + total_items(arr[1:])

def main():
    print(total_items(items))

if __name__ == "__main__":
    main()
