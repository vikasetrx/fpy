"""
The data source for all watchlist specific requests
"""

from ...utils.datasources import RestDataSource
from . import endpoints

from .models.get_names import GetWatchListNamesRequestModel, GetWatchListNamesResponseModel
from .models.get_watchlist import GetWatchListRequestModel, GetWatchListResponseModel
from .models.search_scrips import SearchScripsRequestModel, SearchScripsResponseModel
from .models.add_scrips import AddScripsRequestModel, AddScripsResponseModel
from .models.delete_scrips import DeleteScripsRequestModel, DeleteScripsResponseModel
from .models.get_security_info import GetSecurityInfoRequestModel, GetSecurityInfoResponseModel
from .models.get_quotes import GetQuotesRequestModel, GetQuotesResponseModel
from .models.get_predefined_watchlists import GetPredefinedWatchListsRequestModel, GetPredefinedWatchListsResponseModel
from .models.get_predefined_scrips import GetPredefinedScripsRequestModel, GetPredefinedScripsResponseModel

class WatchListDataSource(RestDataSource):
  """
  The datasource for all watch list specific requests
  """

  def get_names(self, model: GetWatchListNamesRequestModel, key: str = None) -> GetWatchListNamesResponseModel:
    """
    Fetch watchlist names

    Args:
      model (GetWatchListNamesRequestModel): The data to be send as GetWatchListNamesRequestModel.
      key (str): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      GetWatchListNamesResponseModel: The response as GetWatchListNamesResponseModel.
    """
    # get key from saved state if not passed explicitly
    key = self.get_state('token') if key is None else key
    # convert request model to json string
    request_json = model.json(exclude_unset=True)
    # send the post request to get the json response
    response_json = self.post(endpoints.GET_NAMES, f"jData={request_json}&jKey={key}")
    # convert the request to response model
    return GetWatchListNamesResponseModel.parse_raw(response_json)

  def get_watchlist(self, model: GetWatchListRequestModel, key: str = None) -> GetWatchListResponseModel:
    """
    Get scrip list for a given watchlist name

    Args:
      model (GetWatchListRequestModel): The data to be send as GetWatchListRequestModel.
      key (str): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      GetWatchListResponseModel: The response as GetWatchListResponseModel.
    """
    # get key from saved state if not passed explicitly
    key = self.get_state('token') if key is None else key
    # convert request model to json string
    request_json = model.json(exclude_unset=True)
    # send the post request to get the json response
    response_json = self.post(endpoints.GET_WATCHLIST, f"jData={request_json}&jKey={key}")
    # convert the request to response model
    return GetWatchListResponseModel.parse_raw(response_json)

  def search_scrips(self, model: SearchScripsRequestModel, key: str = None) -> SearchScripsResponseModel:
    """
    Search for scrips

    Args:
      model (SearchScripsRequestModel): The data to be send as SearchScripsRequestModel.
      key (str): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      SearchScripsResponseModel: The response as SearchScripsResponseModel.
    """
    # get key from saved state if not passed explicitly
    key = self.get_state('token') if key is None else key
    # convert request model to json string
    request_json = model.json(exclude_unset=True)
    # send the post request to get the json response
    response_json = self.post(endpoints.SEARCH_SCRIPS, f"jData={request_json}&jKey={key}")
    # convert the request to response model
    return SearchScripsResponseModel.parse_raw(response_json)

  def add_scrips(self, model: AddScripsRequestModel, key: str = None) -> AddScripsResponseModel:
    """
    Add multiple scrips to a watchlist

    Args:
      model (AddScripsRequestModel): The data to be send as AddScripsRequestModel.
      key (str): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      AddScripsResponseModel: The response as AddScripsResponseModel.
    """
    # get key from saved state if not passed explicitly
    key = self.get_state('token') if key is None else key
    # convert request model to json string
    request_json = model.json(exclude_unset=True)
    # send the post request to get the json response
    response_json = self.post(endpoints.ADD_SCRIPS, f"jData={request_json}&jKey={key}")
    # convert the request to response model
    return AddScripsResponseModel.parse_raw(response_json)

  def delete_scrips(self, model: DeleteScripsRequestModel, key: str = None) -> DeleteScripsResponseModel:
    """
    Delete scrips from a watchlist

    Args:
      model (DeleteScripsRequestModel): The data to be send as DeleteScripsRequestModel.
      key (str): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      DeleteScripsResponseModel: The response as DeleteScripsResponseModel.
    """
    # get key from saved state if not passed explicitly
    key = self.get_state('token') if key is None else key
    # convert request model to json string
    request_json = model.json(exclude_unset=True)
    # send the post request to get the json response
    response_json = self.post(endpoints.DELETE_SCRIPS, f"jData={request_json}&jKey={key}")
    # convert the request to response model
    return DeleteScripsResponseModel.parse_raw(response_json)

  def get_security_info(self, model: GetSecurityInfoRequestModel, key: str = None) -> GetSecurityInfoResponseModel:
    """
    Get security info

    Args:
      model (GetSecurityInfoRequestModel): The data to be send as GetSecurityInfoRequestModel.
      key (str): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      GetSecurityInfoResponseModel: The response as GetSecurityInfoResponseModel.
    """
    # get key from saved state if not passed explicitly
    key = self.get_state('token') if key is None else key
    # convert request model to json string
    request_json = model.json(exclude_unset=True)
    # send the post request to get the json response
    response_json = self.post(endpoints.GET_SECURITY_INFO, f"jData={request_json}&jKey={key}")
    # convert the request to response model
    return GetSecurityInfoResponseModel.parse_raw(response_json)

  def get_quotes(self, model: GetQuotesRequestModel, key: str = None) -> GetQuotesResponseModel:
    """
    Get quotes

    Args:
      model (GetQuotesRequestModel): The data to be send as GetQuotesRequestModel.
      key (str): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      GetQuotesResponseModel: The response as GetQuotesResponseModel.
    """
    # get key from saved state if not passed explicitly
    key = self.get_state('token') if key is None else key
    # convert request model to json string
    request_json = model.json(exclude_unset=True)
    # send the post request to get the json response
    response_json = self.post(endpoints.GET_QUOTES, f"jData={request_json}&jKey={key}")
    # convert the request to response model
    return GetQuotesResponseModel.parse_raw(response_json)

  def get_predefined_watchlists(self, model: GetPredefinedWatchListsRequestModel, key: str = None) -> GetPredefinedWatchListsResponseModel:
    """
    Get list of predefined MWs

    Args:
      model (GetPredefinedWatchListsRequestModel): The data to be send as GetPredefinedWatchListsRequestModel.
      key (str): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      GetPredefinedWatchListsResponseModel: The response as GetPredefinedWatchListsResponseModel.
    """
    # get key from saved state if not passed explicitly
    key = self.get_state('token') if key is None else key
    # convert request model to json string
    request_json = model.json(exclude_unset=True)
    # send the post request to get the json response
    response_json = self.post(endpoints.GET_PREDEFINED_WATCHLISTS, f"jData={request_json}&jKey={key}")
    # convert the request to response model
    return GetPredefinedWatchListsResponseModel.parse_raw(response_json)

  def get_predefined_scrips(self, model: GetPredefinedScripsRequestModel, key: str = None) -> GetPredefinedScripsResponseModel:
    """
    Get list of predefined MW scrips

    Args:
      model (GetPredefinedScripsRequestModel): The data to be send as GetPredefinedScripsRequestModel.
      key (str): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      GetPredefinedScripsResponseModel: The response as GetPredefinedScripsResponseModel.
    """
    # get key from saved state if not passed explicitly
    key = self.get_state('token') if key is None else key
    # convert request model to json string
    request_json = model.json(exclude_unset=True)
    # send the post request to get the json response
    response_json = self.post(endpoints.GET_PREDEFINED_WATCHLISTS, f"jData={request_json}&jKey={key}")
    # convert the request to response model
    return GetPredefinedScripsResponseModel.parse_raw(response_json)