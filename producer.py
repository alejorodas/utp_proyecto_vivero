class Producer:
  def __init__(self, identity_document, name, last_name, phone, email):
    self.__identity_document = identity_document
    self.__name = name
    self.__last_name = last_name
    self.__phone = phone
    self.__email = email
    self.__farms = []
  
  @property
  def identity_document(self):
    return self.__identity_document
  
  @identity_document.setter
  def identity_document(self, identity_document):
    self.__identity_document = identity_document
  
  @property
  def name(self):
    return self.__name
  
  @name.setter
  def name(self, name):
    self.__name = name
  
  @property
  def last_name(self):
    return self.__last_name
  
  @last_name.setter
  def last_name(self, last_name):
    self.__last_name = last_name
  
  @property
  def phone(self):
    return self.__phone
  
  @phone.setter
  def phone(self, phone):
    self.__phone = phone
    
  @property
  def email(self):
    return self.__email
  
  @email.setter
  def email(self, email):
    self.__email = email
    
  @property
  def farms(self):
    return self.__farms
  
  @farms.setter
  def farms(self, farm):
    self.__farms.append(farm)
  
  def asociar(self,farm):
    self.farms = farm
  

  
  def __str__(self):
    cadena = "documento identidad: {} nombre: {} apellido: {} telefono: {} correo: {}".format(self.__identity_document,
                                                                  self.__name,
                                                                  self.__last_name,
                                                                  self.__phone,
                                                                  self.__email)
    return cadena

