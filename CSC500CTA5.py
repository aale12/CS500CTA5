# Anthony Le
# CSC500 - Principles of Programming
# Critical Thinking Assignment 5

# This program contains two functions:
# The first function uses nested loops to collect data and calulate the average rainfall over a number of years.
# The second function displays the number of points earned by a student from buying books at a bookstore.
# If a customer purchases 0 books, they earn 0 points.
# If a customer purchases 2 books, they earn 5 points.
# If a customer purchases 4 books, they earn 15 points.
# If a customer purchases 6 books, they earn 30 points.
# If a customer purchases 8 or more books, they earn 60 points.


# Function to collect rainfall data and calculate total and average rainfall
def collect_rainfall_data():
    # Prompt user to enter the number of years
    while True:
        try:
            num_years = int(input("Enter the number of years: "))
            # Ensure the number of years is a positive integer
            if num_years > 0:
                break
            else:
                print("Please enter a positive integer for the number of years.")
        # Handle non-integer inputs
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    total_rainfall = 0.0  # Initialize total rainfall

    # Loop through each year
    for year in range(1, num_years + 1):
        print(f"\nYear {year}:")
        # Loop through each month
        months = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ]
        for month in range(12):
            while True:
                # Prompt user to enter the rainfall for the month
                try:
                    monthly_rainfall = float(
                        input(
                            f"  Enter the rainfall for month {months[month]} (in inches): "
                        )
                    )
                    # Ensure the rainfall is a non-negative number
                    if monthly_rainfall >= 0:
                        total_rainfall += monthly_rainfall  # Add to total rainfall
                        break
                    else:
                        print("Please enter a non-negative value for rainfall.")
                # Handle non-float inputs
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

    # Calculate average monthly rainfall
    total_months = num_years * 12
    average_rainfall = total_rainfall / total_months

    # Print results
    print(f"\nTotal months: {total_months}")
    print(f"Total inches of rainfall: {total_rainfall:.2f}")
    print(f"Average monthly rainfall: {average_rainfall:.2f} inches")


# Function to calculate and display bookstore points based on number of books purchased
def bookstore_points():
    # Prompt user to enter the number of books purchased
    while True:
        try:
            num_books = int(input("Enter the number of books purchased: "))
            # Ensure the number of books is a non-negative integer
            if num_books >= 0:
                break
            else:
                print("Please enter a non-negative integer for the number of books.")
        # Handle non-integer inputs
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Determine points based on the number of books purchased
    if num_books < 2:
        points = 0
    elif 2 <= num_books <= 3:
        points = 5
    elif 4 <= num_books <= 5:
        points = 15
    elif 6 <= num_books <= 7:
        points = 30
    elif num_books >= 8:
        points = 60
    else:
        points = 0  # Default case (should not be reached)

    # Print the number of points earned
    print(f"Points earned: {points}")


# Main function
if __name__ == "__main__":
    # Prompt the user to choose which function they want to run
    while True:
        choice = (
            input(
                "\nChoose a function to run:\n1. Collect Rainfall Data\n2. Bookstore Points\nQ. Quit\nEnter 1, 2, or Q: "
            )
            .strip()
            .lower()
        )
        if choice == "1":
            collect_rainfall_data()  # Call the rainfall data function
        elif choice == "2":
            bookstore_points()  # Call the bookstore points function
        elif choice == "q":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or Q.")
