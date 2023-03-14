from checkout import Checkout
import pytest
@pytest.fixture()
def checkout():
    checkout=Checkout()
    return checkout

def test_Canadditem(checkout):
    checkout.add_item("sam",1)
    checkout.add_item("sammy",2)
    checkout.add_item("samarth",4)
    checkout.add_item_in_cart("sam")
    checkout.add_item_in_cart("samarth")
    assert checkout.calculate_total()==5