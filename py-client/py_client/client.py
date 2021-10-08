"""
The client combines all the modules and abstracts the inner logic
"""
from py_client.modules.watchlists.datasource import WatchListDataSource
from .modules.users import LoginRequestModel, LogoutRequestModel
from .modules.users import UserDataSource
from .utils.stateful import Stateful

__all__ = ['Client']

class Client(Stateful):
  """
  The python client for communicating with external api
  """
  def __init__(self, base_url: str = None) -> None:
    """
    Initialize the client

    Args:
      base_url (str, optional): The base url for the rest api endpoint. Defaults to None.
    """
    super().__init__({
      "token": None
    })
    self.__setup__()
    self.__users = UserDataSource(base_url, interceptors=self._interceptors, state = self.state)
    self.__watchlists = WatchListDataSource(base_url, interceptors=self._interceptors, state=self.state)

  def __setup__(self) -> None:
    """
    Initial setup for the client
    """
    self._interceptors = []

  @property
  def state(self):
    """The current client state"""
    return self.__state__

  @property
  def users(self) -> UserDataSource:
    """
    The user module datasource
    """
    return self.__users

  @property
  def watchlists(self) -> WatchListDataSource:
    """
    The watchlists module datasource
    """
    return self.__watchlists

  def login(self, model: LoginRequestModel):
    """
    Send a login request to rest api. Alias for ```client.users.login```

    Args:
      model (LoginRequestModel): The data to be send as LoginRequestModel instance.

    Returns:
      LoginResponseModel: The response from login request as LoginResponseModel instance.
    """
    response = self.__users.login(model)
    # set state token if successful
    if response.susertoken is not None:
      self.set_state('token', response.susertoken)
    return response

  def logout(self, model: LogoutRequestModel, key: str):
    """
    Send a logout request to rest api. Alias for ```client.users.logout```

    Args:
      model (LogoutRequestModel): The data to be send as LogoutRequestModel instance
      key (str): The key obtained on login success

    Returns:
      LogoutResponseModel: The response from logout request as LogoutResponseModel instance
    """
    return self.__users.logout(model, key)