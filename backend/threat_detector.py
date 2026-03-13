login_attempts = {}

def detect_bruteforce(ip):
    if ip in login_attempts:
        login_attempts[ip] += 1
    else:
        login_attempts[ip] = 1

    if login_attempts[ip] > 5:
        return "⚠️ Possible Brute Force Attack Detected from " + ip
    else:
        return "Login attempt recorded"
