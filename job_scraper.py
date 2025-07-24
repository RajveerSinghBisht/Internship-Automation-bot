import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

import requests
from bs4 import BeautifulSoup


def scrape_remoteok():
    print("\U0001F4E6 Scraping RemoteOK...")
    jobs = []
    try:
        url = "https://remoteok.com/api"
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers)
        if res.status_code != 200:
            print("❌ RemoteOK API failed")
            return []

        data = res.json()[1:]  # First item is metadata
        keywords = ["cyber", "security", "ai", "ml", "communication"]

        for job in data:
            title = job.get("position") or job.get("title", "")
            company = job.get("company", "")
            link = job.get("url", "")

            if any(kw.lower() in title.lower() for kw in keywords):
                jobs.append({
                    "title": title.strip(),
                    "company": company.strip(),
                    "link": f"https://remoteok.com{link}" if link.startswith("/") else link,
                    "description": job.get("description", "")[:200]
                })

            if len(jobs) >= 5:
                break
        return jobs
    except Exception as e:
        print(f"❌ RemoteOK scraping failed: {e}")
        return []


def scrape_internships():
    print("\U0001F50D Scraping internships from source...")
    all_jobs = []
    all_jobs.extend(scrape_remoteok())
    

    # Remove duplicates (same link)
    seen = set()
    unique_jobs = []
    for job in all_jobs:
        if job["link"] not in seen:
            seen.add(job["link"])
            unique_jobs.append(job)

    print(f"✅ Found {len(unique_jobs)} total jobs across APIs")
    return unique_jobs[:12]
