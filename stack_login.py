import json
import os
import re
import requests
from datetime import datetime
from colorama import Fore


class Account:
    def __init__(self):
        self.email = os.environ["EMAIL"]
        self.password = os.environ["PASS"]
        self.user_id = os.environ["USER_ID"]
        self.bot_api_token = os.environ["BOT_API_TOKEN"]


class StackOverflow:
    base_url = "https://stackoverflow.com/users/login"
    fkey = ""

    headers = {
        "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    }

    params = {
        "ssrc": "head",
        "returnurl": "https://stackoverflow.com/",
    }

    def login(self, account, current_time):
        session = requests.session()
        print(
            f"{Fore.GREEN}Start login ...{Fore.RESET}\n"
            f"{Fore.BLUE}Email : {account.email}\nPassword : {account.password}{Fore.RESET}"
        )
        payload = self.get_payload(account)
        response = session.post(
            self.base_url, data=payload, headers=self.headers, params=self.params
        )
        if response.history:
            print(
                f"{Fore.GREEN}Logged in:{current_time} with "
                f"fkey: {payload['fkey']}{Fore.RESET}"
            )
            profile_url = self.get_profile_url(session)
            session.get(profile_url)
            print(f"{Fore.BLUE}Login and access validated.{Fore.RESET}")
        else:
            print(f"{Fore.RED}Please check your email and password.{Fore.RESET}")

    def get_fkey(self):
        print("Retrieving fkey information...")
        response = requests.get(self.base_url, params=self.params, headers=self.headers)
        return re.search(r'"fkey":"([^"]+)"', response.text).group(1)

    def get_payload(self, account):
        self.fkey = self.get_fkey()
        return {
            "openid_identifier": "",
            "password": account.password,
            "fkey": self.fkey,
            "email": account.email,
            "oauth_server": "",
            "oauth_version": "",
            "openid_username": "",
            "ssrc": "head",
        }

    def get_profile_url(self, session):
        response = session.get("https://stackoverflow.com/")
        html = response.text
        return "https://stackoverflow.com" + re.search(
            r'href="(/users/[^"]*)"', html
        ).group(1)

    def send_message_to_telegram(self, account, current_time):
        url = f"https://api.telegram.org/bot{account.bot_api_token}/sendMessage"

        payload = {
            "chat_id": account.user_id,
            "text": f"Stackoverflow visited at {current_time}!",
        }

        response = requests.post(url, json=payload)

        print(f"TELEGRAM API RESPONSE: {json.dumps(response.json(), indent=2)}")


if __name__ == "__main__":
    current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    account_info = Account()
    stack_overflow = StackOverflow()
    stack_overflow.login(account_info, current_time)
    stack_overflow.send_message_to_telegram(account_info, current_time)
