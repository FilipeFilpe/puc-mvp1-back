from typing import List

from model.property import Property
from pydantic import BaseModel
from schemas import VisitSchema

title_base: str = "Um lindo apartamento à beira mar"
address_base: str = "Rua XPTO, 61, Rio de Janeiro/RJ"
value_base: float = 285000.00
size_base: float = 55.45
rooms_base: int = 2
bathrooms_base: int = 1
garages_base: int = 1
type_base: str = "Apartamento"
# thumbnail_base: str = "https://pointer.com.br/blog/wp-content/uploads/2021/02/5a8c590ea936140d7f6def44.jpg"
thumbnail_base: str = "01.jpg"

class PropertySchema(BaseModel):
    """ Define como uma nova propriedade é apresentada
    """
    title: str = title_base
    address: str = address_base
    value: float = value_base
    size: float = size_base
    rooms: int = rooms_base
    bathrooms: int = bathrooms_base
    garages: int = garages_base
    type: str = type_base
    thumbnail: str = thumbnail_base

class PropertyWithIdSchema(PropertySchema):
    """ Define uma nova propriedade com id
    """
    id: int = 1
    
class PropertySearchSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no id da propriedade.
    """
    id: int = 1

class ListPropertiesSchema(BaseModel):
    """ Define como uma listagem de propriedades será retornada.
    """
    properties:List[PropertyWithIdSchema]
    

def show_properties(properties: List[Property]):
    """ Retorna uma representação da propriedade seguindo o schema definido em
        PropertyViewSchema.
    """
    result = []
    for property in properties:
        result.append({
            "id": property.id,
            "title": property.title,
            "address": property.address,
            "value": property.value,
            "size": property.size,
            "rooms": property.rooms,
            "bathrooms": property.bathrooms,
            "garages": property.garages,
            "type": property.type,
            "thumbnail": property.thumbnail,
        })

    return {"properties": result}


class PropertyViewSchema(BaseModel):
    """ Define como uma propriedade será retornada: property.
    """
    title: str = title_base
    address: str = address_base
    value: float = value_base
    size: float = size_base
    rooms: int = rooms_base
    bathrooms: int = bathrooms_base
    garages: int = garages_base
    type: str = type_base
    thumbnail: str = thumbnail_base    
    visits:List[VisitSchema]

class PropertyDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    message: str
    title: str

def show_property(property: Property):
    """ Retorna uma representação da propriedade seguindo o schema definido em
        PropertyWithIdSchema.
    """
    return {
        "id": property.id,
        "title": property.title,
        "address": property.address,
        "value": property.value,
        "size": property.size,
        "rooms": property.rooms,
        "bathrooms": property.bathrooms,
        "garages": property.garages,
        "type": property.type,
        "thumbnail": property.thumbnail,
        "visits": [
            {
                "name": v.name,
                "email": v.email,
                "phone": v.phone,
                "date": v.date,
            }
            for v in property.visits
        ]
    }