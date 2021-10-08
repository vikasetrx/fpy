"""
The request and response models for delete scrips from watchlist request
"""

from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel

from ....common.enums import ResponseStatus
from ....utils.decoders import build_loader, datetime_decoder
from ....utils.encoders import build_dumber, list_encoder

__all__ = ['DeleteScripsRequestModel', 'DeleteScripsResponseModel']

class DeleteScripsRequestModel(BaseModel):
  """
  The request model for delete scrips from watchlist endpoint
  """
  uid: str
  """The user id of the login user"""
  wlname: str
  """Name of the Watchlist, for which scrip list is required"""
  scrips: List[str]
  """List of scrips"""
  class Config:
    """model configuration"""
    json_dumps = build_dumber({
      "scrips": list_encoder('|')
    })

class DeleteScripsResponseModel(BaseModel):
  """
  The response model for delete scrips from watchlist endpoint
  """
  stat: ResponseStatus
  """The delete scrips success or failure status"""
  request_time: Optional[datetime]
  """It will be present only on successful logout."""
  emsg: Optional[str]
  """Error message if the logout failed"""

  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder()
    })