def get_response(coin_a: str, coin_b: str) -> dict:
    import http.client
    import json

    conn = http.client.HTTPSConnection("api.coinbase.com")
    conn.request("GET", f"/v2/prices/{coin_a}-{coin_b}/buy")
    response = conn.getresponse()
    response_text = response.read().decode()
    conn.close()
    return json.loads(response_text)


def get_exchange_rate(coin_a: str, coin_b: str) -> float:
    response = get_response(coin_a, coin_b)
    try:
        return float(response["data"]["amount"])
    except (KeyError, ValueError):
        return 0.0


def get_new_value(coin_a: str, coin_b: str, value: float) -> float:
    rate = get_exchange_rate(coin_a, coin_b)
    return value * rate


def test_get_exchange_rate_and_new_value():
    # Testa usando mocks ou exemplos manuais
    sample_response = {
        "data": {
            "base": "BTC",
            "currency": "USD",
            "amount": "30000.50"
        }
    }

    # Mockando get_response para testes (normalmente com unittest.mock)
    global get_response
    original_get_response = get_response
    get_response = lambda a, b: sample_response

    assert get_exchange_rate("BTC", "USD") == 30000.50
    assert abs(get_new_value("BTC", "USD", 2) - 60001.0) < 0.01

    get_response = original_get_response

