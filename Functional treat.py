
# Data Analyzer and Transformer Program

# Global variables
dataset = []
data_type = ""
dataset_summary = {
    "total_values": 0,
    "overall_mean": 0
}


# Function to convert input into numbers
def convert_number(value):
    """Convert a string into an integer or float."""
    number = float(value)
    if number.is_integer():
        return int(number)
    return number


# Function to flatten 1D and 2D lists
def flatten_data(data):
    """Convert 1D or 2D list into a single 1D list."""
    if data and isinstance(data[0], list):
        return [item for row in data for item in row]
    return data.copy()


# Function to update global dataset summary
def update_global_summary(data):
    """Update the global dataset summary."""
    global dataset_summary

    values = flatten_data(data)

    if values:
        dataset_summary = {
            "total_values": len(values),
            "overall_mean": sum(values) / len(values)
        }
    else:
        dataset_summary = {
            "total_values": 0,
            "overall_mean": 0
        }


# Function to display data
def display_data(data):
    """Display 1D or 2D dataset."""
    if not data:
        print("No data available.")
        return

    if isinstance(data[0], list):
        print("\n2D Dataset:")
        for row in data:
            print(row)
    else:
        print("\n1D Dataset:")
        print(data)


# Function to input data
def input_data():
    """Accept manual or sample 1D and 2D data."""
    global dataset, data_type

    print("\nSelect Data Input:")
    print("1. Enter Data Manually")
    print("2. Use Sample Data")

    choice = input("Enter your choice: ")

    if choice == "2":
        print("\nSelect Data Type:")
        print("1. 1D List")
        print("2. 2D List")

        option = input("Enter your choice: ")

        if option == "1":
            dataset = [10, 20, 30, 40, 50, 20]
            data_type = "1D"

        elif option == "2":
            dataset = [
                [10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]
            ]
            data_type = "2D"

        else:
            print("Invalid choice!")
            return

    elif choice == "1":
        print("\nSelect Data Type:")
        print("1. 1D List")
        print("2. 2D List")

        option = input("Enter your choice: ")

        if option == "1":
            while True:
                try:
                    values = input(
                        "Enter numbers separated by commas: "
                    )
                    dataset = [
                        convert_number(x.strip())
                        for x in values.split(",")
                        if x.strip()
                    ]

                    if dataset:
                        break

                    print("Please enter at least one number.")

                except ValueError:
                    print("Invalid input! Enter numeric values.")

            data_type = "1D"

        elif option == "2":
            dataset = []

            print("Enter each row separated by commas.")
            print("Press Enter without values to finish.")

            while True:
                row = input("Enter row: ")

                if not row.strip():
                    break

                try:
                    numbers = [
                        convert_number(x.strip())
                        for x in row.split(",")
                        if x.strip()
                    ]

                    if numbers:
                        dataset.append(numbers)

                except ValueError:
                    print("Invalid row! Please enter numbers only.")

            if not dataset:
                print("No data entered!")
                return

            data_type = "2D"

        else:
            print("Invalid choice!")
            return

    else:
        print("Invalid choice!")
        return

    update_global_summary(dataset)

    print("\nData entered successfully!")
    display_data(dataset)


# Function using *args
def calculate_summary(*values):
    """Calculate statistics using variable positional arguments."""
    if not values:
        print("No values available.")
        return

    print("\n--- Data Summary ---")
    print("Total Values:", len(values))
    print("Sum:", sum(values))
    print("Minimum:", min(values))
    print("Maximum:", max(values))
    print("Average:", sum(values) / len(values))


# Function using **kwargs
def display_dataset_info(**details):
    """Display dataset characteristics using keyword arguments."""
    print("\n--- Dataset Information ---")

    for key, value in details.items():
        print(f"{key}: {value}")


# Function to calculate average
def calculate_average(data):
    """Calculate the average of dataset values."""
    values = flatten_data(data)

    if not values:
        return 0

    return sum(values) / len(values)


# Function to find duplicates
def find_duplicates(data):
    """Find duplicate values in the dataset."""
    values = flatten_data(data)

    return list(set(
        x for x in values if values.count(x) > 1
    ))


# Function to find unique values
def find_unique(data):
    """Return unique values from the dataset."""
    return list(set(flatten_data(data)))


# Recursive function to calculate factorial
def factorial(n):
    """Calculate factorial using recursion."""
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


# Function to filter data using lambda
def filter_data(data, threshold, choice):
    """Filter values using lambda and filter()."""
    values = flatten_data(data)

    if choice == "1":
        result = list(filter(lambda x: x > threshold, values))

    elif choice == "2":
        result = list(filter(lambda x: x < threshold, values))

    else:
        print("Invalid choice!")
        return

    print("\nFiltered Data:", result)

    # Transform data using map() and lambda
    transformed = list(map(lambda x: x * 2, result))

    print("Doubled Filtered Data:", transformed)


# Function to sort data
def sort_data():
    """Sort 1D or 2D dataset."""
    global dataset

    if not dataset:
        print("Please enter data first.")
        return

    print("\n1. Ascending Order")
    print("2. Descending Order")

    choice = input("Enter your choice: ")

    reverse = choice == "2"

    if choice not in ["1", "2"]:
        print("Invalid choice!")
        return

    if data_type == "1D":

        # In-place sorting
        dataset.sort(reverse=reverse)

        print("\nSorted 1D Data:", dataset)

    else:

        # sorted() returns a new sorted list of rows
        dataset = sorted(
            dataset,
            key=lambda row: sum(row),
            reverse=reverse
        )

        print("\nSorted 2D Data (based on row sum):")

        for row in dataset:
            print(row)

    update_global_summary(dataset)


# Function returning multiple values
def calculate_statistics(data):
    """Return minimum, maximum, and average values."""
    values = flatten_data(data)

    if not values:
        return None, None, None

    minimum = min(values)
    maximum = max(values)
    average = sum(values) / len(values)

    return minimum, maximum, average


# Function to display documentation
def show_documentation():
    """Display function descriptions using __doc__."""
    print("\n--- Program Documentation ---")

    print(input_data.__doc__)
    print(calculate_summary.__doc__)
    print(factorial.__doc__)
    print(filter_data.__doc__)
    print(sort_data.__doc__)
    print(calculate_statistics.__doc__)


# Main Program
print("=" * 50)
print("WELCOME TO THE DATA ANALYZER AND TRANSFORMER PROGRAM")
print("=" * 50)

show_documentation()

while True:

    print("\n============== MAIN MENU ==============")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Find Duplicates and Unique Values")
    print("8. Display Global Dataset Summary")
    print("9. Exit Program")
    print("=======================================")

    choice = input("Please enter your choice: ")

    if choice == "1":

        input_data()

    elif choice == "2":

        if not dataset:
            print("Please input data first.")
        else:
            values = flatten_data(dataset)

            calculate_summary(*values)

            display_dataset_info(
                Dataset_Type=data_type,
                Total_Elements=len(values),
                Total_Sum=sum(values),
                Minimum=min(values),
                Maximum=max(values)
            )

    elif choice == "3":

        try:
            number = int(input("Enter a number: "))

            if number < 0:
                print("Factorial is not defined for negative numbers.")
            else:
                print("Factorial of", number, "is:", factorial(number))

        except ValueError:
            print("Please enter a valid integer.")

    elif choice == "4":

        if not dataset:
            print("Please input data first.")
        else:
            try:
                threshold = float(input("Enter threshold value: "))

                print("\n1. Values Above Threshold")
                print("2. Values Below Threshold")

                option = input("Enter your choice: ")

                filter_data(dataset, threshold, option)

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "5":

        sort_data()

    elif choice == "6":

        if not dataset:
            print("Please input data first.")
        else:
            minimum, maximum, average = calculate_statistics(dataset)

            print("\n--- Dataset Statistics ---")
            print("Minimum Value:", minimum)
            print("Maximum Value:", maximum)
            print("Average Value:", average)

    elif choice == "7":

        if not dataset:
            print("Please input data first.")
        else:
            print("Duplicate Values:", find_duplicates(dataset))
            print("Unique Values:", find_unique(dataset))

    elif choice == "8":

        print("\n--- Global Dataset Summary ---")
        print("Total Values:", dataset_summary["total_values"])
        print("Overall Mean:", dataset_summary["overall_mean"])

    elif choice == "9":

        print("\nThank you for using the Data Analyzer and Transformer Program!")
        print("Program exited successfully. Goodbye!")
        break

    else:
        print("Invalid choice! Please select between 1 and 9.")
