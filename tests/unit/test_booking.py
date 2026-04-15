import pytest
from datetime import datetime
from club.member import Member
from club.room import Room
from club.booking import Booking


@pytest.fixture
def member_non_premium():
    return Member("Alice", 100.0, is_premium=False)


@pytest.fixture
def member_premium():
    return Member("Bob", 100.0, is_premium=True)


@pytest.fixture
def room_tennis():
    return Room("T1", "tennis", 2)


@pytest.fixture
def room_badminton():
    return Room("B1", "badminton", 4)


@pytest.fixture
def room_squash():
    return Room("S1", "squash", 2)


@pytest.fixture
def start_time():
    return datetime(2025, 6, 1, 10, 0)


def test_booking_initialization(member_non_premium, room_tennis, start_time):
    booking = Booking(member_non_premium, room_tennis, start_time)
    assert type(booking.booking_id) is str
    assert booking.member == member_non_premium
    assert booking.room == room_tennis
    assert booking.start_time == start_time
    assert booking.price == 30.0


def test_compute_price_tennis_non_premium(member_non_premium, room_tennis, start_time):
    booking = Booking(member_non_premium, room_tennis, start_time)
    assert booking.price == 30.0


def test_compute_price_tennis_premium(member_premium, room_tennis, start_time):
    booking = Booking(member_premium, room_tennis, start_time)
    assert booking.price == 11.0


def test_compute_price_badminton_non_premium(member_non_premium, room_badminton, start_time):
    booking = Booking(member_non_premium, room_badminton, start_time)
    assert booking.price == 20.0


def test_compute_price_badminton_premium(member_premium, room_badminton, start_time):
    booking = Booking(member_premium, room_badminton, start_time)
    assert booking.price == 10.0


def test_compute_price_squash_non_premium(member_non_premium, room_squash, start_time):
    booking = Booking(member_non_premium, room_squash, start_time)
    assert booking.price == 15.0


def test_compute_price_squash_premium(member_premium, room_squash, start_time):
    booking = Booking(member_premium, room_squash, start_time)
    assert booking.price == 9.0


def test_compute_price_invalid_sport(member_non_premium):
    with pytest.raises(ValueError, match="Unknown sport type"):
        Booking.compute_price(member_non_premium, "football")
