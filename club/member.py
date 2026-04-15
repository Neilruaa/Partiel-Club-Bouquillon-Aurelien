class Member:
    
    def __init__(self, name: str, funds: float, is_premium: bool = False):
        self.name = name
        self.funds = funds
        self.is_premium = is_premium

    def subscribe_premium(self) -> None:
        if self.funds < 200.0:
            raise ValueError("Insufficient funds to subscribe to premium")
        self.funds -= 200.0
        self.is_premium = True

    def can_afford(self, amount: float) -> bool:
        return self.funds >= amount

    def charge(self, amount: float) -> None:
        if not self.can_afford(amount):
            raise ValueError("Insufficient funds")
        self.funds -= amount
