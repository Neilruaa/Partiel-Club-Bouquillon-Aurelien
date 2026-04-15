import pytest
from club.member import Member
from club.room import Room


def test_room_initialization():
    room = Room("T1", "tennis", 2)
    assert room.room_id == "T1"
    assert room.sport_type == "tennis"
    assert room.capacity == 2
    assert room.is_available is True
    assert room.members == []


def test_room_initialization_invalid_sport():
    with pytest.raises(ValueError, match="Invalid sport type"):
        Room("X1", "football", 10)


def test_has_capacity():
    room = Room("S1", "squash", 2)
    assert room.has_capacity() is True
    
    m1 = Member("Alice", 100)
    m2 = Member("Bob", 100)
    
    room.book(m1)
    assert room.has_capacity() is True
    
    room.book(m2)
    assert room.has_capacity() is False


def test_book_adds_member():
    room = Room("B1", "badminton", 4)
    m = Member("Alice", 100)
    room.book(m)
    assert m in room.members


def test_book_fails_when_full():
    room = Room("T1", "tennis", 1)
    m1 = Member("Alice", 100)
    m2 = Member("Bob", 100)
    
    room.book(m1)
    with pytest.raises(ValueError, match="Room is at full capacity"):
        room.book(m2)


def test_book_fails_when_unavailable():
    room = Room("T1", "tennis", 2)
    room.is_available = False
    m = Member("Alice", 100)
    
    with pytest.raises(ValueError, match="Room is not available"):
        room.book(m)


def test_book_fails_if_already_in_room():
    room = Room("T1", "tennis", 2)
    m = Member("Alice", 100)
    room.book(m)
    with pytest.raises(ValueError, match="Member is already in the room"):
        room.book(m)


def test_release_removes_member():
    room = Room("T1", "tennis", 2)
    m = Member("Alice", 100)
    room.book(m)
    
    room.release(m)
    assert m not in room.members
    assert room.has_capacity() is True


def test_release_fails_if_member_not_in_room():
    room = Room("T1", "tennis", 2)
    m = Member("Alice", 100)
    with pytest.raises(ValueError, match="Member is not in the room"):
        room.release(m)
