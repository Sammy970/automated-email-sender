# Automated Email Sender - Cold Emails

This Python script automates the process of sending emails to multiple recipients with attached PDFs. It reads configuration data from a JSON file, allowing easy customization of recipient emails, case studies, subject lines, and the message body.

## Features

- **Email Customization**: Specify recipient emails, subject lines, and message body easily through a JSON configuration file.
- **Attachment Support**: Attach multiple PDF case studies from a specified folder.
- **Flexible Configuration**: Customize the email data, including recipient emails, subject lines, message body, and case study folder path.

## Prerequisites

- Python 3
- Required Python packages:
  - `smtplib`
  - `email`
  - `alive-progress` (for progress bar)

## Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/automated-email-sender.git
   cd automated-email-sender
   ```

2. **Install the required packages:**

   ```bash
   pip install alive-progress
   ```

3. **Edit the email_data.json file:**

   Customize the recipient emails, subject lines, and other parameters in the email_data.json file. Ensure that the case studies are stored in the specified folder.

4. **Create a message.txt file:**

    Add your message that will be sent in the email to the ``message.txt`` file.

5. **Add your resume.pdf file:**

    Place your ``resume.pdf`` in the base path (make sure to name it as resume.pdf).

6. **Run the script:**

   ```bash
   python send_emails.py
   ```

## Configuration

Edit the email_data.json file to customize the email sending parameters. Example configuration:

```
{
  "sender_email": "example@gmail.com",
  "app_password": "your_app_password",
  "case_study_folder": "case_study",
  "recipient_emails": ["email@example.com", "another_email@example.com"],
  "subject": ["Subject 1", "Subject 2"],
  "case_study_pdf_names": ["file1.pdf", "file2.pdf"]
}
```

## Configuration Details

- **`sender_email`**: Your Gmail address (e.g., `example@gmail.com`).
- **`app_password`**: App password generated for Gmail. [How to create an app password](https://support.google.com/accounts/answer/185833?hl=en).
- **`case_study_folder`**: Folder name where all case study files (PDF) are stored.
- **`recipient_emails`**: List of recipient email addresses.
- **`subject`**: List of subject lines for the emails.
- **`case_study_pdf_names`**: List of case study PDF file names.
