def get_movies(texto_busca: str) -> dict:
    import http.client
    import json

    conn = http.client.HTTPSConnection("search.imdbot.workers.dev")
    conn.request("GET", f"/?q={texto_busca}")
    response = conn.getresponse()
    response_text = response.read().decode()
    conn.close()
    return json.loads(response_text)


def search_movie(movie_name: dict) -> dict:
    resultados = movie_name.get("results", [])
    if resultados:
        return resultados[0]
    return None


def test_search_movie():
    sample_response = {
        "results": [
            {"title": "Inception", "year": 2010, "id": "tt1375666"},
            {"title": "Interstellar", "year": 2014, "id": "tt0816692"}
        ]
    }

    assert search_movie(sample_response) == {"title": "Inception", "year": 2010, "id": "tt1375666"}
    assert search_movie({"results": []}) is None
    assert search_movie({}) is None
