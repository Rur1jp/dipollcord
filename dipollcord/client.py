import requests

class pollclient:
    def __init__(self, token: str):
        self.token = token

    def sendPoll(
        self,
        channel_id: str,
        question: str,
        answers: list[str],
        content: str | None = None,
        duration: int = 1,
        allow_multiselect: bool = False
    ):
        url = f"https://discord.com/api/v10/channels/{channel_id}/messages"
        headers = {
            "Authorization": f"Bot {self.token}",
            "Content-Type": "application/json"
        }

        json = {
            "content": content,
            "poll": {
                "question": {"text": question},
                "answers": [
                    {"poll_media": {"text": a}}
                    for a in answers
                ],
                "allow_multiselect": allow_multiselect,
                "duration": duration,
                "layout_type": 1
            }
        }

        return requests.post(url, headers=headers, json=json)
