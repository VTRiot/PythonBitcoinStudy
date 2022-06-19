from email.errors import HeaderDefect
import requests
def send_message_to_line(message):
    print("go")
    Dist = "HRD"
    if Dist == "HRD":
        access_token = "uQSk2NNet76BrZaIudpg56I7HM1026g1jVVY53z3KX6"
    else:
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
    send_message_to_line("通知のテスト")
    print("send")
else:
    print("false")