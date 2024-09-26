import openai
import os

# Set your OpenAI API key here
openai.api_key = os.environ['OPENAI_KEY']

def summarize_text(text):
    try:
        # Call the OpenAI API with the chat model to summarize the text
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert summarizer."},
                {"role": "user", "content": f"Summarize the following text: {text}"}
            ]
        )

        # Extract and return the summary
        return response['choices'][0]['message']['content']
    except openai.error.OpenAIError as e:
        # Handle API errors
        return f"Error: {e}"

# Example usage
if __name__ == "__main__":
    # https://investor.capitalone.com/board-member/richard-fairbank
    long_text = """
    Mr. Fairbank is the founder, CEO and Chairman of Capital One and one of just a few founder-CEOs among America's largest public companies. In 1987, Mr. Fairbank founded Capital One on the belief that data and technology could change how banking works. He has been the CEO since the Company's initial public offering in November 1994, and has served as the Chairman since February 1995.
    Mr. Fairbank's vision and leadership have positioned Capital One as a leader in technology, data, and cloud capabilities and the Company has been recognized as one of the most innovative financial services providers in the world. Today, Capital One serves over 100 million customers and has reimagined the banking experience, built an iconic and respected brand, and been consistently recognized as one of the best companies to work for.
    Prior to Capital One, Mr. Fairbank earned his BA and MBA from Stanford University. He became a strategy consultant, advising leading companies on long-term business strategy and growth opportunities. Mr. Fairbank has over three decades of experience in banking and financial services. As the founder and CEO of Capital One, he is deeply knowledgeable about all aspects of the Company's businesses, strategies, capabilities and culture. His qualifications as a Director also include his broad range of skills in the areas of strategy, technology, risk management, customer experience, talent, and public company leadership and governance.
    """
    summary = summarize_text(long_text)
    print("Summary:", summary)
