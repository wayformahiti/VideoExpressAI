#!/usr/bin/env python3
"""
Global Search Engine Submission Script
This script submits your website to major search engines worldwide to improve global ranking.
"""

import urllib.request
import urllib.parse
import urllib.error
import json
import time
import ssl
import os
from datetime import datetime

# Your API key from IndexNow
API_KEY = "edb9ab6a3b6609163fdc698e8a61bece"

# Base domain
BASE_DOMAIN = "https://videoexpressai.app"

# URLs to submit (from sitemap)
URLS = [
    f"{BASE_DOMAIN}/",
    f"{BASE_DOMAIN}/home.html",
    f"{BASE_DOMAIN}/ai-video-creation-guide.html",
    f"{BASE_DOMAIN}/contact.html",
    f"{BASE_DOMAIN}/privacy-policy.html",
    f"{BASE_DOMAIN}/terms-and-condition.html",
    f"{BASE_DOMAIN}/disclaimer.html"
]

# Search engine submission endpoints
SEARCH_ENGINES = {
    "Google": "https://www.google.com/ping?sitemap=",
    "Bing": f"https://www.bing.com/indexnow?url=PLACEHOLDER&key={API_KEY}",
    "Yandex": f"https://yandex.com/indexnow?url=PLACEHOLDER&key={API_KEY}",
    "Seznam": "https://search.seznam.cz/indexnow?url=PLACEHOLDER&key={API_KEY}",
    "Naver": "https://searchadvisor.naver.com/indexnow?url=PLACEHOLDER&key={API_KEY}"
}

def log_submission(engine, url, response_code, response_text):
    """Log submission results to a file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {engine}: {url} - Status: {response_code} - Response: {response_text}\n"
    
    with open("search_engine_submissions.log", "a") as log_file:
        log_file.write(log_entry)
    
    print(log_entry.strip())

def submit_to_search_engines():
    """Submit URLs to all search engines"""
    print(f"Starting global search engine submission for {BASE_DOMAIN}")
    print(f"Targeting #1 worldwide ranking position")
    print("-" * 60)
    
    # Create SSL context that ignores certificate validation
    context = ssl._create_unverified_context()
    
    # Submit sitemap to Google
    google_url = f"{SEARCH_ENGINES['Google']}{BASE_DOMAIN}/sitemap.xml"
    try:
        response = urllib.request.urlopen(google_url, context=context)
        log_submission("Google", "sitemap.xml", response.getcode(), "Sitemap submitted")
    except urllib.error.URLError as e:
        log_submission("Google", "sitemap.xml", "Error", str(e))
    
    # Submit each URL to other search engines
    for url in URLS:
        for engine, endpoint in SEARCH_ENGINES.items():
            if engine == "Google":
                continue  # Already submitted sitemap to Google
                
            submission_url = endpoint.replace("PLACEHOLDER", urllib.parse.quote(url))
            
            try:
                response = urllib.request.urlopen(submission_url, context=context)
                response_text = response.read().decode('utf-8')
                log_submission(engine, url, response.getcode(), response_text)
            except urllib.error.URLError as e:
                log_submission(engine, url, "Error", str(e))
            
            # Avoid rate limiting
            time.sleep(1)
    
    print("-" * 60)
    print("Global search engine submission completed")
    print("Log saved to search_engine_submissions.log")

if __name__ == "__main__":
    submit_to_search_engines()