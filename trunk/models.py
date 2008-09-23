from google.appengine.ext import db

class parabus(db.Model):
    '''son los parabuses de las rutas de trasnsporte 
    en estas se tiene el nombre y la ubicacion geoestacionaria
    '''
    nombre = db.StringProperty()
    ubicacion = db.GeoPtProperty()

class route(db.Model):
    '''las rutas guardan el dato de la ruta de transporte 
    contienen el nombre de la rutam la empresa a la que pertenece 
    y su ubicacion en el mapa '''
    nombre = db.StringProperty()
    inicia = db.TimeProperty()
    termina = db.TimeProperty()    
    shape = db.ListProperty()

class empresa(db.Model):
    '''las empresas a las que pertenece cada una de las rutas'''
    nombre = db.StringProperty()
    logo = db.BlobProperty()
    
class wikiuser(db.Model):
    '''los datos de el usuario que ingreso la informacion de la ruta '''
    id = db.TextProperty
    lastLogin = db.DateTimeProperty
    