from fastapi import APIRouter
from datetime import datetime
from models import ResponsePredict, InputPredict
from logic.predict import perform_prediction

router = APIRouter(
    prefix='/predict',
    tags=['predict'],
    responses={400: {'description': 'Bad Request'}}
)


@router.post('/', response_model=ResponsePredict)
def predict(item: InputPredict):
    predicted_class = perform_prediction(item)
    return {
        'predicted_class': predicted_class,
        'DateTime': datetime.now()
    }
