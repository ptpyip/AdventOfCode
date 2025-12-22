"""Advent of Code 2025 Day 3: Lobby"""


def main():
    exampl_input = """
987654321111111
811111111111119
234234234234278
818181911112111"""

    #print(exampl_input)
    #ans = sum(map(turn_on_batteries, exampl_input.split('\n')))
    #print(ans)

    ### geting answer for real
    sum = 0
    with open("../inputs/day3.txt", 'r') as f:
        for bank in f:
            sum += turn_on_batteries(bank)

    print(sum)
        

def turn_on_batteries(bank):
    """ Select 2 number in the str `bank` to form the **largest** 2-digit number"""
    
    assert isinstance(bank, str)
    if len(bank) == 0: 
        return 0

    first_digit = bank[0]
    second_digit = bank[1]
    for i in range(2,  len(bank)):
        rating = bank[i]
        
        current = int(first_digit + second_digit)
        opt_1 = int(first_digit + rating)
        opt_2 = int(second_digit + rating)
        
        if (opt_1 <= current and opt_2 <= current):
            continue
        elif (opt_1 > opt_2):
            second_digit = rating
        else:
            first_digit = second_digit
            second_digit = rating

    print(int(first_digit + second_digit))
    return int(first_digit + second_digit)

if __name__ == "__main__":
    main()
