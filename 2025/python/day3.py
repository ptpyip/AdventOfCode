"""Advent of Code 2025 Day 3: Lobby"""


def part1():
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

def part2():
    exampl_input = """987654321111111
811111111111119
234234234234278
818181911112111"""

    #print(exampl_input)
    #ans = sum(map(lambda x: int(max_sub_string(x)), exampl_input.split('\n')))
    #print(ans)

    ### geting answer for real
    sum = 0
    with open("../inputs/day3.txt", 'r') as f:
        for bank in f:
            bank = bank.strip("\n")
            sum += int(max_sub_string(bank))

    print(sum)
        
def max_sub_string(bank, l = 12):
    if (len(bank) == 0): return
    assert len(bank) >= l
    if l == len(bank):
        return bank
    elif l == 1:
        return str(max(map(int, bank)))
    
    largest_rating = (0, -1)
    for i in range(len(bank)-l, -1, -1):
        # print(i)
        rating = int(bank[i])
        if (rating >= largest_rating[0]):
            largest_rating = (rating, i) 
    print(largest_rating) 
    return str(largest_rating[0]) + max_sub_string(bank[largest_rating[1]+1:], l-1)
    # l < len(bank)
    # mid = len(bank) // 2     
    # l_next = l // 2
    # left = max_sub_string(bank[:mid], l_next)
    # right = max_sub_string(bank[mid:], l_next)

    #print((mid, l_next, bank[: mid], bank[mid:]), (left, right))

if __name__ == "__main__":
    part1()
    
    part2()
    # print(max_sub_string("987654321111111"))
