# Email Sandbox Monitor (local)

This is a small, local sandbox for monitoring email behavior. It is designed to be safe to run locally and does not connect to any external email accounts.

Files added:
- `server.py`: small SMTP server (using `aiosmtpd`) that listens on `127.0.0.1:1025` and saves incoming messages to `mailbox/`.
- `analyzer.py`: polls `mailbox/` for `.eml` files, parses messages, extracts links/attachments, and flags suspicious patterns. Summaries are written to `processed/` as JSON.
- `sender_test.py`: sends two test messages (benign and phishing-like) to the local sandbox.
- `requirements.txt`: Python dependencies (`aiosmtpd`, `beautifulsoup4`).

Quick start (Windows PowerShell):

1. Create and activate a venv (optional but recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Start the SMTP sandbox in one terminal:

```powershell
python server.py
```

4. In another terminal, start the analyzer:

```powershell
python analyzer.py
```

5. In a third terminal, send test messages:

```powershell
python sender_test.py
```

You should see `.eml` files appear in `mailbox/` and corresponding JSON summaries in `processed/` with detected alerts.

Notes & safety:
- This sandbox runs locally on an unprivileged port (1025) and does not forward messages outside your machine.
- Do not expose this to the public internet; it is intended for experimentation on a local machine or isolated network.

Next steps you might want:
- Add more heuristics (e.g., DKIM/SPF checks, domain reputation lookups).
- Add a small web UI to review `processed/` summaries.
- Hook analyzer to an actual IMAP server (requires credentials and extra care).
