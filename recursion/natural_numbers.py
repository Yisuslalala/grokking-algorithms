
# print firsts 50 natural numbers using recursion
def natural_numbers(n):
    if n <= 50:
        print(n)
        natural_numbers(n + 1)

def main():
    natural_numbers(1)

if __name__ == "__main__":
    main()
