# Internship Automation Bot

This repository contains a Python-based bot designed to automate the process of finding and applying for internships. The bot scrapes relevant job postings from online platforms, uses an AI model to generate personalized LinkedIn outreach messages for each opportunity, and sends a consolidated summary to your email address daily.

## How It Works

The automation follows a simple yet effective workflow:

1.  **Scheduling**: The `scheduler.py` script uses `APScheduler` to trigger the main process once a day at a predefined time (10:00 AM by default) you may modify it accordingly.
2.  **Scraping**: The `job_scraper.py` module fetches internship listings from the RemoteOK API, filtering for roles related to keywords like "cyber security," "AI," and "ML"(edit or add the keywords in the roles for which you are interested in).
3.  **Message Generation**: For each relevant internship, the `openrouter_client.py` script communicates with the OpenRouter API. It uses the deep-seek-R1 model to generate a concise, professional, and personalized LinkedIn connection message.
4.  **Email Notification**: The `email_sender.py` module compiles all the scraped job details and their corresponding AI-generated messages into a single, well-formatted email.
5.  **Execution & Logging**: The `main.py` script orchestrates this entire process. It logs all operations, including found jobs and any errors, to a timestamped log file in the `logs/` directory for easy monitoring and debugging. If no jobs are found, it sends a notification email to that effect.

## Features

-   **Automated Daily Job Search**: Runs automatically every day to find the latest internship opportunities.
-   **Targeted Scraping**: Focuses on specific keywords to find relevant roles in tech.
-   **AI-Powered Message Crafting**: Generates high-impact, personalized LinkedIn messages under 300 characters to help you stand out.
-   **Email Summaries**: Delivers a daily digest directly to your inbox with job links and ready-to-use outreach messages.
-   **Scheduled Operation**: "Set it and forget it" functionality using a built-in scheduler.
-   **Robust Logging**: Keeps a record of each run for easy troubleshooting.

## Setup and Usage

Follow these steps to get the Internship Automation Bot running on your own machine.

### Prerequisites

-   Python 3.x
-   pip package manager

### 1. Clone the Repository

```bash
git clone https://github.com/RajveerSinghBisht/Internship-Automation-bot.git
cd Internship-Automation-bot
```

### 2. Install Dependencies

Install the required Python packages using pip.

```bash
pip install requests python-dotenv apscheduler
```

### 3. Configure Environment Variables

Create a file named `.env` in the root directory of the project. This file will store your API keys and credentials securely. Add the following variables to it:

```
# Your OpenRouter API Key
OPENROUTER_API_KEY="sk-or-v1-..."

# Your Gmail address for sending/receiving notifications
EMAIL_ADDRESS="your_email@gmail.com"

# Your Gmail App Password (not your regular password)
# See: https://support.google.com/accounts/answer/185833
EMAIL_PASSWORD="your_gmail_app_password"
```

### 4. Running the Bot

You have two options for running the bot:

**Option A: Run Manually (for a single execution)**

To perform a one-time scrape and receive an email immediately, run the `main.py` script.

```bash
python main.py
```

**Option B: Run on a Schedule**

To start the scheduler, which will run the bot daily at 10:00 AM, execute the `scheduler.py` script. This process will run in the foreground until you stop it (e.g., with `Ctrl+C`).

```bash
python scheduler.py
```

## File Structure

-   `main.py`: The entry point that orchestrates the scraping, message generation, and email sending process.
-   `scheduler.py`: Configures and starts the `APScheduler` to run `main.py` on a daily schedule.
-   `job_scraper.py`: Contains the logic for scraping internship data from the RemoteOK API.
-   `openrouter_client.py`: Handles the API calls to OpenRouter for generating LinkedIn messages with the Deepseek model.
-   `message_generator.py`: A simple wrapper that connects the main script to the `openrouter_client`.
-   `email_sender.py`: Manages the connection to the Gmail SMTP server and sends the final summary email.
-   `check_models.py`: A utility script to list available models from a configured AI provider (used for development).


## Automating on Local Machine (Windows Startup)

To ensure the internship bot runs automatically every day when your PC starts, follow these steps to add the scheduler to your Windows startup routine.

### Step-by-Step Setup:

#### 1. Convert Python Script to Executable (Optional but Recommended)

If you prefer an executable file over a Python script, you can convert `scheduler.py` to `.exe` using PyInstaller:

```bash
pip install pyinstaller
pyinstaller --onefile scheduler.py
```

This creates a `scheduler.exe` file inside the `dist/` folder.

#### 2. Open the Windows Startup Folder

- Press `Win + R` to open the Run dialog.
- Type:
  ```
  shell:startup
  ```
- Press Enter. This opens the Startup folder.

#### 3. Add Script or Executable to Startup

- **If using the **``**:**

  - Navigate to the `dist/` folder where `scheduler.exe` is located.
  - Right-click it → **Create shortcut**.
  - Copy the shortcut to the Startup folder.

- **If using the **``** file directly:**

  - Right-click on `scheduler.py` → **Create shortcut**.

  - Right-click the shortcut → **Properties**.

  - In the **Target** field, enter:

    ```
    "C:\Path\To\python.exe" "C:\Path\To\Your\Project\scheduler.py"
    ```

  - Replace paths with your actual Python interpreter and script file path.

  - Move the shortcut into the Startup folder.

#### 4. Ensure PC is On or Wakes Up

The script runs only if the PC is turned on and your user account is active. You can:

- Set your PC to auto-wake using Task Scheduler (optional)
- Keep your machine awake during trigger time (10 AM by default)

#### 5. Logs and Debugging

Create a 'logs' folder where you will download the complete project files.
Log files are saved in the `logs/` folder. If something breaks, check the logs for details.

#### 6. Stopping the Automation

- **To disable automation**: Just delete the shortcut from the Startup folder.
- **To stop the script manually**: If running manually, use `Ctrl + C` in the terminal.

