from google.appengine.ext import db
''' 
These classes are based 
on the Google Transit Feed Specification
http://code.google.com/transit/spec/transit_feed_specification.html
'''
class stop(db.Model):
    '''son los parabuses de las rutas de trasnsporte 
    en estas se tiene el nombre y la ubicacion geoestacionaria
    '''    
    stop_name = db.StringProperty
    stop_geo = db.GeoPtProperty

class route(db.Model):
    '''las rutas guardan el dato de la ruta de transporte 
    contienen el nombre de la rutam la empresa a la que pertenece 
    y su ubicacion en el mapa '''
    #route_id = db.ReferenceProperty
    #agency_id = db.
    route_short_name = db.StringProperty
    route_long_name = db.StringProperty
    #route_desc = db.StringProperty
    route_type = db.IntegerProperty
    #route_url = db.URLProperty
    #route_color 
    #route_text_color

class trips(db.Model):
    ''' representan los viajes que una ruta puede realizar '''
    route_id = db.ReferenceProperty
    service_id = db.ReferenceProperty
    trip_id = db.ReferenceProperty
    #trip_headsign
    #direction_id
    #block_id
    #shape_id

class shape(db.Model):
    '''son las lineas que sigue un viaje'''
    shape_id = db.ReferenceProperty
    shape_pt_geo = db.GeoPtProperty
    shape_pt_sequence = db.IntegerProperty
    shape_dist_traveled = db.FloatProperty


class agency(db.Model):
    '''las empresas a las que pertenece cada una de las rutas'''
    agency_id = db.ReferenceProperty
    agency_name = db.StringProperty
    logo = db.BlobProperty
    
class user(db.Model):
    '''los datos de el usuario que ingreso la informacion de la ruta '''
    id = db.TextProperty
    lastLogin = db.DateTimeProperty
    