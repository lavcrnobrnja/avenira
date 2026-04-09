#!/usr/bin/env python3
"""Clear Ghost default social links"""
import jwt, time, requests, json

def make_token(admin_key):
    kid, secret = admin_key.split(':')
    iat = int(time.time())
    header = {'alg': 'HS256', 'typ': 'JWT', 'kid': kid}
    payload = {'iat': iat, 'exp': iat + 300, 'aud': '/admin/'}
    return jwt.encode(payload, bytes.fromhex(secret), algorithm='HS256', headers=header)

def clear_socials(base_url, admin_key, label):
    token = make_token(admin_key)
    headers = {
        'Authorization': f'Ghost {token}',
        'Content-Type': 'application/json'
    }
    
    # Try to update settings
    url = f"{base_url}/ghost/api/admin/settings/"
    data = {
        'settings': [
            {'key': 'twitter', 'value': ''},
            {'key': 'facebook', 'value': ''}
        ]
    }
    resp = requests.put(url, headers=headers, json=data)
    if resp.status_code == 200:
        print(f"[{label}] Social links cleared")
    else:
        print(f"[{label}] Settings update: {resp.status_code} - {resp.text[:200]}")

en_key = "69d8185cb437b1e938a801c7:6dc467a96bb5c9dcf0795151f5e9dd9185528751d77468a47f0d797ba80bf02e"
fr_key = "69d818d214e97ce940a3ac7c:84e3838aeca8f3e90827685c3c6ee2ea6e1cff9ee8d50153c33c154769e36fe9"

clear_socials("https://avenira.ai", en_key, "EN")
clear_socials("https://avenira.ai/fr", fr_key, "FR")
