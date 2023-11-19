import openai
from openai import OpenAI
import os

class TextCompletion:

    def __init__(self, prompt, num_token):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI()
        self.all_responses = list()
        self.prompt = prompt
        self.num_token = num_token

    def chunk_response(self):
        if self.num_token > 4096:
            step = 2000
            for i in range(0,len(self.prompt), step):

                print('Processo de chunk iniciado:')

                response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": "Summarize the following text in original language within 150 words"},
                        {"role": "assistant", "content": "Yes."},
                        {"role": "user", "content": self.prompt[i:i+step]},
                    ],
                )

                self.all_responses += response.choices[0].message.content
        else:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": "Summarize the following text in original language"},
                    {"role": "assistant", "content": "Yes."},
                    {"role": "user", "content": self.prompt},
                ],
            )

            self.all_responses += response.choices[0].message.content

    def final_response(self):

        self.chunk_response()

        response_summarize = self.client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Summarize the following text in original language"},
            {"role": "assistant", "content": "Yes."},
            {"role": "user", "content": ''.join(self.all_responses)},
        ],
        stream = True
    )
        
        chunk_message = ''

        for chunk in response_summarize:
            if chunk.choices[0].delta.content is None:
                pass
            else:
                chunk_message += chunk.choices[0].delta.content

            yield chunk_message