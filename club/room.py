from typing import List
from club.member import Member


class Room:
    def __init__(self, room_id: str, sport_type: str, capacity: int):
        self.room_id = room_id
        if sport_type not in ("tennis", "badminton", "squash"):
            raise ValueError(f"Invalid sport type: {sport_type}")
        self.sport_type = sport_type
        self.capacity = capacity
        self.is_available = True
        self.members: List[Member] = []

    def has_capacity(self) -> bool:
        return len(self.members) < self.capacity

    def book(self, member: Member) -> None:
        if not self.is_available:
            raise ValueError("Room is not available")
        if not self.has_capacity():
            raise ValueError("Room is at full capacity")
        if member in self.members:
            raise ValueError("Member is already in the room")
            
        self.members.append(member)

    def release(self, member: Member) -> None:
        if member not in self.members:
            raise ValueError("Member is not in the room")
        self.members.remove(member)
