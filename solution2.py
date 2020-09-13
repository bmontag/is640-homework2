# Part1: Square and Cube
def part1():
    columns = ['Number', 'Square', 'Cube']
    print(f'{columns[0]:>20}{columns[1]:>20}{columns[2]:>20}')
    for i in range(0, 6):
        print(f'{i:>20}{i**2:>20}{i**3:>20}')

# Part2: Celsius to F
def part2():
    def convertCtoF(c):
        return 9 / 5 * c + 32

    def convertAndPrint(c):
        print(f'{c}°C = {convertCtoF(c)}°F')

    convertAndPrint(-40)
    convertAndPrint(0)
    convertAndPrint(40)
    convertAndPrint(100)

# Part3: Sum and Average
def part3():
    sum_value = 0
    occurences = 3

    for i in range(0, occurences):
        input_value = None
        while type(input_value) != int:
            input_value = input(f"Enter an integer value ({i + 1} / {occurences}): ")
            try:
                input_value = int(input_value)
            except ValueError:
                continue
        sum_value += input_value

    print(f'The sum is {sum_value:,.0f}')
    print(f'The average is {sum_value / occurences:,.2f}')

# Function calls
print("*** Part1 ***")
part1()

print("\n*** Part2 ***")
part2()

print("\n*** Part3 ***")
part3()