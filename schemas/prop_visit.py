from pydantic import BaseModel


class VisitSchema(BaseModel):
    """ Define como uma nova visita é apresentada
    """
    property_id: int = 1
    name: str = 'Filipe Sousa'
    email: str = 'filipe@gmail.com'
    phone: str = '61981392996'
    date: str = '2023-09-20T20:40'
