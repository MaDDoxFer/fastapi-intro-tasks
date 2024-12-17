from fastapi import FastAPI, Cookie

app = FastAPI()

# BEGIN (write your solution here)
@app.get("/language")
def get_language(language: str = Cookie(None, description="Языковая настройка")):
    if language is None:
        return {"message": "Language not set"}
    return {"language": language}
# END
