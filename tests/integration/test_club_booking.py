import pytest
from datetime import datetime
from club.member import Member
from club.room import Room
from club.club import Club


@pytest.fixture
def initialize_club():
    room = Room(room_id="T1", sport_type="tennis", capacity=2)
    member = Member(name="Dave", funds=200.0)
    club = Club(rooms=[room], members=[member])
    return club, room, member


def test_booking_decreases_room_capacity(initialize_club):
    club, room, member = initialize_club
    start = datetime(2025, 6, 1, 10, 0)
    
    club.make_booking(member, room, start)
    
    assert len(room.members) == 1
    assert room.has_capacity() is True
    assert member in room.members

    assert len(club.bookings) == 1


def test_booking_deducts_member_funds(initialize_club):
    club, room, member = initialize_club
    start = datetime(2025, 6, 1, 10, 0)
    
    club.make_booking(member, room, start)
    
    assert member.funds == 170.0


def test_booking_fails_outside_opening_hours(initialize_club):
    club, room, member = initialize_club
    start = datetime(2025, 6, 1, 23, 0)
    
    with pytest.raises(ValueError, match="within opening hours"):
        club.make_booking(member, room, start)
        
    assert len(room.members) == 0
    assert member.funds == 200.0 


def test_get_room_by_type(initialize_club):
    club, room, _ = initialize_club
    assert club.get_room_by_type("tennis") == room
    assert club.get_room_by_type("badminton") is None


def test_booking_fails_if_no_funds(initialize_club):
    club, room, member = initialize_club
    member.funds = 10.0
    start = datetime(2025, 6, 1, 10, 0)
    
    with pytest.raises(ValueError, match="Insufficient funds"):
        club.make_booking(member, room, start)
        
    assert len(room.members) == 0
    assert len(club.bookings) == 0
