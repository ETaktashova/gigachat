import time
from typing import List, Optional
import uuid
import requests

rquid = str(uuid.uuid4())


class BaseApi:
    def completions(self, *args, **kwargs) -> str:
        raise NotImplementedError


class GigaChatApi(BaseApi):
    _token: Optional[str] = None
    _token_time: float = 0

    def __init__(self,
                 authorization_data: str,
                 scope: str = 'GIGACHAT_API_PERS'
                 ) -> None:
        self.authorization_data = authorization_data
        self.scope = scope

    def _get_token(self) -> str:

        if (
            self._token and
            self._token_time and
            (time.monotonic() - self._token_time < 1000)
        ):
            return self._token

        print(f'self.authorization_data: {self.authorization_data}')
        headers = {
            'Authorization': f'Bearer {self.authorization_data}',
            'RqUID': str(uuid.uuid4()),
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {'scope': self.scope}
        response = requests.post(
            "https://ngw.devices.sberbank.ru:9443/api/v2/oauth",
            headers=headers,
            data=data,
            verify=False
        )
        if response.status_code == 200:
            self._token_time = time.monotonic()
            self._token = response.json()["access_token"]
            if isinstance(self._token, str):
                return self._token
        raise Exception(f'Error[{response.status_code}]: {response.text}')

    def completions(self,
                    messages: List[dict],
                    model: str = 'GigaChat:latest',
                    temperature: int = 1
                    ) -> str:
        token = self._get_token()
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }
        data = {
            'messages': messages,
            'model': model,
            'temperature': temperature,
        }
        response = requests.post(
            'https://gigachat.devices.sberbank.ru/api/v1/chat/completions',
            headers=headers,
            json=data,
            verify=False
        )
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        raise Exception(f'Error[{response.status_code}]: {response.text}')


class LlamaCppApi(BaseApi):
    # TODO: write this
    pass

# class ChatGTPApi(BaseApi):
#     # TODO: write this
#     pass
