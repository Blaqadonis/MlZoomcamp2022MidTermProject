import bentoml
from bentoml.io import JSON
from pydantic import BaseModel

class CreditApplication(BaseModel):
    location: str
    mintemp: int
    maxtemp: int
    rainfall: int
    evaporation: int
    sunshine: int
    windgustdir: str
    windgustspeed: int
    winddir9am: str
    winddir3pm: str
    windspeed9am: int
    windspeed3pm: int
    humidity9am: int
    humidity3pm: int
    pressure9am: int
    pressure3pm: int
    cloud9am: int
    cloud3pm: int
    temp9am: int
    temp3pm: int
    raintoday: str
    month: int
    day: int


model_ref = bentoml.xgboost.get("rain_tomorrow_model:latest")
dv = model_ref.custom_objects["dictVectorizer"]


model_runner = model_ref.to_runner()


svc = bentoml.Service("rain_tomorrow_classifier", runners=[model_runner])


@svc.api(input=JSON(pydantic_model=CreditApplication), output=JSON())
async def classify(credit_application):
    application_data = credit_application.dict()
    vector = dv.transform(application_data)
    prediction = await model_runner.predict.async_run(vector)
    print(prediction)

    result = prediction[0]

    if result > 0.65:
        return {"Rain tomorrow?": "Highly likely"}
    elif result > 0.5:
        return {"Rain tomorrow?": "Quite likely"}
    elif result > 0.43:
        return {"Rain tomorrow?": "Quite unlikely"}
    else:
        return {"Rain tomorrow?": "Highly unlikely"}



