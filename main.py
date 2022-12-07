import json
import os
import openai

openai.api_key = "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"
# openai.Model.list()
# json_string=json.dumps(openai.Model.retrieve("text-davinci-003").__dict__)
# model=json.loads(json_string)
# print(type(model))
# print(model["_response_ms"])
prompt = openai.Completion.create(
    model="text-davinci-003",
    prompt="Difference between Parallel and Distributed Systems",
    max_tokens=1000,
    temperature=0
)
# print(prompt)
json_string = json.dumps(prompt.__dict__)
model = json.loads(json_string)
# print(type(model))
# print(model['_previous']['choices'][0])
print(model['_previous']['choices'][0]['text'])
