# Quillify.ai

## Introduction
Quillify.ai is an innovative application that allows users to create customized stories, generate images, and compile them into videos with audio. It leverages the power of AI models such as OpenAI and Hugging Face to generate engaging and personalized content.

## Table of Contents
- [Introduction](#introduction)
- [Table of Contents](#table-of-contents)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Documentation](#documentation)
- [Examples](#examples)
- [Videos](#videos)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)
- [License](#license)

## Installation
To install and run Quillify.ai locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/mo-atiff/story-generator.git
    cd story-generator
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    streamlit run quillify_ai.py
    ```

## Usage
1. Open the application in your web browser as directed by Streamlit.
2. Enter your OpenAI and Hugging Face API tokens in the sidebar.
3. Input a story prompt, select the desired number of words, voice gender, and image style.
4. Click "Generate Story" to create your customized story.
5. The generated story, images, and video will be displayed and saved to the gallery.

## Features
- **Story Generation**: Generate customized stories based on user prompts.
- **Image Generation**: Create detailed images using AI models.
- **Video Compilation**: Combine images and audio to create a video.
- **Voice Synthesis**: Convert text to speech using different voice options.
- **Gallery**: View and manage generated videos.

## Dependencies
- Streamlit
- Langchain
- HuggingFace Hub
- Spacy
- PIL
- Moviepy
- Pyttsx3
- Mutagen

## Configuration
- **OpenAI API Key**: Required for story generation.
- **Hugging Face API Token**: Required for image generation.

## Documentation
For detailed documentation on using Quillify.ai, refer to the code comments and functions within `quillify_ai.py`, `demo.py`, and `gallery.py`.

## Examples
Here is an example of generating a story:

1. **Input Prompt**: "A young boy with blue eyes embarks on a journey to the moon in a rocket he built with his friends."
2. **Generated Story**: Displays the story text generated by the AI.
3. **Generated Images**: Displays images created from the story text.
4. **Generated Video**: Compiles images and audio into a video.

## Videos
Here are some example videos generated using Quillify.ai:

1. **Video 1**: [Animals World](https://mega.nz/file/ZxdGWIxa#ldIcug9PrBJd0YwzaA72GwfqZz4B5ogNuoa5BOUHPLs)
2. ![Preview](vids/mars.mp4)
3. **Video 2**: [Boy on Mars](https://mega.nz/file/EkUHGZYR#8lWd2l56wUEqXTMWJKBGlJm1105ZmRqwpZxXqfA07ps)
4. **Video 3**: [Treasure Island](https://mega.nz/file/ggEUnQBS#QShTxb0LPaq3q5GodtNRODaDOE8jQ8RzNfh7JF73xiA)
5. **Video 4**: [Love Story](https://mega.nz/file/M8kFHazT#l0FSrFFVDYH7u-eA9Gpb42UwFmtGBpEcTg63_MExOPw)

## Troubleshooting
If you encounter any issues, consider the following steps:
- Ensure that you have entered valid API keys for OpenAI and Hugging Face.
- Check the console for error messages and stack traces.
- Reload the application and try again.

## Contributors
- **Atif Shaik** - [GitHub Profile](https://github.com/mo-atiff)

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
