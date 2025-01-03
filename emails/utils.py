import logging
from django.core.mail import EmailMessage
from django.conf import settings

logger=logging.getLogger(__name__)

def send_email_notification(mail_subject, message, to_email, attachment=None):
    try:
        from_email=settings.DEFAULT_FROM_EMAIL
        mail=EmailMessage(mail_subject, message, from_email, to=to_email)
        if attachment is not None:
            mail.attach_file(attachment)
            mail.content_subtype='html'
        mail.send()
        logger.info(f'Email sent to {to_email} with subject "{mail_subject}"')
    except Exception as e:
        logger.error(f"Failed to send email to {to_email}: {e}")
        raise e