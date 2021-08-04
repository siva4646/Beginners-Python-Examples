#Generator example

def square_numbers(nums):
    for i in nums:
#yield is a keyword in Python that is used to return from a function without destroying the states of its local variable and when the function is called, the execution starts from the last yield statement.        
        yield (i * i)


if __name__ == '__main__':

    squares_of_nums = square_numbers([1, 2, 3, 4, 5, 6])
    for num in squares_of_nums:
        print(num)

