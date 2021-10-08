"""
Common models used across the project
"""

from typing import List, Optional
from pydantic import BaseModel

__all__ = ['Product', 'BankDetails', 'DpAccountNumber', 'Scrip']

class Product(BaseModel):
  """
  The product model
  """
  prd: str
  """The product name"""
  s_prdt_ali: str
  """The product display name"""
  exch: List[str]
  """List of strings with enabled, allowed exchange names"""

class BankDetails(BaseModel):
  """
  The bank details model
  """
  bankn: Optional[str]
  """Bank Name"""
  acctnum: Optional[str]
  """Account Number"""

class DpAccountNumber(BaseModel):
  """
  The dp account number model
  """
  dpnum: Optional[str]

class Scrip(BaseModel):
  """
  The scrip model
  """
  exch: Optional[str]
  """Exchange"""
  tsym: Optional[str]
  """Trading symbol of the scrip (contract)"""
  token: Optional[str]
  """Token of the scrip (contract)"""
  pp: Optional[float]
  """Price precision"""
  ti: Optional[float]
  """Tick size"""
  ls: Optional[float]
  """Lot size"""