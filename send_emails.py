import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart, MIMEBase
from email import encoders
import time
from alive_progress import alive_bar
import json
import os

resume_attachment_path = "resume.pdf"  # Assuming the same resume for all recipients


def read_email_data(file_path, message_body_file):
    with open(file_path, "r") as file:
        data = json.load(file)

    # Read message body from the text file
    with open(message_body_file, "r") as body_file:
        data["message_body"] = body_file.read()

    return (
        data["recipient_emails"],
        # data["case_study_pdf_names"],
        data.get("case_study_folder", ""),
        data["subject"],
        data["message_body"],
        data["sender_email"],
        data["app_password"],
    )


# Usage
file_path = "email_data.json"
message_body_file = "message.txt"
(
    recipient_emails,
    case_study_folder,
    subject,
    message_body,
    sender_email,
    app_password,
) = read_email_data(file_path, message_body_file)

# Assuming you have the case studies in PDF format in the specified folder
case_study_pdf_names = [file for file in os.listdir(case_study_folder) if file.endswith(".pdf")]

# Connect to the SMTP server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, app_password)

# Attach Resume file (outside the loop)
with open(resume_attachment_path, "rb") as attachment:
    resume_pdf_part = MIMEBase("application", "octet-stream")
    resume_pdf_part.set_payload(attachment.read())
    encoders.encode_base64(resume_pdf_part)
    resume_pdf_part.add_header(
        "Content-Disposition", f"attachment; filename={resume_attachment_path}"
    )

try:
    with alive_bar(len(recipient_emails), title="Sending Emails") as bar:
        # Send emails to each recipient at 30-second intervals
        for i, recipient_email in enumerate(recipient_emails):
            # Create a new MIMEMultipart object for each iteration
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = recipient_email
            message["Subject"] = subject[i]
            message.attach(MIMEText(message_body, "plain"))

            # Attach PDF file
            pdf_attachment_path = f"{case_study_folder}/{case_study_pdf_names[i]}"
            with open(pdf_attachment_path, "rb") as attachment:
                pdf_part = MIMEBase("application", "octet-stream")
                pdf_part.set_payload(attachment.read())
                encoders.encode_base64(pdf_part)
                pdf_part.add_header(
                    "Content-Disposition", f"attachment; filename={case_study_pdf_names[i]}"
                )
                message.attach(pdf_part)

            # Attach Resume file (outside the loop)
            message.attach(resume_pdf_part)

            server.sendmail(sender_email, recipient_email, message.as_string())
            print(
                f"Email {i+1} sent to {recipient_email} with PDF and Resume attachments"
            )
            time.sleep(15)
            bar()

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the SMTP connection
    server.quit()
