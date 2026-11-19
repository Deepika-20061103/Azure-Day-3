response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "system", "content": "You are a sentiment Analysis assistant. by considering user content analyse sentiment analysis"},
        {"role": "user", "content": "i am feeling bad today because this day made me more sad"}
    ]
)

print(response.choices[0].message.content)
