from MODEL import *

class Crud():
  def __init__(self):
    self.__hospitals = []
  
  def createdoctor(self,hospital_name,dni,doc_name,speciality):
    hospital = Hospital(hospital_name)
    hospital.add_doctor(dni,doc_name,speciality)
    self.__hospitals.append(hospital)

  def search_by_dni(self,dni):
    for i in self.__hospitals:
      if dni in i.doctors:
        return [i.name,i.doctors[dni].doc_info]
    return ['']