"""
Request and response models for logout
"""
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from ....common.enums import ResponseStatus
from ....utils.decoders import build_loader, datetime_decoder

__all__ = ['LogoutRequestModel', 'LogoutResponseModel']

class LogoutRequestModel(BaseModel):
  """
  The request model for logout endpoint
  """
  uid: str
  """The user id of the login user"""

class LogoutResponseModel(BaseModel):
  """
  The response model for logout endpoint
  """
  stat: ResponseStatus
  """The logout success or failure status"""
  request_time: Optional[datetime]
  """It will be present only on successful logout."""
  emsg: Optional[str]
  """Error message if the logout failed"""

  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder()
    })