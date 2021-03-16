from abc import ABC, abstractmethod


class ICrud(ABC):
  
  @abstractmethod
  def create(self, **kwargs):
    raise NotImplementedError
  
  @abstractmethod
  def search_by(self, **kwargs):
    raise NotImplementedError

  
  def has_many(self, one, many):
    for m in many:
      one.associated_to(m)