import orjson
from pydantic import BaseModel
from typing import TypeVar

def orjson_dumps(v, *, default):
    # orjson.dumps returns bytes, to match standard json.dumps we need to decode
    return orjson.dumps(v, default=default).decode()


class GeoPoint(BaseModel):
    latitude: float = 55.824322
    longitude: float = 37.611089


class Photo(BaseModel):
    geo: GeoPoint
    title: str
    source: str
    period: str
    file_name: str
    cid: int


class Params(BaseModel):
    geo: GeoPoint = GeoPoint()
    distance: int = 125
    limit: int = 5
    skip: int = 0

    def set_pagination(self, page: int = 0):
        self.skip = page * self.limit
        return self

    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps
        json_encoders = {
            GeoPoint: lambda g: [g.latitude, g.longitude],
        }
