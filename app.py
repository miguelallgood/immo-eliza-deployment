from fastapi import FastAPI
from predict import Item, predict
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "alive"}

@app.post("/predict/")
async def predict_price(item: Item):
    prediction = predict(item)
    status_code = 200 if prediction else 404  # Set status code based on prediction availability
    return {"prediction": prediction, "status_code": status_code}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)