login_attempts = {}
blacklisted_ips = []

def detect_bruteforce(ip):
    if ip in login_attempts:
        login_attempts[ip] += 1
    else:
        login_attempts[ip] = 1

    if login_attempts[ip] > 5:
        if ip not in blacklisted_ips:
            blacklisted_ips.append(ip)
        return "⚠️ Suspicious IP detected: " + ip
    else:
        return "Login attempt recorded from " + ip
