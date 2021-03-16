from utp_proyecto_vivero.model.implcrud_farm import ImplCrudFarm as crud_farm
from utp_proyecto_vivero.model.crud_models import CrudModels as crud_models

class ControllerFarm():
  @staticmethod
  def create(**kwargs):
    crud_farm.create(kwargs)

    #Asociar Uno a Muchos
    producer = crud_models.producer_list[0]
    farms = crud_models.farm_list
    crud_farm().has_many(producer,farms)
    crud_models.greenhouse_system_register_list.append(producer)
