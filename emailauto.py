import smtplib
import os
import schedule
import time
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")

emails = [
    "ishaqnazil16@gmail.com",
    "gingosonda@gmail.com"
]

for email in emails:
    def send_report():
        users =  128
        errors = 2

        

        msg = EmailMessage()
        msg["From"] = SENDER_EMAIL
        msg["to"] = emails
        msg["Subject"] = "TEST"

        msg.set_content( """
                <!doctype html>
                <html lang="en">
                <head>
                <meta charset="utf-8" />
                <meta name="viewport" content="width=device-width,initial-scale=1" />
                <meta name="x-apple-disable-message-reformatting" />
                <title>Security Alert</title>
                </head>

                <body style="margin:0;padding:0;background:#f4f4f4;font-family:Arial, Helvetica, sans-serif;">
                <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
                    <tr>
                    <td align="center" style="padding:40px 16px;">

                        <!-- Main Card -->
                        <table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0"
                        style="max-width:600px;width:100%;background:#ffffff;border-radius:6px;padding:40px;">

                        <!-- Logo -->
                        <tr>
                            <td align="center" style="padding-bottom:30px;">
                            <img
                                src="https://iili.io/qdm4o8v.png"
                                alt="Robinhood"
                                width="120"
                                style="display:block;height:auto;border:0;outline:none;text-decoration:none;"
                            />
                            </td>
                        </tr>

                        <!-- Alert Text -->
                        <tr>
                            <td style="font-size:16px;line-height:26px;color:#333333;padding-bottom:25px;">
                            A recent sign-in to your account was recorded from a device or network that is not typically used.
                            The information below is provided for your reference.
                            </td>
                        </tr>

                        <!-- Section Title -->
                        <tr>
                            <td style="font-size:18px;font-weight:bold;color:#000000;padding-bottom:15px;">
                            Sign-in Details
                            </td>
                        </tr>

                        <!-- Details Table -->
                        <tr>
                            <td>
                            <table width="100%" cellpadding="12" cellspacing="0" border="1"
                                style="border-collapse:collapse;border-color:#dddddd;font-size:15px;color:#333333;">
                                <tr>
                                <td width="35%" style="background:#f9f9f9;font-weight:bold;">Location</td>
                                <td>Warsaw, Poland</td>
                                </tr>
                                <tr>
                                <td style="background:#f9f9f9;font-weight:bold;">Date & Time</td>
                                <td>Wed, February 18, 2026</td>
                                </tr>
                                <tr>
                                <td style="background:#f9f9f9;font-weight:bold;">Device</td>
                                <td>Apple iPhone 8</td>
                                </tr>
                                <tr>
                                <td style="background:#f9f9f9;font-weight:bold;">Browser</td>
                                <td>Chrome</td>
                                </tr>
                                <tr>
                                <td style="background:#f9f9f9;font-weight:bold;">IP Address</td>
                                <td>192.168.1.1</td>
                                </tr>
                            </table>
                            </td>
                        </tr>

                        <!-- Instructions -->
                        <tr>
                            <td style="font-size:15px;line-height:24px;color:#333333;padding-top:25px;">
                            If you recognize this activity, no further action is needed.
                            <br><br>
                            If you do not recognize it or would like assistance, please contact our support team.
                            </td>
                        </tr>

                        <!-- Support -->
                        <tr>
                            <td style="padding-top:20px;font-size:16px;">
                            <strong>Customer Support Line:</strong><br>
                            <a href="tel:+18662704670"
                                style="color:#1a73e8;text-decoration:none;">
                                +1 (866) 270 4670
                            </a>
                            </td>
                        </tr>

                        <!-- Signature -->
                        <tr>
                            <td style="padding-top:30px;font-size:15px;color:#333333;">
                            Thank you,<br>
                            Customer Support
                            </td>
                        </tr>

                        </table>
                        <!-- End Card -->

                    </td>
                    </tr>
                </table>
                </body>
                </html>""", subtype = "html")
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(SENDER_EMAIL,APP_PASSWORD)
            smtp.send_message(msg)

#schedule.every().day.at("13:42").do(send_report)

#print("AUtomation running...")
send_report()
#while True:
#    schedule.run_pending()
#    time.sleep(60)
    