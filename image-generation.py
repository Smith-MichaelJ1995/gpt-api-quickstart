import openai
import os

# Set your OpenAI API key here
openai.api_key = os.environ['OPENAI_KEY']

def generate_image(prompt, n=1, size="1024x1024"):
    try:
        # Call the OpenAI API to generate an image based on the text prompt
        response = openai.Image.create(
            prompt=prompt,
            n=n,
            size=size
        )

        # Return the URLs of the generated images
        return [image['url'] for image in response['data']]
    except openai.error.OpenAIError as e:
        # Handle API errors
        return f"Error: {e}"

# Example usage
if __name__ == "__main__":
    image_prompt = "Sunset on a beautiful sunny California beach from perspective of a mountain"
    image_urls = generate_image(image_prompt)

    # Display the URLs of the generated images
    for idx, url in enumerate(image_urls, 1):
        print(f"Image {idx} URL: {url}")
