import unittest
from py_client import Client, LoginRequestModel

class TestUserModule(unittest.TestCase):

  def setUp(self) -> None:
    self.client = Client('https://norenapi.thefirstock.com')

  def test_login(self):
    """
    Test if login method is working
    """
    model = LoginRequestModel(
      apkversion = "1.0.0",
      appkey = 'abcd',
      vc = '12341234',
      uid = "TV0001",
      pwd = "Trade$666",
      factor2 = "AEQPV7108A",
      imei = "134243434",
      source = "MOB"
    )

    response = self.client.login(model)
    # assertions
    if response.stat == 'Ok':
      assert response.susertoken is not None
    else:
      assert response.emsg is not None
