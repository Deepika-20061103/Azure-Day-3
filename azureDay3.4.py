response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "system", "content": "You are a text summarizer assistant. by considering user content summarize my text into 3 lines"},
        {"role": "user", "content": """Dear Participant,

Last Saturday, we witnessed an incredible virtual round of the Odoo x NMIT Bangalore Hackathon 2026, and we’d love to hear about your experience! We have already started assessment to declare the virtual round result on time.

Your learning, challenges, problem-solving moments, team collaboration, and overall hackathon journey matter to us. 

We encourage you to share your experience and memories on social media (especially on LinkedIn) and let the world know what your hackathon journey was like.

Don’t forget to tag Odoo on LinkedIn and use the hashtags:
#odoohackathon
#odooxnmit26
Your stories not only inspire fellow participants and future developers but also help us capture the incredible energy and spirit of the hackathon.

We’re looking forward to reading your stories and celebrating your journey with you! 

With regards,
Team Odoo"""}
    ]
)

print(response.choices[0].message.content)
