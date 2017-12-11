"""Contains the MailSender class."""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class MailSender:
    """Connects to an SMTP server and sends emails to participants."""

    # Default port for SSL connections
    SSL_DEFAULT_PORT = 465

    # Timeout, in seconds, when connecting to SMTP server
    CONNECT_TIMEOUT = 10

    def __init__(self, host, port=SSL_DEFAULT_PORT):
        """Attempt an SMTP SSL connection with the given host/port values.

        Args:
            host: Host to connect to.
            port: Port number to connect on host.
        """
        self._host = host
        self._port = port
        self._login = False
        self._server = smtplib.SMTP_SSL(host, port,
                                        timeout=self.CONNECT_TIMEOUT)

    def login(self, username, password):
        """Login to the SMTP server using the given username and password.

        Args:
            username: Username used for logging in to server.
            password: The correspondent username's password.
        """
        self._username = username
        self._server.login(username, password)
        self._login = True

    def send(self, to, subject, msg):
        """Send an email by using the specified arguments.

        Args:
            to:      Email recipient.
            subject: Email subject.
            msg:     Email message body.
        """
        # Configure header
        email = MIMEMultipart()
        email['From'] = self._username
        email['To'] = to
        email['Subject'] = subject

        # Configure message body
        email.attach(MIMEText(msg, 'plain'))
        email_text = email.as_string()

        # Try to send email
        self._server.sendmail(self._username, to, email_text)

    def quit(self):
        """Close connection with the SMTP server."""
        self._server.quit()
