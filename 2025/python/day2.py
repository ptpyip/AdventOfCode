"""Advent Of Code 2025 Day2: Gift Shop"""


def part1(product_id_ranges):
    total_sum = 0
    for id_range in product_id_ranges:
        result = scan_for_invalid(id_range)
        total_sum += result

    print(total_sum)

def scan_for_invalid(id_range):
    start, end = list(map(int, id_range.split("-")))
    print(start, end)
   
    sum_of_invalid = 0
    for num in range(start, end+1):
        invalid = is_invalid(str(num))
        if (invalid):
            print(num)
            sum_of_invalid += num
    return sum_of_invalid


def is_invalid(num):
    num_len = len(num)
    if num_len%2 != 0:
        return False
    
    return int(num[:num_len//2]) == int(num[num_len//2:])
    

def part2(product_id_ranges):
    total_sum = 0
    for id_range in product_id_ranges:
        result = scan_for_invalid2(id_range)
        total_sum += result

    print(total_sum)

def scan_for_invalid2(id_range):
    start, end = list(map(int, id_range.split("-")))
    
    sum_of_invalid = 0
    for num in range(start, end+1):
        for k in range(1, len(str(num))//2 + 1):
            invalid = is_invalid2(str(num), k)
            if (invalid):
                print(num)
                sum_of_invalid += num
    
    return sum_of_invalid
        

def is_invalid2(num, k):
    num_len = len(num)
    if num_len % k == 0: return False

    l = num_len // k
    left = l
    right = l*2
    for i in range(1, k-1):
        if int(num[l*(i-1): l*i]) == int(num[l*i: l*(i+1)]):
            return True
    
    return False


def gen_repeat_sequence(num_of_digit):
    # too many combination
    pass

    
        


if __name__ == "__main__":
    test_inputs = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224, 1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    part1(test_inputs.split(","))
    
    day2_inputs = "853-1994,1919078809-1919280414,1212082623-1212155811,2389-4173,863031-957102,9393261874-9393318257,541406-571080,1207634-1357714,36706-61095,6969667126-6969740758,761827-786237,5516637-5602471,211490-235924,282259781-282327082,587606-694322,960371-1022108,246136-353607,3-20,99-182,166156087-166181497,422-815,82805006-82876926,14165-30447,4775-7265,83298136-83428425,2439997-2463364,44-89,435793-511395,3291059-3440895,77768624-77786844,186-295,62668-105646,7490-11616,23-41,22951285-23017127"
    part1(day2_inputs.split(","))
    
    part2(test_inputs.split(","))
