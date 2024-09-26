
# Image Generation PoC using OpenAI API

This is a simple Python Proof of Concept (PoC) for generating images using the OpenAI DALL-E model based on text prompts. It demonstrates how to interact with the OpenAI API to create custom images and download them locally.

## Prerequisites

- Python 3.7+
- OpenAI Python library

## Installation

1. **Clone the Repository** (if applicable) or create a new project directory:

   ```bash
   git clone https://github.com/Smith-MichaelJ1995/gpt-api-quickstart.git
   cd gpt-api-quickstart
   ```

2. **Install Required Packages**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Obtain OpenAI API Key**:
   - Sign up at [OpenAI](https://beta.openai.com/signup/) and get an API key.
   - Set your API key in the script or as an environment variable.

## Usage

1. **Set Your API Key**:

   Replace `"your_openai_api_key"` in the script with your actual OpenAI API key or set it as an environment variable:

   ```bash
   export OPENAI_KEY='your_openai_api_key'
   ```

## Tutorials

1. **Run the Script**:

   ```bash
   python <script-name>.py
   ```
## Usage

1. **Set Your API Key**:

   Make sure your OpenAI API key is set as an environment variable (`OPENAI_KEY`).

2. **Run the Script**:

   ```bash
   python basic-chatbot.py
   ```

3. **Start Chatting**:

   Begin the conversation with the chatbot by entering your queries. Type 'exit' to end the chat.

   ```
   You: What is the weather like today?
   Bot: I'm sorry, but I can't access real-time information. How can I assist you with something else?
   ```

4. **Conversation History**:

   The chatbot maintains the context of the conversation, allowing for more natural and coherent interactions.

## Customization

- **Change the System Message**: Modify the initial message in the `conversation_history` to change the chatbot's behavior and personality.

   ```python
   {"role": "system", "content": "You are a helpful assistant that specializes in technology-related queries."}
   ```

- **Handle Different User Inputs**: You can extend the functionality by adding specific responses or actions for particular user inputs.

## Example Output

<div align="center">
    <video width="600" controls>
        <source src="https://drive.google.com/uc?export=download&id=1slhjkD8XcmcSo6DO47sPyiEjMyIyTaci" type="video/mp4">
        Your browser does not support the video tag.
    </video>
</div>


## Downloading Images

The script includes an optional function to download the generated images locally. To enable it, uncomment the relevant section in `generate_image.py` and run the script again.

```python
# Uncomment to download images
for idx, url in enumerate(image_urls, 1):
    file_name = f"image_{idx}.png"
    download_image(url, file_name)
    print(f"Downloaded {file_name}")
```

## Customization

- **Number of Images**: Change the `n` parameter in the `generate_image` function to generate multiple images.
- **Image Size**: Modify the `size` parameter (`256x256`, `512x512`, `1024x1024`) to specify the image resolution.
- **Text Prompt**: Update the `image_prompt` variable with your desired text description.

## Example Output

![Example Image](example.png) *(Replace with a URL or local path to an example image)*

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [OpenAI](https://www.openai.com/) for providing the API and resources.
