import os
import time
import pathlib
from aiosmtpd.controller import Controller


class MailHandler:
    def __init__(self, mailbox_dir='mailbox'):
        self.mailbox_dir = pathlib.Path(mailbox_dir)
        self.mailbox_dir.mkdir(exist_ok=True)

    async def handle_DATA(self, server, session, envelope):
        """Called by aiosmtpd when a message is received. Saves the raw message to disk."""
        ts = int(time.time() * 1000)
        filename = self.mailbox_dir / f'msg_{ts}.eml'
        # envelope.content is bytes
        content = envelope.content if hasattr(envelope, 'content') else getattr(envelope, 'original_content', None)
        if content is None:
            content = b''
        with open(filename, 'wb') as f:
            f.write(content)
        print(f"Saved incoming message to {filename}")
        return '250 Message accepted for delivery'


def run_smtp_server(hostname='127.0.0.1', port=1025, mailbox_dir='mailbox'):
    """Start a local SMTP server (honeypot) that stores messages in `mailbox_dir`.

    Run this in a dedicated terminal. It listens on the given port and writes .eml files
    for each received message.
    """
    handler = MailHandler(mailbox_dir=mailbox_dir)
    controller = Controller(handler, hostname=hostname, port=port)
    controller.start()
    try:
        print(f"SMTP sandbox running on {hostname}:{port} — messages stored in {mailbox_dir}/")
        print("Press Ctrl+C to stop.")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping SMTP sandbox...")
    finally:
        controller.stop()


if __name__ == '__main__':
    run_smtp_server()
