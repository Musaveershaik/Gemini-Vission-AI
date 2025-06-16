---

# Gemini Vission AI

Gemini Vission AI is a Streamlit web application that uses Google Gemini models to analyze images and respond to prompts.
You can try it live here 👉 [Gemini Vission AI App](https://gemini-vission.streamlit.app/)

## Features

* Upload an image (`.jpg`, `.jpeg`, `.png`)
* Provide a text prompt (optional)
* Get AI-generated insights about the image

## How to run locally

1️⃣ Clone the repo:

```bash
git clone https://github.com/Musaveershaik/Gemini-Vission-AI.git
cd Gemini-Vission-AI
```

2️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```

3️⃣ Create a `.streamlit/secrets.toml` file:

```toml
GOOGLE_API_KEY = "YOUR_GOOGLE_API_KEY"
```

4️⃣ Run the app:

```bash
streamlit run streamlit_app.py
```

## Requirements

* streamlit
* Pillow
* google-generativeai

(These are listed in `requirements.txt`.)

## Live App

🌐 [Gemini Vission AI](https://gemini-vission.streamlit.app/)

---
