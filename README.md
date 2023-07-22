# Number to Words Converter

This Python script converts an integer number into its word representation. It provides the following functionalities:

1. Conversion of large numbers (thousands, millions, billions, etc.) into words.
2. Formatting a number with commas for better readability.

## How to Use

1. Run the script using a Python interpreter.
2. Enter the integer number you want to convert when prompted.

## Function Descriptions

1. `convert_less_than_hundred(num)`: Converts a number less than 100 into words.

2. `convert_less_than_thousand(num)`: Converts a number less than 1000 into words.

3. `format_number_with_comma(num)`: Formats a number with commas for better readability.

4. `convert_number_to_words(num)`: Converts a large number (thousands, millions, billions, etc.) into words.

## Examples

1. Input: `1234567`
   Output: `"one million two hundred thirty-four thousand five hundred sixty-seven"`

2. Input: `987654321`
   Output: `"nine hundred eighty-seven million six hundred fifty-four thousand three hundred twenty-one"`

3. Input: `42`
   Output: `"forty-two"`

4. Input: `1000000`
   Output: `"one million"`

## Note

- The script only works with positive integer numbers.
- Negative numbers and non-integer inputs are not supported.

Happy coding! 🚀
