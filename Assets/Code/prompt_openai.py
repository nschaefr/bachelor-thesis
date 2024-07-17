response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": [{"type": "text", "text": system}]},
        {"role": "user", "content": [{"type": "text", "text": prompt}]},
    ],
    temperature=temperature,
    max_tokens=4096,
)
test_code = response.choices[0].message.content
