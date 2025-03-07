from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def helloWorld():
    return {'message': 'Testando 1 2 3...'}