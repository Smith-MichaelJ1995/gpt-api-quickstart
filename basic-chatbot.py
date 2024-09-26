import openai
import os

# Set your OpenAI API key here
openai.api_key = os.environ['OPENAI_KEY']

def chat_with_gpt4(prompt):
    try:
        # Call the OpenAI API with the chat model
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        # Extract and return the assistant's response
        return response['choices'][0]['message']['content']
    except openai.error.OpenAIError as e:
        # Handle API errors
        return f"Error: {e}"

# Example usage
if __name__ == "__main__":
    user_prompt = input("Enter your question for GPT-4: ")
    reply = chat_with_gpt4(user_prompt)
    print("GPT-4 Response:", reply)
