from collections import namedtuple

Booking = namedtuple('Booking', ['room', 'date', 'time', 'purpose', 'booker'])

conference_rooms = ['Room 1', 'Room 2', 'Room 3', 'Room 4', 'Room 5', 'Room 6', 'Room 7', 'Room 8', 'Room 9', 'Room 10', 'Room 11', 'Room 12']

def display_menu():
    print("\n" + "-"*60)
    print("{:^60}".format("Online Conference Booking System"))
    print("-" * 60)
    options = [
        "1. Book a conference room", "2. Check available conference rooms",
        "3. Check booked conference rooms", "4. Update booking",
        "5. Delete booking", "6. Exit"
    ]
    half_options = len(options) // 2
    for i in range(half_options):
        print("{:<40}{:<}".format(options[i], options[i + half_options]))
    print("-" * 60)

def check_available_rooms(bookings):
    available_rooms = [room for room in conference_rooms if not any(booking.room == room for booking in bookings)]
    return available_rooms

def display_available_rooms_columns(available_rooms):
    num_columns = (len(available_rooms) + 3) // 4
    for i in range(num_columns):
        for j in range(i, len(available_rooms), num_columns):
            print("{:<25}".format(available_rooms[j]), end="")
        print()

def book_conference_room(bookings):
    print("\nAvailable Conference Rooms:")
    available_rooms = check_available_rooms(bookings)
    display_available_rooms_columns(available_rooms)
    room_choice = input("\nChoose a room: ").strip()
    if room_choice.isdigit():
        room_index = int(room_choice) - 1
        if room_index < 0 or room_index >= len(available_rooms):
            print("Invalid room. Please choose a valid option.")
            return bookings
        chosen_room = available_rooms[room_index]
    else:
        chosen_room = room_choice.title()
        if chosen_room not in available_rooms:
            print("Invalid room. Please choose a valid option.")
            return bookings
    date = input("Enter date: ")
    time = input("Enter time: ")
    purpose = input("Enter purpose: ")
    booker = input("Enter your name: ")
    new_booking = Booking(chosen_room, date, time, purpose, booker)
    return bookings + [new_booking]

def update_booking(bookings):
    print("\nBooked Conference Rooms:")
    for i, booking in enumerate(bookings, 1):
        print(f"{i}. {booking.room}")
    booking_choice = input("Choose the booking to update: ").strip()
    if booking_choice.isdigit():
        booking_index = int(booking_choice) - 1
        if booking_index < 0 or booking_index >= len(bookings):
            print("Invalid choice. Please choose a valid booking number.")
            return bookings
        booking_to_update = bookings[booking_index]
    else:
        chosen_room = booking_choice.title()
        if chosen_room not in [booking.room for booking in bookings]:
            print("Invalid room. Please choose a valid option.")
            return bookings
        booking_to_update = next(booking for booking in bookings if booking.room == chosen_room)
    new_date = input("Enter new date: ").strip() or booking_to_update.date
    new_time = input("Enter new time: ").strip() or booking_to_update.time
    new_purpose = input("Enter new purpose: ").strip() or booking_to_update.purpose
    new_booker = input("Enter new booker name: ").strip() or booking_to_update.booker
    updated_booking = Booking(booking_to_update.room, new_date, new_time, new_purpose, new_booker)
    return [updated_booking if booking == booking_to_update else booking for booking in bookings]


def cancel_booking(bookings):
    print("\nBooked Conference Rooms:")
    for i, booking in enumerate(bookings, 1):
        print(f"{i}. {booking.room}")
    booking_choice = input("Choose the booking to cancel: ").strip()
    if booking_choice.isdigit():
        booking_index = int(booking_choice) - 1
        if booking_index < 0 or booking_index >= len(bookings):
            print("Invalid choice. Please choose a valid booking number.")
            return bookings
        return bookings[:booking_index] + bookings[booking_index+1:]
    else:
        chosen_room = booking_choice.title()
        if chosen_room not in [booking.room for booking in bookings]:
            print("Invalid room name. Please choose a valid option.")
            return
            return bookings
        return [booking for booking in bookings if booking.room != chosen_room]

def check_booked_rooms(bookings):
    return [booking.room for booking in bookings]

def display_booked_rooms_columns(booked_rooms):
    num_columns = (len(booked_rooms) + 2) // 3
    for i in range(num_columns):
        for j in range(i, len(booked_rooms), num_columns):
            print("{:<25}".format(booked_rooms[j]), end="")
        print()

def view_room_details(bookings):
    room_choice = input("\nEnter the room to view details: ").strip()
    if room_choice.isdigit():
        matching_bookings = [booking for booking in bookings if booking.room.lower() == conference_rooms[int(room_choice)-1].lower()]
    else:
        matching_bookings = [booking for booking in bookings if booking.room.lower() == room_choice.lower()]
    if not matching_bookings:
        print("No bookings found for the specified room.")
    else:
        for booking in matching_bookings:
            print(f"\nRoom: {booking.room}")
            print(f"Date: {booking.date}")
            print(f"Time: {booking.time}")
            print(f"Purpose: {booking.purpose}")
            print(f"Booker: {booking.booker}")

def display_view_details_menu():
    print("\n" + "-"*40)
    print(" " * 10 + "View Details Menu")
    print("1. Check details of a booking")
    print("2. Go back to the main menu")
    print("-" * 40)

def prompt_go_back_or_exit():
    while True:
        choice = input("Enter your choice: ")
        if choice == '1':
            return True
        elif choice == '2':
            return False
        else:
            print("Invalid choice. Please enter 1 or 2.")

def display_option3_menu():
    print("\nOptions:")
    print("1. Check details of a booked room")
    print("2. Go back to main menu")
    print("3. Exit")

def display_go_back_exit_menu():
    print("\nOptions:")
    print("1. Go back to main menu")
    print("2. Exit")

if __name__ == "__main__":
    bookings = []
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")
        if choice == '1':
            bookings = book_conference_room(bookings)
            print("\nBooking successful.")
        elif choice == '2':
            print("\nAvailable Conference Rooms:")
            available_rooms = check_available_rooms(bookings)
            display_available_rooms_columns(available_rooms)
            display_go_back_exit_menu()
            if not prompt_go_back_or_exit():
                print("Exiting...Thank you!")
                break
        elif choice == '3':
            booked_rooms = check_booked_rooms(bookings)
            if not booked_rooms:
                print("\nNo conference rooms are currently booked.")
                display_go_back_exit_menu()
                if not prompt_go_back_or_exit():
                    print("Exiting...Thank you!")
                    break
                continue
            else:
                print("\nBooked Conference Rooms:")
                if len(booked_rooms) <= 3:
                    print(", ".join(booked_rooms))
                else:
                    display_booked_rooms_columns(booked_rooms)
                while True:
                    display_option3_menu()
                    choice_option3 = input("Enter your choice: ").strip()
                    if choice_option3 == '1':
                        view_room_details(bookings)
                    elif choice_option3 == '2':
                        break
                    elif choice_option3 == '3':
                        print("Exiting...Thank you!")
                        exit()
                    else:
                        print("Invalid choice. Please select a valid option.")
        elif choice == '4':
            if not bookings:
                print("\nNo conference rooms are currently booked.")
                display_go_back_exit_menu()
                if not prompt_go_back_or_exit():
                    print("Exiting...Thank you!")
                    break
            else:
                bookings = update_booking(bookings)
                print("Booking updated successfully.")
        elif choice == '5':
            if not bookings:
                print("\nNo conference rooms are currently booked.")
                display_go_back_exit_menu()
                if not prompt_go_back_or_exit():
                    print("Exiting...Thank you!")
                    break
            else:
                bookings = cancel_booking(bookings)
                print("Booking canceled successfully.")
        elif choice == '6':
            print("Exiting...Thank you!")
            break
        else:
            print("Invalid choice. Please select a valid option from the menu.")