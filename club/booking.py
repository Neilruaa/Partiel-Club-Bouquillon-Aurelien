from datetime import datetime
import uuid
from club.member import Member
from club.room import Room


class Booking:
    PRICES = {
        "tennis": {"premium": 11.0, "non_premium": 30.0},
        "badminton": {"premium": 10.0, "non_premium": 20.0},
        "squash": {"premium": 9.0, "non_premium": 15.0},
    }

    def __init__(self, member: Member, room: Room, start_time: datetime):
        self.booking_id = str(uuid.uuid4())
        self.member = member
        self.room = room
        self.start_time = start_time
        self.price = self.compute_price(member, room.sport_type)

    @classmethod
    def compute_price(clas, member: Member, sport_type: str) -> float:
        if sport_type not in clas.PRICES:
            raise ValueError(f"Unknown sport type: {sport_type}")
        
        tier = "premium" if member.is_premium else "non_premium"
        return clas.PRICES[sport_type][tier]
