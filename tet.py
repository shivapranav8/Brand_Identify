import requests

def test_hello_endpoint():
    # Define the base URL of your FastAPI app
    base_url = "http://localhost:8000"

    # Send a GET request to the /hello endpoint
    response = requests.get(f"{base_url}/hello")

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Parse the JSON response
    data = response.json()

    # Check if the response message is "hi Shiva"
    assert data["message"] == "hi Shiva"

if __name__ == "__main__":
    test_hello_endpoint()
