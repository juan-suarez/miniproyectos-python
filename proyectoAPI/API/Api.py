import pandas as pd
from sodapy import Socrata

def filterColumns(results_df) :
    try:
        results_df = results_df[["ciudad_municipio_nom", "departamento_nom", "edad", "tipo_recuperacion", "estado", "pais_viajo_1_nom"]]
    except:
        try:
            results_df = results_df[["ciudad_municipio_nom", "departamento_nom", "edad", "tipo_recuperacion", "estado"]]
            results_df.insert(5,'Procedencia', pd.Series())
        except:
            print("No hay reusltados para este departamento")
    return results_df
def consult(limit,departament):
    client = Socrata("www.datos.gov.co", None )
    results = client.get("gt2j-8ykr", limit = limit,departamento_nom =departament)
    results_df = pd.DataFrame.from_records(results)
    results_df = filterColumns(results_df)
    return results_df
