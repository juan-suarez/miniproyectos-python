class Hospital():
  def __init__(self,hospital_name):
    self.__name = hospital_name
    self.__doctor_list = {}
  
  @property
  def doctors(self):
    return self.__doctor_list
  def add_doctor(self,doc_dni,doc_name,speciality):
    doc = Doctor(doc_dni,doc_name,speciality)
    self.__doctor_list[doc_dni] = doc
  @property
  def name(self):
    return self.__name

class Doctor():
    def __init__(self,dni,doc_name,speciality):
      self.__doc_name = doc_name
      self.__dni = dni
      self.__speciality = speciality
    @property
    def doc_info(self):
      return [self.__dni,self.__doc_name,self.__speciality]