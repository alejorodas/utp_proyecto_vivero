from utp_proyecto_vivero.model import producer, ICrud, crud_models
from utp_proyecto_vivero.model.crud_models import CrudModels as crud_models


class ImplCrudProducer(ICrud.ICrud):
  def create(self, **kwargs):
    producer_register = producer.Producer(self['identity_document'], self['name'], self['last_name'],
                                          self['phone'], self['email'])

    crud_models.producer_list.append(producer_register)

  
  def search_by(self, **kwargs):
    greenhouses_registers = crud_models.greenhouse_system_register_list
  
    for producer_register in greenhouses_registers:
      to_compare = producer_register.identity_document
      if to_compare == self['identity_document']:
        return producer_register
        break