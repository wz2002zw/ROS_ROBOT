# Api/models.py
from pydantic import BaseModel

class Position(BaseModel):
    x: float
    y: float
    z: float

class Orientation(BaseModel):
    x: float
    y: float
    z: float
    w: float

class PoseInput(BaseModel):
    position: Position
    orientation: Orientation