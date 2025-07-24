from job_scraper import scrape_internships
from message_generator import generate_linkedin_message
from email_sender import send_email

def main():
    print("🔍 Scraping internships from all sources...")
    jobs = scrape_internships()

    if not jobs:
        print("⚠️ No jobs found. Sending fallback email...")
        send_email("No Jobs Found", "No internships matched the criteria today.")
        return

    email_body = "🌟 **Today's Curated Internships (AI, Cybersecurity, Comms)** 🌟\n\n"

    for idx, job in enumerate(jobs):
        title = job.get("title", "").strip()
        company = job.get("company", "").strip()
        link = job.get("link", "").strip()

        if not title or not company or not link:
            print(f"⚠️ Skipping job {idx+1} due to missing info")
            continue

        print(f"🧠 Generating message for job {idx+1}: {title} at {company}")
        try:
            message = generate_linkedin_message(job)
        except Exception as e:
            print(f"❌ Message generation failed for job {idx+1}: {e}")
            continue

        email_body += f"🔹 **{title}** at *{company}*\n"
        email_body += f"🔗 {link}\n"
        email_body += f"💬 LinkedIn Message:\n{message.strip()}\n"
        email_body += "\n---\n\n"

    if not email_body.strip():
        email_body = "The scraper ran, but no valid internships were collected today."

    print("📧 Sending compiled email...")
    send_email("🚀 Internship Picks + LinkedIn Messages", email_body)
    print("✅ Done! Email sent.")

if __name__ == "__main__":
    main()
