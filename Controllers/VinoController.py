from werkzeug.wrappers import response
from ..Models.vinoModel import vino
from ..Services import dbVinoService
def insertVino(Nombre,VolatileAcidity,FixedAcidity,CitricAcid,
               FreeSulfurDioxide,Chlorides,Density,
    TotalSulfurDioxide, PH,Sulphates,Alcohol,Quality,IdProductor):
    vinoObj=vino(Nombre,VolatileAcidity,FixedAcidity,CitricAcid
                 ,FreeSulfurDioxide,Chlorides,Density,TotalSulfurDioxide,PH,Sulphates,
                 Alcohol,Quality,IdProductor)
    response=dbVinoService.insertVino(vinoObj.__json__())
    return response

def getVinosByIdProductor(id):
    response=dbVinoService.getVinosByIdProductor(id)
    return response

def deleteVino(id):
    response=dbVinoService.deleteVino(id)
    return response