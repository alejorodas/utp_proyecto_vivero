from utp_proyecto_vivero.model.implcrud_producer import ImplCrudProducer as crud_producer


class ControllerProducer():
  
  @staticmethod
  def create(**kwargs):
    crud_producer.create(kwargs)

  @staticmethod
  def search_by(**kwargs):
    return crud_producer.search_by(kwargs)
