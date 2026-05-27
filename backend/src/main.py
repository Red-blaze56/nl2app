from fastapi import FastAPI, APIRouter

app = FastAPI(
    title="NL2app : natural language to application",
    description="NL2app is a tool that converts natural language into application code. It supports multiple programming languages and frameworks, allowing developers to quickly generate code snippets based on their requirements.",
    version="0.1.0",
)

@app.get("/")
async def root():
    return {"message": "Welcome to NL2app!"}