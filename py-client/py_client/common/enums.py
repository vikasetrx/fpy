"""
Commonly used enumerators
"""
from enum import Enum

__all__ = [
  'RequestSourceType',
  'ResponseStatus',
  'RestMethod'
]

class RequestSourceType(str, Enum):
  """
  The source of the request, mobile or web
  """
  MOB = 'MOB'
  WEB = 'WEB'
  API = 'API'

class ResponseStatus(str, Enum):
  """
  The response success or failure status
  """
  OK = 'Ok'
  NOT_OK = 'Not_Ok'

class RestMethod(str, Enum):
  """
  Enumeration for REST methods
  """
  GET = 'get'
  POST = 'post'
  PATCH = 'patch'
  PUT = 'put'
  DELETE = 'delete'
  OPTION = 'option'
  HEAD = 'head'
