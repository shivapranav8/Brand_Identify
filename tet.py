import requests

def test_hello_endpoint():

    base_url = "http://localhost:8000"
    response = requests.get(f"{base_url}/hello")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "hi Shiva"

if __name__ == "__main__":
    test_hello_endpoint()
