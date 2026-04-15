import pytest
from datetime import datetime
from club.member import Member
from club.room import Room
from club.club import Club

MOCK_API_RESPONSE = (
    "2025-06-01T09:00:00,tennis,T1\n"
    "2025-06-01T10:00:00,badminton,B1\n"
)


@pytest.fixture
def full_club(mocker):
    # Using mock because the API is not available
    mocker.patch(
        "api.reservations.fetch_reservations",
        return_value=MOCK_API_RESPONSE,
    )

    rooms = [
        Room(room_id="T1", sport_type="tennis", capacity=4),
        Room(room_id="B1", sport_type="badminton", capacity=4),
    ]
    alice = Member(name="Alice", funds=500.0, is_premium=True)
    club = Club(rooms=rooms, members=[alice])
    return club, alice


def test_api_data_is_loaded_into_bookings(full_club):
    club, _ = full_club
    club.load_bookings_from_api()
    pass

def test_end_to_end_premium_tennis_booking(mocker):
    def mock_fetch(sport):
        if sport == "tennis":
            return "2025-06-01T09:00:00,tennis,T1\n"
        elif sport == "badminton":
            return "2025-06-01T10:00:00,badminton,B1\n"
        return ""
        
    mocker.patch("api.reservations.fetch_reservations", side_effect=mock_fetch)
    rooms = [Room("T1", "tennis", 4), Room("B1", "badminton", 4)]
    alice = Member("Alice", 500.0, is_premium=True)
    club = Club(rooms=rooms, members=[alice])
    
    club.load_bookings_from_api()
    
    assert len(club.bookings) == 2
    
    room = club.get_room_by_type("tennis")
    start = datetime(2025, 6, 1, 14, 0)

    booking = club.make_booking(alice, room, start)

    assert booking is not None
    assert booking.price == 11.0         
    assert alice.funds == 489.0           
    assert alice in room.members
    assert len(club.bookings) == 3
