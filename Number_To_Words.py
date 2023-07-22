# Define the word mappings for numbers 0 to 19
numbers_map = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
    11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
    16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
}

# Define the word mappings for tens and multiples of ten
tens_map = {
    20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
    60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'
}

# Function to convert a number less than 100 into words
def convert_less_than_hundred(num):
    if num < 20:
        return numbers_map[num]

    tens = num // 10 * 10
    ones = num % 10
    if ones != 0:
        return tens_map[tens] + '-' + numbers_map[ones]
    else:
        return tens_map[tens]

# Function to convert a number less than 1000 into words
def convert_less_than_thousand(num):
    hundreds = num // 100
    remainder = num % 100
    result = ''
    if hundreds != 0:
        result = numbers_map[hundreds] + ' hundred'
    if remainder != 0:
        if result:
            result += ' '
        result += convert_less_than_hundred(remainder)
    return result

# Function to format number with comma
def format_number_with_comma(num):
    num_str = str(num)
    formatted_num = ""
    for i in range(len(num_str)):
        formatted_num += num_str[i]
        if (len(num_str) - i - 1) % 3 == 0 and i != len(num_str) - 1:
            formatted_num += ","
    return formatted_num

# Function to convert a number into words
def convert_number_to_words(num):
    if num == 0:
        return 'zero'

    # Split the number into groups of three digits
    groups = []
    while num > 0:
        groups.append(num % 1000)
        num //= 1000

    # Convert each group of three digits into words
    group_names = ['', 'thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion',
                   'sextillion', 'septillion', 'octillion', 'nonillion', 'decillion', 'undecillion',
                   'duodecillion', 'tredecillion', 'quattuordecillion', 'quindecillion', 'sexdecillion',
                   'septendecillion', 'octodecillion', 'novemdecillion', 'vigintillion']
    result = ''
    for i in range(len(groups)):
        if groups[i] != 0:
            group_name = group_names[i]
            group_words = convert_less_than_thousand(groups[i])
            if result:
                result = group_words + ' ' + group_name + ' ' + result
            else:
                result = group_words + ' ' + group_name

    return result


# Test the program
print()
num = int(input('Enter an integer number: '))
formatted_num = format_number_with_comma(num)
print("\nNumber with comma:", formatted_num)
result = convert_number_to_words(num)
print('\nNumber in words:-\n\n', result)
print()
