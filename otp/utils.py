import random
from backend.utils.mailer import send_email

def generate_otp():
    return random.randint(100000, 999999)

def send_otp(email, verification_code):
    send_email(
        f"{verification_code} is your verification code", 
        f"""
        <!DOCTYPE html>
        <html>
        <body style="font-family: Arial, sans-serif; background:#f5f6f7; padding:20px;">
            <table width="100%" cellpadding="0" cellspacing="0" border="0">
            <tr>
                <td align="center">
                <table width="500" cellpadding="0" cellspacing="0" border="0" style="background:#ffffff; padding:20px; border-radius:6px;">
                    <!-- Logo -->
                    <tr>
                    <td align="center" style="font-size:22px; font-weight:bold; color:#0052cc; padding-bottom:10px;">
                        Notelet
                    </td>
                    </tr>
                    <tr>
                    <td style="border-top:1px solid #ddd; padding-top:20px;">
                        <!-- Content -->
                        <h2 style="margin:0; font-size:18px; color:#172b4d;">You’re nearly there!</h2>
                        <p style="font-size:14px; color:#333;">Hi,</p>
                        <p style="font-size:14px; color:#333; margin-bottom:20px;">
                        Your verification code is:
                        </p>
                        <p style="font-size:20px; font-weight:bold; color:#172b4d; letter-spacing:2px; text-align:center; margin:20px 0;">
                        {verification_code}
                        </p>
                        <p style="font-size:13px; color:#555;">
                        Enter this verification code to continue setting up your Atlassian account. 
                        This code will expire in 10 minutes.
                        </p>
                        <p style="font-size:12px; color:#999;">
                        If you didn't request this code, please ignore this email.
                        </p>
                    </td>
                    </tr>
                </table>
                </td>
            </tr>
            </table>
        </body>
        </html>
        """, 
        email
    )