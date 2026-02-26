import os
import requests
import json
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

CONFLUENCE_URL = os.getenv("CONFLUENCE_URL").rstrip('/')
EMAIL = os.getenv("CONFLUENCE_EMAIL")
API_TOKEN = os.getenv("CONFLUENCE_API_TOKEN")

auth = HTTPBasicAuth(EMAIL, API_TOKEN)
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

def test_connection():
    """Test authentication with Confluence API."""
    url = f"{CONFLUENCE_URL}/wiki/rest/api/user/current"
    response = requests.get(url, auth=auth, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Successfully connected to Confluence as {data.get('displayName')} ({data.get('email')})!")
        return True
    else:
        print(f"❌ Connection failed. HTTP {response.status_code}")
        print(response.text)
        return False

def get_spaces():
    """Get a list of all spaces the user has access to."""
    url = f"{CONFLUENCE_URL}/wiki/api/v2/spaces"
    response = requests.get(url, auth=auth, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print("\nAvailable Spaces:")
        for space in data.get('results', []):
            print(f" - {space['name']} (Key: {space['key']})")
        return data.get('results', [])
    else:
        print(f"Failed to fetch spaces: {response.status_code}")
        return []

def create_page(space_key, title, content_html, parent_id=None):
    """Create a new page in a given space."""
    url = f"{CONFLUENCE_URL}/wiki/api/v2/pages"
    
    payload = {
        "spaceId": get_space_id(space_key),
        "status": "current",
        "title": title,
        "body": {
            "representation": "storage",
            "value": content_html
        }
    }
    
    if parent_id:
        payload["parentId"] = str(parent_id)

    response = requests.post(url, auth=auth, headers=headers, json=payload)
    if response.status_code == 200:
        print(f"✅ Successfully created page: {title}")
        return response.json()
    else:
        print(f"❌ Failed to create page. HTTP {response.status_code}")
        print(response.text)
        return None

def get_space_id(space_key):
    """Helper to get Space ID from Space Key."""
    url = f"{CONFLUENCE_URL}/wiki/api/v2/spaces?keys={space_key}"
    response = requests.get(url, auth=auth, headers=headers)
    if response.status_code == 200:
        results = response.json().get('results', [])
        if results:
            return results[0]['id']
    return None

if __name__ == "__main__":
    if test_connection():
        get_spaces()
