# 🔎 Search Engine with Streamlit

A simple **personal search assistant** built using **Python & Streamlit**.  
This app can search Wikipedia, check the weather, send emails, play YouTube videos, open applications, and more — all from a single interface.  

---

## 📂 Project Structure
search-engine-streamlit/
│
├── app.py # Main Streamlit application
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── .gitignore # Files to ignore in Git


---

## 📸 Demo
(Add a screenshot or GIF of your app here)  

---

## ✨ Features
- 🔍 **Wikipedia Search** – get quick summaries  
- 🌐 **Open Website** – launch any URL in your browser  
- ⏰ **Tell Time** – announces the current time using TTS  
- 🌦 **Weather Information** – fetch real-time weather via OpenWeatherMap API  
- 📧 **Send Email** – send emails via Gmail SMTP  
- ▶️ **Play YouTube Video** – play any video using `pywhatkit`  
- 💻 **Open Applications** – launch apps like Word, Excel, VS Code, Notepad, etc.  
- 👋 **Exit Jarvis** – gracefully stop the app  

---

## 🛠️ Built With
- [Python](https://www.python.org/)  
- [Streamlit](https://streamlit.io/)  
- [pyttsx3](https://pypi.org/project/pyttsx3/) – Text-to-Speech  
- [Wikipedia](https://pypi.org/project/wikipedia/)  
- [pywhatkit](https://pypi.org/project/pywhatkit/)  
- [Requests](https://pypi.org/project/requests/)  

---

## 🚀 Installation (Local Setup)

1. **Clone the repository**
   ```bash
   git clone https://github.com/YourUsername/search-engine-streamlit.git
   cd search-engine-streamlit

======================================================================

## Install dependencies
pip install -r requirements.txt

Set environment variables
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_email_password
OPENWEATHER_API_KEY=your_openweather_api_key

=================================================================

Run the app
streamlit run app.py

📖 Usage
Select a command from the sidebar.

Example:
Wikipedia Search → Enter a query → Get a 2-line summary
Get Weather → Enter city name → Get temperature, humidity, pressure
Play a YouTube Video → Enter title/URL → Opens in browser
Send Email → Enter recipient & message → Send directly

⚙️ Configuration
Weather API: Requires an OpenWeatherMap
 API key
Email: Works with Gmail SMTP — you may need an App Password instead of your real password
Applications: Modify the app_paths dictionary in app.py to match your system paths

====================================================================================

👩‍💻 Author
GitHub: janhaviotari10

======================================================================================
