# Story Generator Project

## Description
This is a Streamlit-based web application for generating stories and creating corresponding videos with images and voice narration. The project uses OpenAI's GPT-3.5 Turbo model and Hugging Face's DALL-E model for text and image generation, respectively.

## Docker Image Usage

### Pulling the Docker Image
To use the Story Generator project, you can pull the Docker image from Docker Hub. Follow these steps in your terminal:

```bash
docker pull atiff/story_gen_docker:latest
```

### Running the Docker Container
After pulling the image, you can run the Docker container with the following command:

```bash
docker run -p 8501:8501 atiff/story_gen_docker:latest
```

#### Open a browser and go to localhost:8501 to see the application

## Configuration

### API KEYS
Upon running the Streamlit app, you will be prompted to enter your OpenAI API key and Hugging Face API token. Please provide these keys to enable text and image generation functionalities.

## Usage

- Enter your OpenAI API key and Hugging Face API token.\n
- Pull the Docker image and run the container.\n
- Access the Streamlit app through your web browser.
- Provide a story prompt in the text input.\n
- Adjust the number of words for the generated story using a slider.
- Select the gender of the voice for narration and the style of images (Realistic, Cartoon, or Anime).
- Click the "Generate Story" button to create the story, voice narration, and video.

## License 
This project is licensed under the MIT License.
