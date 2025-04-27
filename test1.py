import pytest

@pytest.mark.run(order=2)
def test_sending_mail_1(set_up):
   print("Письмо 1")


@pytest.mark.run(order=3)
def test_sending_mail_2(set_up):
   print("Письмо 2")


@pytest.mark.run(order=1)
def test_sending_mail_3(set_up):
   print("Письмо 3")


@pytest.mark.run(order=6)
def test_sending_mail_4(set_up):
   print("Письмо 4")


@pytest.mark.run(order=4)
def test_sending_mail_5(set_up,):
   print("Письмо 5")


@pytest.mark.run(order=5)
def test_sending_mail_6(set_up):
   print("Письмо 6")
