import streamlit as st 
import requests
import json

# Page setup
st.set_page_config(page_title="Smartest AI Nutrition Assistant", layout="centered")
st.title("The Smartest AI Nutrition Assistant")

# IBM Cloud API Key
API_KEY = "fKEeYdtdc9qb0lBJLk0yvcZSNXGBrFj55KxufEVYV3hh"
ROLE = "user"

# Input area
content = st.text_area("Enter your query to Smart Assistant:", height=100, value="")

# Submit button
if st.button("Submit"):
    if not content.strip():
        st.warning("Please enter a message.")
    else:
        try:
            with st.spinner("Getting IBM access token..."):
                token_response = requests.post(
                    'https://iam.cloud.ibm.com/identity/token',
                    data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'}
                )
                token_response.raise_for_status()
                mltoken = token_response.json()["access_token"]

            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + mltoken
            }

            payload_scoring = {
                "messages": [
                    {"content": content, "role": ROLE}
                ]
            }

            with st.spinner("Sending request to IBM Watson..."):
                response_scoring = requests.post(
                    'https://us-south.ml.cloud.ibm.com/ml/v4/deployments/eddd2256-5fba-47ae-b8a4-10bc53bd125e/ai_service?version=2021-05-01',
                    json=payload_scoring,
                    headers=headers
                )

            # ✅ Extract content from JSON response
            result = response_scoring.json()

            if "choices" in result and len(result["choices"]) > 0:
                extracted = result["choices"][0]["message"]["content"]
            else:
                extracted = "No content found in response."

            # Show clean text response
            st.markdown("### 💡 AI Assistant’s Answer")
            st.write(extracted)

        except requests.exceptions.RequestException as e:
            st.error(f"Network error: {e}")
        except Exception as e:
            st.error(f"Error: {e}")

                            # extracted = result[key]
