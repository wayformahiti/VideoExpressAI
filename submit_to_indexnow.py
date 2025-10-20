#!/usr/bin/env python3
"""
IndexNow URL submission script for VideoExpress.AI Studio
This script submits URLs to the IndexNow API to improve search engine indexing.
"""

import urllib.request
import urllib.parse
import json
import sys

def submit_to_indexnow(key, urls, host="videoexpressai.app"):
    """Submit URLs to IndexNow API"""
    
    # IndexNow API endpoint (Bing)
    api_url = f"https://www.bing.com/indexnow?url=https://{host}/&key={key}"
    
    # Prepare the payload
    payload = {
        "host": host,
        "key": key,
        "urlList": urls
    }
    
    # Make the API request
    try:
        data = json.dumps(payload).encode('utf-8')
        req = urllib.request.Request(
            api_url,
            data=data,
            headers={"Content-Type": "application/json; charset=utf-8"}
        )
        
        # Send the request
        with urllib.request.urlopen(req) as response:
            response_text = response.read().decode('utf-8')
            print(f"Success! URLs submitted to IndexNow API: {response_text}")
            return True
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
        return False
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
        return False
    except Exception as e:
        print(f"Exception occurred: {str(e)}")
        return False

if __name__ == "__main__":
    # IndexNow API key
    api_key = "edb9ab6a3b6609163fdc698e8a61bece"
    
    # Read URLs from sitemap-indexnow.txt
    try:
        with open("sitemap-indexnow.txt", "r") as f:
            urls = [line.strip() for line in f.readlines() if line.strip()]
    except Exception as e:
        print(f"Error reading sitemap-indexnow.txt: {str(e)}")
        sys.exit(1)
    
    # Submit URLs to IndexNow API
    if urls:
        print(f"Submitting {len(urls)} URLs to IndexNow API...")
        submit_to_indexnow(api_key, urls)
    else:
        print("No URLs found in sitemap-indexnow.txt")