class Farm:
  def __init__(self, crop, land_registry,municipality):
    self.__land_registry = land_registry
    self.__municipality = municipality
    self.__greenhouses = []
    
  @property
  def crop(self):
    return self.__crop
  
  @crop.setter
  def crop(self, crop):
    self.__crop = crop
  
  @property
  def land_registry(self):
    return self.land_registry
  
  @land_registry.setter
  def land_registry(self, land_registry):
    self.__land_registry = land_registry
    
  @property
  def municipality(self):
    return self.__municipality
  
  @municipality.setter
  def municipality(self, municipality):
    self.__municipality = municipality
  
  @property
  def greenhouses(self):
    return  self.__greenhouses
  
  @greenhouses.setter
  def greenhouses(self, greenhouse):
    self.__greenhouses.append(greenhouse)
    
  def add_greenhouse(self, greenhouse):
    self.greenhouses = greenhouse
    
  def __str__(self):

    cadena = "Cultivo: {} Registro Catastral: {} Municipio: {}".format(self.__crop,
                                                                       self.__land_registry,
                                                                       self.__municipality)
    return cadena
    
  
    
    