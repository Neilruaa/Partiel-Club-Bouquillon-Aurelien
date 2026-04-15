from datetime import datetime
from typing import List, Optional
from club.member import Member
from club.room import Room
from club.booking import Booking


class Club:
    OPENING_HOUR = 8
    CLOSING_HOUR = 22

    def __init__(self, rooms: List[Room], members: List[Member]):
        self.rooms = rooms
        self.members = members
        self.bookings: List[Booking] = []

    def is_within_hours(self, start_time: datetime) -> bool:
        return self.OPENING_HOUR <= start_time.hour < self.CLOSING_HOUR

    def get_room_by_type(self, sport_type: str) -> Optional[Room]:
        for room in self.rooms:
            if room.sport_type == sport_type and room.is_available and room.has_capacity():
                return room
        return None

    def make_booking(self, member: Member, room: Room, start_time: datetime) -> Booking:
        if not self.is_within_hours(start_time):
            raise ValueError("Booking must be within opening hours (8am to 10pm)")
        
        if room not in self.rooms:
            raise ValueError("Room does not exist")
        if member not in self.members:
            raise ValueError("Member is not registered in this club")
            
        price = Booking.compute_price(member, room.sport_type)
        
        member.charge(price)
        
        try:
            room.book(member)
        except ValueError as e:
            member.funds += price
            raise e

        booking = Booking(member, room, start_time)
        self.bookings.append(booking)
        return booking

    def load_bookings_from_api(self) -> None:
        pass
