from utp_proyecto_vivero.model import farm, ICrud
from utp_proyecto_vivero.model.crud_models import CrudModels as crud_models


class ImplCrudFarm(ICrud.ICrud):
  
  def create(self, **kwargs):
    farm_register = farm.Farm(self['land_registry'], self['municipality'])
    crud_models.farm_list.append(farm_register)

  def search_by(self, **kwargs):
    pass
