
### 44. `weather_app/performance/load_test.py`
A script to perform load testing for the API to ensure it can handle a high number of requests.

```python
# load_test.py
import requests
import threading

API_ENDPOINT = "http://localhost:5000/api/v1/weather"

def send_request():
    try:
        response = requests.get(API_ENDPOINT)
        print(f"Response Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

def main():
    threads = []
    for i in range(100):
        thread = threading.Thread(target=send_request)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
