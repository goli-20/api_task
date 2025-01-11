import requests
import json


class ApiTests:
    # Define the base URL as a class variable
    BASE_URL = "https://jsonplaceholder.typicode.com"

    @staticmethod
    def http_get_posts():
        print("\n--- Output for GET Request on /posts ---")
        res = requests.get(f"{ApiTests.BASE_URL}/posts")
        if res.status_code == 200:
            print("Success")
        result = res.json()
        print("Response Data:")
        print(json.dumps(result, indent=4))  # Pretty print JSON response
        if isinstance(result, list):
            print("Successfully validated")

    @staticmethod
    def http_get_posts_1():
        print("\n--- Output for GET Request on /posts/1 ---")
        res = requests.get(f"{ApiTests.BASE_URL}/posts/1")
        if res.status_code == 200:
            print("Success")
        result = res.json()
        print("Response Data:")
        print(json.dumps(result, indent=4))  # Pretty print JSON response
        if isinstance(result, dict):
            print("Successfully validated")

    @staticmethod
    def http_get_comments():
        print("\n--- Output for GET Request on /posts/1/comments ---")
        res = requests.get(f"{ApiTests.BASE_URL}/posts/1/comments")
        if res.status_code == 200:
            print("Success")
        result = res.json()
        print("Response Data:")
        print(json.dumps(result, indent=4))  # Pretty print JSON response
        if isinstance(result, list):
            print("Successfully validated")

    @staticmethod
    def http_get():
        print("\n--- Output for GET Request on /comments?PostId=1 ---")
        res = requests.get(f"{ApiTests.BASE_URL}/comments?postId=1")
        if res.status_code == 200:
            print("Success")
        result = res.json()
        print("Response Data:")
        print(json.dumps(result, indent=4))  # Pretty print JSON response
        if isinstance(result, list):
            print("Successfully validated")

    @staticmethod
    def http_post():
        print("\n--- Output for Post Request on /posts ---")
        payload = {
            "userId": 20,
            "id": 122,
            "title": "New record created",
            "body": "New record"
        }
        res = requests.post(f"{ApiTests.BASE_URL}/posts", json=payload)
        if res.status_code == 201:
            print("Success")
        result = res.json()
        print("Response Data:")
        print(json.dumps(result, indent=4))  # Pretty print JSON response
        if isinstance(result, dict):
            print("Successfully validated")

    @staticmethod
    def http_put():
        print("\n--- Output for put Request on /posts/1 ---")
        res = requests.put(f"{ApiTests.BASE_URL}/posts/1")
        if res.status_code == 200:
            print("Success")
        result = res.json()
        print("Response Data:")
        print(json.dumps(result, indent=4))  # Pretty print JSON response
        if isinstance(result, dict):
            print("Put successfully validated")

    @staticmethod
    def http_patch():
        print("\n--- Output for Patch Request on /posts/1 ---")
        res = requests.patch(f"{ApiTests.BASE_URL}/posts/1")
        if res.status_code == 200:
            print("Success")
        result = res.json()
        print("Response Data:")
        print(json.dumps(result, indent=4))  # Pretty print JSON response
        if isinstance(result, dict):
            print("Patch successfully validated")

    @staticmethod
    def http_delete():
        print("\n--- Output for Delete Request on /posts/1 ---")
        res = requests.delete(f"{ApiTests.BASE_URL}/posts/1")
        if res.status_code == 200:
            print("Success")
        result = res.json()
        print("Response Data:")
        print(json.dumps(result, indent=4))  # Pretty print JSON response
        if isinstance(result, dict):
            print("Delete successfully validated")


# Run all test cases
if __name__ == "__main__":
    api_tests = ApiTests()
    api_tests.http_get_posts()
    api_tests.http_get_posts_1()
    api_tests.http_get_comments()
    api_tests.http_get()
    api_tests.http_post()
    api_tests.http_put()
    api_tests.http_patch()
    api_tests.http_delete()
