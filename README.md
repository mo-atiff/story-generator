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
