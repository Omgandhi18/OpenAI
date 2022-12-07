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
    prompt="Write SQL code to Select All data from Students Table ",
    max_tokens=1000,
    temperature=0
)
# print(prompt)
json_string = json.dumps(prompt.__dict__)
model = json.loads(json_string)
# print(type(model))
# print(model['_previous']['choices'][0])
print(model['_previous']['choices'][0]['text'])
image=openai.Image.create(
    prompt="Doctor operating on a Sea otter",
    n=1,
    size="1024x1024",
)
# print(image)
json_string1=json.dumps(image.__dict__)
image_model=json.loads(json_string1)
# print(image_model)
print(image_model['_previous']['data'][0]['url'])
