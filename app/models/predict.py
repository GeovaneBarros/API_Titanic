from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class Embarked(str, Enum):
    cherbourg = "C"
    queenstown = "Q"
    southampton = "S"


class PClass(str, Enum):
    class_1 = "1"
    class_2 = "2"
    class_3 = "3"


class InputPredict(BaseModel):
    passengerId: int
    pClass: PClass
    name: str
    sex: str
    age: int
    sibSp: int
    parch: int
    ticket: str
    fare: float
    cabin: str
    embarked: Embarked


class ResponsePredict(BaseModel):
    predicted_class: str
    DateTime: datetime
