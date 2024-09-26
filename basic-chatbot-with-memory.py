import openai
import os

# Set your OpenAI API key here
openai.api_key = os.environ['OPENAI_KEY']

def chatbot_conversation():
    conversation_history = [
        {"role": "system", "content": "You are a friendly chatbot who helps users with general inquiries."}
    ]

    print("Start chatting with the bot (type 'exit' to end):")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break

        # Add user input to conversation history
        conversation_history.append({"role": "user", "content": user_input})

        try:
            # Call the OpenAI API with the chat model to generate a response
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=conversation_history
            )

            # Extract the assistant's response
            assistant_reply = response['choices'][0]['message']['content']
            print("Bot:", assistant_reply)

            # Add assistant's reply to conversation history
            conversation_history.append({"role": "assistant", "content": assistant_reply})

        except openai.error.OpenAIError as e:
            # Handle API errors
            print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    chatbot_conversation()
