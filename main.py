from fastapi import FastAPI

app =  FastAPI()


@app.get("/", description="Main root of Fast API")
async def root():
    return {"message": "Hello World"}