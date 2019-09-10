from Checkout import Checkout
import pytest


@pytest.fixture
def checkout():
    checkout = Checkout()
    checkout.addItemPrice("A", 50)
    checkout.addItemPrice("B", 30)
    checkout.addItemPrice("D", 15)
    checkout.addItemPrice("C", 20)
    return checkout


# def test_CanCalculateTotal(checkout):
#     checkout.addItem("A")
#     assert checkout.calculateTotal() == 50


# def test_GetCorrectTotalWIthMultipleItems(checkout):
#     checkout.addItem("A")
#     checkout.addItem("B")
#     checkout.addItem("C")
#     checkout.addItem("D")
#     assert checkout.calculateTotal() == 115


# def test_CanAddDiscountRule(checkout):
#     checkout.addDiscount("A", 2, 100)
#     checkout.addDiscount("A", 3, 130)
#     checkout.addDiscount("A", 4, 180)
#     checkout.addDiscount("A", 5, 230)
#     checkout.addDiscount("A", 6, 260)
    # checkout.addDiscount("B", 2, 45)

def test_CanApplyDiscountRule(checkout):
    # checkout.addDiscount("A",2,100)
    checkout.addDiscount("A", 3, 130)
    # checkout.addDiscount("A", 4, 180)
#     checkout.addDiscount("A", 5, 230)
#     checkout.addDiscount("A", 6, 260)
    checkout.addDiscount("B", 2, 45)
    checkout.addItem("A")
    checkout.addItem("A")
    checkout.addItem("A")
    checkout.addItem("B")
    checkout.addItem("B")
    checkout.addItem("D")

    return print("The Total price to be paid =",checkout.calculateTotal())
