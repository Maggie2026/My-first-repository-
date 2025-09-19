import os
import requests
from urllib.parse import urlparse
from pathlib import Path

def fetch_image():
    # Prompt the user for an image URL
    url = input("Enter the image URL: ").strip()
    
    # Create directory if it doesn't exist
    output_dir = Path("Fetched_Images")
    output_dir.mkdir(exist_ok=True)
    
    # Extract filename from URL or generate one
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    if not filename:  # If no filename in URL, generate one
        filename = "downloaded_image.jpg"
    
    save_path = output_dir / filename

    try:
        # Fetch the image from the internet
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises HTTPError for bad status codes

        # Save the image in binary mode
        with open(save_path, 'wb') as file:
            file.write(response.content)

        print(f"✅ Image successfully saved to: {save_path}")

    except requests.exceptions.MissingSchema:
        print("⚠️ Invalid URL. Please make sure you include 'http://' or 'https://'.")
    except requests.exceptions.ConnectionError:
        print("⚠️ Network error. Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("⚠️ Request timed out. Try again later.")
    except requests.exceptions.HTTPError as e:
        print(f"⚠️ HTTP Error: {e.response.status_code} - {e.response.reason}")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

if __name__ == "__main__":
    fetch_image()
📦 How to Use
Save the script as ubuntu_fetcher.py.

Install requests if you don’t have it yet:

bash
Copy code
pip install requests
Run the script:

bash
Copy code
python ubuntu_fetcher.py
Enter a valid image URL when prompted.

