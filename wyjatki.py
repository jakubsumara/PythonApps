class ReservationException(Exception):
    pass

class NoAvailableSeatsException(ReservationException):
    def __init__(self, message="No available seats for this screening."):
        self.message = message
        super().__init__(self.message)

class SeatAlreadyReservedException(ReservationException):
    def __init__(self, message="This seat is already reserved."):
        self.message = message
        super().__init__(self.message)

class UserAlreadyReservedException(ReservationException):
    def __init__(self, message="This user has already reserved a seat."):
        self.message = message
        super().__init__(self.message)

class InvalidCancellationException(ReservationException):
    def __init__(self, message="Invalid cancellation attempt."):
        self.message = message
        super().__init__(self.message)

class Cinema:
    def __init__(self, rows, cols):
        self.seats = {f"{chr(65 + r)}{c+1}": None for r in range(rows) for c in range(cols)}
        self.user_reservations = {}

    def reserve_seat(self, seat, user):
        if seat not in self.seats:
            raise ValueError(f"Seat {seat} does not exist.")

        if all(value is not None for value in self.seats.values()):
            raise NoAvailableSeatsException()

        if self.seats[seat] is not None:
            raise SeatAlreadyReservedException()

        if user in self.user_reservations:
            raise UserAlreadyReservedException()

        self.seats[seat] = user
        self.user_reservations[user] = seat

    def cancel_reservation(self, seat, user):
        if seat not in self.seats:
            raise ValueError(f"Seat {seat} does not exist.")

        if self.seats[seat] != user:
            raise InvalidCancellationException()

        self.seats[seat] = None
        del self.user_reservations[user]

    def display_seating(self):
        for seat, user in self.seats.items():
            status = f"{seat}: {'Available' if user is None else f'Reserved by {user}'}"
            print(status)

cinema = Cinema(5, 5)

try:
    cinema.reserve_seat("A1", "Jan Kowalski")
    cinema.reserve_seat("B2", "Anna Nowak")
    cinema.reserve_seat("A1", "Piotr Wiśniewski")  # Powinien zgłosić wyjątek
except ReservationException as e:
    print(e)

try:
    cinema.cancel_reservation("A1", "Jan Kowalski")
    cinema.cancel_reservation("A1", "Anna Nowak")  # Powinien zgłosić wyjątek
except ReservationException as e:
    print(e)

cinema.display_seating()
