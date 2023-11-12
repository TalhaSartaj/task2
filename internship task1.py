def get_valid_input(prompt, error_message, validator_func):
    while True:
        try:
            value = int(input(prompt))
            if validator_func(value):
                return value
            else:
                print(error_message)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def validate_positive(value):
    return value > 0


def calculate_total_cost(num_passengers, ticket_price, group_discount_threshold, group_discount_tickets):
    total_cost = num_passengers * ticket_price
    if group_discount_threshold <= num_passengers <= group_discount_tickets:
        free_tickets = num_passengers // 10
        total_cost -= free_tickets * ticket_price
    return total_cost


def display_tickets_available(departure_times, available_tickets):
    print("\nAvailable Tickets:")
    for time, tickets in zip(departure_times, available_tickets):
        if tickets == 0:
            print(f"{time} - Closed")
        else:
            print(f"{time} - {tickets} tickets available")


def purchase_tickets(available_tickets, ticket_price, group_discount_threshold, group_discount_tickets):
    departure_times = ["09:00", "11:00", "13:00", "15:00"]
    return_times = ["10:00", "12:00", "14:00", "16:00"]

    total_passengers = 0
    total_money = 0
    max_passengers = 0
    max_passengers_train = ""

    for i, time in enumerate(departure_times):
        num_passengers = get_valid_input(f"Enter the number of passengers when the train leaves at {time}: ",
                                         "Number of passengers must be positive.", validate_positive)

        if available_tickets[i] >= num_passengers:
            total_cost = calculate_total_cost(num_passengers, ticket_price, group_discount_threshold,
                                              group_discount_tickets)
            available_tickets[i] -= num_passengers

            print(f"\nTickets purchased for {num_passengers} passengers when the train leaves at {time}.")
            print(f"Total Cost: ${total_cost}")

            # Update totals
            total_passengers += num_passengers
            total_money += total_cost

            # Check for max passengers
            if num_passengers > max_passengers:
                max_passengers = num_passengers
                max_passengers_train = time

        else:
            print(f"Not enough tickets available for {num_passengers} passengers when the train leaves at {time}.")

    return available_tickets, total_passengers, total_money, max_passengers_train


def main():
    # Constants
    coaches_per_train = 6
    seats_per_coach = 80
    ticket_price = 25
    group_discount_threshold = 10
    group_discount_tickets = 80

    # Initialize available tickets for each train
    available_tickets = [coaches_per_train * seats_per_coach] * len(departure_times)

    print("Electric Mountain Railway Program")
    display_tickets_available(departure_times, available_tickets)

    # Purchase tickets
    available_tickets, total_passengers, total_money, max_passengers_train = purchase_tickets(
        available_tickets, ticket_price, group_discount_threshold, group_discount_tickets
    )

    # Display results
    print("\nSummary:")
    print(f"Total Passengers for the Day: {total_passengers}")
    print(f"Total Money Taken for the Day: ${total_money}")
    print(f"Train Journey with Most Passengers: {max_passengers_train} with {max_passengers} passengers")

    # Update display after purchases
    display_tickets_available(departure_times, available_tickets)


if __name__ == "__main__":
    main()
