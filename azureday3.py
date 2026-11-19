!pip install openai
! pip install azure-ai-ml
!python -m pip install azure-identity
from openai import AzureOpenAI
endpoint = "https://project401-resource.services.ai.azure.com/api/projects/project401"
api_key = "Dd2eOP5rZQGNCkdRpLgosRLGPlltRFkKD3ITY2EbcYWQ5pfHhLSGJQQJ99CKACF24PCXJ3w3AAAAACOGkHPL"
deployment_name = "gpt-5-mini"
from openai import OpenAI

# Connect to Azure OpenAI
client = OpenAI(
    base_url=f"{endpoint.rstrip('/')}/openai/v1/",
    api_key=api_key
)

# Your GPT-5-mini deployment name
deployment_name = "gpt-5-mini"

# Call the model
response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "user", "content": "who is the cm of Andhra Pradesh in 2026?"}
    ]
)

print(response.choices[0].message.content)
