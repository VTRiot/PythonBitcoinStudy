from email.errors import HeaderDefect
import requests

def pprint(message):
    s = ""
    if isinstance(message, dict):
        for k, v in message.items():
            s += f"{k}:{v}\n"
        message = s
    return "\n" + message

def send_message_to_line(message):
    Dist = "HRD"
    if Dist == "HRD":
        access_token = "uQSk2NNet76BrZaIudpg56I7HM1026g1jVVY53z3KX6"
    elif Dist == "Yu":
        access_token = "IGq5z7sGQQTJrLSmxIB6jVbnyFvxCu1iWvLTRpezN8J"
    
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    data = {"message": pprint(message)}
    requests.post("https://notify-api.line.me/api/notify",
                    headers = headers,
                    data=data
    )

if __name__ == "__main__":
    send_message_to_line({"amount":0.05,"rate":308})
