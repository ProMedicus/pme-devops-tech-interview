from fastapi import FastAPI
import uvicorn

app = FastAPI()

PROGRAMMING_LANGUAGES = [
    "python",
    "javascript",
    "c",
    "java",
    "sql",
    "php",
    "go",
    "r",
    "perl",
    "fortran"
]


@app.get("/")
def get_all_languages() -> list[str]:
    return PROGRAMMING_LANGUAGES


@app.get("/{language}")
def get_language(language: str) -> bool:
    if language in PROGRAMMING_LANGUAGES:
        return True
    else:
        return False


def main():
    uvicorn.run(
        "devops_tech_interview.server:app",
        host="0.0.0.0",
        port=8081,
    )


if __name__ == "__main__":
    main()
