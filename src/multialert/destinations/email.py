import smtplib, ssl
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from typing import Any, Optional

def send_email(
    sender: str,
    recipient: str,
    email_app_password: str,
    subject: str,
    body: str,
    email_host: Optional[str] = "smtp.gmail.com",
    image: Optional[Any] = None
):
    """
    Sends an email with the given parameters.

    Parameters
    ----------
    sender : str
        The email address of the sender.
    recipient : str
        The email address of the recipient.
    email_app_password : str
        The app password of the sender's email account.
    subject : str
        The subject of the email.
    body : str
        The body of the email.
    email_host : str, optional
        The email host, by default "smtp.gmail.com"
    image : Any, optional
        An image to attach to the email, by default None
    """

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    if image is not None:
        filename = "image.jpg"  # In same directory as script

        try:
            import cv2
        except ImportError:
            raise ImportError("OpenCV is required to send images")

        _, im_buf_arr = cv2.imencode(".jpg", image)
        byte_im = im_buf_arr.tobytes()
        message_image_attachment = MIMEImage(byte_im)

        # Encode file in ASCII characters to send by email    
        encoders.encode_base64(message_image_attachment)

        # Add header as key/value pair to attachment part
        message_image_attachment.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        # Add attachment to message and convert message to string
        message.attach(message_image_attachment)

    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(email_host, 465, context=context) as server:
        server.login(sender, email_app_password)
        server.sendmail(sender, recipient, text)