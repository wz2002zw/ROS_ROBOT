# Api/models.py
from pydantic import BaseModel
from typing import Tuple, Dict
# ik_Api.py 模型
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

# ik_quaternion_Api.py 模型
class PositionInput(BaseModel):
    x: float
    y: float
    z: float

class RotationInput(BaseModel):
    x_deg: float
    y_deg: float
    z_deg: float

class IKRequest(BaseModel):
    position: PositionInput
    rotation: RotationInput

class IKResponse(BaseModel):
    success: bool
    position: Tuple[float, float, float] = None
    quaternion: Tuple[float, float, float, float] = None
    joints_deg: Dict[str, float] = None
    message: str = None    