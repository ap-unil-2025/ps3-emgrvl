"""
Problem 3: Number Analysis
Analyze a list of numbers provided by the user.
"""

def get_numbers_from_user():
    """
    Get numbers from user until they type 'done'.
    Return a list of numbers.

    Returns:
        list: List of numbers entered by user
    """
    numbers = []
    n = ""

    while n != "done":
        # TODO: Get input from user
        # TODO: Check if user typed 'done'
        # TODO: Try to convert to float and add to list
        # TODO: Handle invalid input gracefully

        n = input("Enter a number:")
        if n == "done":
            break
        else:
            numbers.append(float(n))
        pass

    print(numbers)

    return numbers

import functools
def analyze_numbers(numbers):
    """
    Analyze the list and return a dictionary with:
    - count: number of elements
    - sum: sum of all numbers
    - average: average value
    - minimum: smallest number
    - maximum: largest number
    - even_count: count of even numbers
    - odd_count: count of odd numbers

    Args:
        numbers (list): List of numbers to analyze

    Returns:
        dict: Dictionary with analysis results, or None if list is empty
    """

    # TODO: Calculate count
    # TODO: Calculate sum
    # TODO: Calculate average
    # TODO: Find minimum
    # TODO: Find maximum
    # TODO: Count even numbers (hint: use modulo operator)
    # TODO: Count odd numbers
    if not numbers:
        return None
    
    analysis = {}

    count = len(numbers)
    analysis["Count"] = count

    sum = functools.reduce(lambda x, y: x+y, numbers)
    analysis["Sum"] = sum

    average = sum/count
    analysis["Average"] = average

    minimum = min(numbers)
    analysis["Minimum"] = minimum

    maximum = max(numbers)
    analysis["Maximum"] = maximum

    list_even = [x for x in numbers if x%2 == 0]
    even_count = len(list_even)
    analysis["Even_count"] = even_count

    list_odd = [x for x in numbers if x%2 != 0]
    odd_count = len(list_odd)
    analysis["Odd_count"] = odd_count

    return analysis


def display_analysis(analysis):
    """
    Display the analysis in a formatted way.

    Args:
        analysis (dict): Dictionary containing analysis results
    """
    if not analysis:
        return

    print("\nAnalysis Results:")
    print("-" * 20)

    # TODO: Display all analysis results in a nice format
    # Example:
    # Count: 5
    # Sum: 25
    # Average: 5.00
    # etc.
    for i in analysis:
        print(f"{i}: {analysis[i]}")
    pass


def main():
    """Main function to run the number analyzer."""
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.")
    print()

    # Get numbers from user
    numbers = get_numbers_from_user()

    if not numbers:
        print("No numbers entered!")
        return

    # Analyze the numbers
    analysis = analyze_numbers(numbers)

    # Display the results
    display_analysis(analysis)


if __name__ == "__main__":
    main()