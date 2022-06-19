import requests
def send_message_to_line(message):
    print("go")
    access_token = "IGq5z7sGQQTJrLSmxIB6jVbnyFvxCu1iWvLTRpezN8J"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    data = {"message":message}
    requests.post("https://notify-api.line.me/api/notify",
                    headers = headers,
                    data=data
    )

if __name__ == "__main__":
    send_message_to_line("これで、自動でスクリプト回しているときに、買いの判断とか、自動取引の内容とか通知できるぜ！")
    print("send")
else:
    print("false")