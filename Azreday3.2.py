response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "system", "content": "You are a named entity recognition assistant. Extract all person names, organization names, and locations from the user's text, and return them in JSON format with keys 'persons', 'organizations', 'locations'."},
        {"role": "user", "content": "Satya Nadella, CEO of Microsoft, announced a new partnership with the University of Washington in Seattle."}
    ]
)

print(response.choices[0].message.content)
