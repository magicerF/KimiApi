import requests
import execjs


class KIMI:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {}
        self.id = None

    def kimi_chat(self, jsonData):
        data = execjs.compile(open('body.js', 'r', encoding='utf-8').read()).call("get_body", jsonData)
        body_bytes = bytes(data)
        response = self.session.post('https://www.kimi.com/apiv2/kimi.gateway.chat.v1.ChatService/Chat',
                                     data=body_bytes)
        return response.text.split('"id":"')[1].split('"')[0]

    def kimi_GetChat(self, id):
        self.session.headers.pop('content-type')
        json_data = {
            'chat_id': id,
        }

        response = self.session.post(
            'https://www.kimi.com/apiv2/kimi.gateway.chat.v1.ChatService/GetChat', json=json_data,
        )
        return response.json()['chat']['messageContent']

    def kimi_DelChat(self, id):
        json_data = {
            'chat_id': id,
        }

        response = self.session.post(
            'https://www.kimi.com/apiv2/kimi.chat.v1.ChatService/DeleteChat',
            json=json_data,
        )
        return response.text

    def kimi_ListMessage(self, id):
        json_data = {
            'chat_id': id,
            'page_size': 1000,
        }

        response = self.session.post(
            'https://www.kimi.com/apiv2/kimi.gateway.chat.v1.ChatService/ListMessages',
            json=json_data,
        )

        for message in response.json()['messages']:
            if message['role'] == "assistant":
                return message['blocks'][-1]['text']['content']
        return response.json()['messages']

    def kimi_GetOutputFileTree(self, id):
        json_data = {
            'chat_id': id,
        }

        response = self.session.post(
            'https://www.kimi.com/apiv2/kimi.gateway.mcp.v1.OKCService/GetOutputFileTree',
            json=json_data,
        )
        return response.json()['downloadUrl']

    def kimi_TextQuestion(self, question):
        try:

            self.id = None
            jsonData = {
                "scenario": "SCENARIO_K2D5",
                "tools": [{"type": "TOOL_TYPE_SEARCH", "search": {}}],
                "message": {
                    "role": "user",
                    "blocks": [{"message_id": "", "text": {"content": question}}],
                    "scenario": "SCENARIO_K2D5"
                },
                "options": {"thinking": False}
            }
            self.id = kimi.kimi_chat(jsonData)
            chatContent = kimi.kimi_GetChat(self.id)
            content = kimi.kimi_ListMessage(self.id)
            delChat = kimi.kimi_DelChat(self.id)
            return content
        except Exception as e:
            delChat = kimi.kimi_DelChat(self.id)
            return delChat if delChat else str(e)

    def kimi_ImageQuestion(self, question):
        try:
            self.id = None
            jsonData = {
                "scenario": "SCENARIO_OK_COMPUTER",
                "tools": [{"type": "TOOL_TYPE_SEARCH", "search": {}}],
                "message": {
                    "role": "user",
                    "blocks": [{"message_id": "", "text": {"content": question}}],
                    "scenario": "SCENARIO_OK_COMPUTER"
                },
                "options": {"thinking": False},
                "kimiplus_id": "ok-computer"
            }
            self.id = kimi.kimi_chat(jsonData)
            chatContent = kimi.kimi_GetChat(self.id)
            downloadUrl = self.kimi_GetOutputFileTree(self.id)
            delChat = kimi.kimi_DelChat(self.id)
            return downloadUrl
        except Exception as e:
            delChat = kimi.kimi_DelChat(self.id)
            return delChat if delChat else str(e)


if __name__ == '__main__':
    kimi = KIMI()
    # print(kimi.kimi_TextQuestion("写一段xxx代码"))
    print(kimi.kimi_ImageQuestion("生成xxx图片"))