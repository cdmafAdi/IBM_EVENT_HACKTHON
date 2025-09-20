import requests
import os

# API Configuration
try:
    api_key = "r8_PsiIqW9PmowY2DNbzOunNED3KXlTfu62wZumR"


    # r8_PsiIqW9PmowY2DNbzOunNED3KXlTfu62wZumR
except KeyError:
    raise ValueError("LANGFLOW_API_KEY environment variable not found. Please set your API key in the environment variables.")

url = "http://localhost:7860/api/v1/run/26260e5b-1089-4a29-b64e-3b0f4ce2eb68"  # The complete API endpoint URL for this flow

# Request payload configuration
payload = {
    "output_type": "chat",
    "input_type": "chat",
    "input_value": "Create a travel itinerary for a trip from Pune to Dubai on October 23, 2025. The traveler enjoys , eating pão de queijo, and drinking special coffee."
}

# Request headers
headers = {
    "Content-Type": "application/json",
    "x-api-key": api_key  # Authentication key from environment variable
}

try:
    # Send API request
    response = requests.request("POST", url, json=payload, headers=headers)
    response.raise_for_status()  # Raise exception for bad status codes

    # Print response
    print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}")
except ValueError as e:
    print(f"Error parsing response: {e}")
