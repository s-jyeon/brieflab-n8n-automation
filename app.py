from fastapi import FastAPI
from src.data_handlers import build_vectordb  
app = FastAPI()

@app.post("/build-vectordb")
def build_vector():
    result = build_vectordb.main()
    result["message"] = "벡터 DB update 완료"
    return result



