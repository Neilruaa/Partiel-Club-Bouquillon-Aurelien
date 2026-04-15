import pytest
from club.member import Member

def test_can_afford_returns_true_when_funds_sufficient():
    member = Member(name="Alice", funds=50.0)
    assert member.can_afford(30.0) is True
    assert member.can_afford(50.0) is True

def test_can_afford_returns_false_when_funds_insufficient():
    member = Member(name="Alice", funds=10.0)
    assert member.can_afford(30.0) is False

def test_charge_deducts_funds():
    member = Member(name="Bob", funds=100.0)
    member.charge(20.0)
    assert member.funds == 80.0

def test_charge_raises_when_insufficient_funds():
    member = Member(name="Bob", funds=5.0)
    with pytest.raises(ValueError, match="Insufficient funds"):
        member.charge(20.0)

def test_subscribe_premium_sets_flag_and_deducts():
    member = Member(name="Carol", funds=300.0)
    member.subscribe_premium()
    assert member.is_premium is True
    assert member.funds == 100.0

def test_subscribe_premium_fails_when_insufficient_funds():
    member = Member(name="Dave", funds=150.0)
    with pytest.raises(ValueError, match="Insufficient funds to subscribe to premium"):
        member.subscribe_premium()
    assert member.is_premium is False
    assert member.funds == 150.0
