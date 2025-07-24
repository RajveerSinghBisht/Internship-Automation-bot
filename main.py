import os
import sys
import io
import logging
from datetime import datetime

from job_scraper import scrape_internships
from message_generator import generate_linkedin_message
from email_sender import send_email

# Ensure console handles Unicode (for emojis)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Setup logging
os.makedirs("logs", exist_ok=True)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

log_filename = f"logs/run_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# File handler
file_handler = logging.FileHandler(log_filename, encoding='utf-8')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Console handler
console_handler = logging.StreamHandler(sys.stdout)
console_console_formatter = logging.Formatter('%(message)s')
console_handler.setFormatter(console_console_formatter)
logger.addHandler(console_handler)


def main():
    logging.info("🔍 Starting internship scraper...")
    logging.info("🔍 Scraping internships from source...")
    jobs = scrape_internships()

    if not jobs:
        logging.warning("⚠️ No jobs found. Sending fallback email.")
        send_email("No Internships Found", "None of the job sources returned any internships today. Try again tomorrow!")
        return

    logging.info(f"✅ {len(jobs)} total internships found.\n")
    logging.info("📋 Previewing scraped jobs:")

    for job in jobs:
        logging.info(f"{job['title']} at {job['company']} — {job['link']}")

    email_body = "🌐 Today's Internship Opportunities\n\n"

    for idx, job in enumerate(jobs, start=1):
        title = job.get("title", "").strip()
        company = job.get("company", "").strip()

        if not title or not company:
            logging.warning(f"⚠️ Skipping job {idx} due to missing title or company")
            continue

        logging.info(f"🧠 Generating message for job {idx}: {title} at {company}")
        try:
            message = generate_linkedin_message(job)
        except Exception as e:
            logging.error(f"❌ Failed to generate message for job {idx}: {e}")
            continue

        email_body += f"🔹 {title} at {company}\n"
        email_body += f"🔗 {job['link']}\n"
        email_body += f"💬 LinkedIn Message:\n{message}\n"
        email_body += "\n---\n\n"

    if not email_body.strip():
        email_body = "No valid internships were found today, but the scraper ran successfully."

    logging.info("📧 Sending compiled email...")
    send_email("🚀 Internship Picks + LinkedIn Messages", email_body)
    logging.info("✅ Done. Email sent successfully.")


if __name__ == "__main__":
    main()
