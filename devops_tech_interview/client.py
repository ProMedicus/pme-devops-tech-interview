import typer
import httpx

app = typer.Typer()


@app.command("list")
def list_all_languages():
    api_query = httpx.get("http://127.0.0.1:8081")
    result = api_query.json()
    print(result)


@app.command("check")
def list_all_languages(language: str):
    api_query = httpx.get("http://127.0.0.1:8082/" + language)
    result = api_query.json()
    print(result)


def main():
    app()


if __name__ == "__main__":
    main()
