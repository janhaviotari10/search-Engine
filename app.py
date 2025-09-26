import streamlit as st
import pyttsx3
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit as kit
import datetime
from requests import get
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

st.title("SEARCH ENGINE")

st.sidebar.subheader("Commands")

command = st.selectbox("Select a command:", [
    "Wikipedia Search",
    "Open Website",
    "Tell Time",
    "Get Weather Information",
    "Send an Email",
    "Play a YouTube Video",
    "Open Application",
    "Exit Jarvis",
])

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def send_email(to, content):
    try:
        # Set up the server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # Login credentials
        server.login('your_email@gmail.com', 'your_password')
        # Send email
        server.sendmail('your_email@gmail.com', to, content)
        server.close()
        return True
    except Exception as e:
        return str(e)

def get_weather(city):
    api_key = "5fc4234cefc55b2b6931f1e9fedfadaa"  # Use your valid API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = get(base_url).json()
    
    # Check if the response contains 'main'
    if response.get("cod") != "404" and "main" in response:
        weather_data = response["main"]
        temperature = weather_data["temp"] - 273.15
        pressure = weather_data["pressure"]
        humidity = weather_data["humidity"]
        weather_description = response["weather"][0]["description"]
        weather_info = (
            f"\nTemperature: {temperature:.2f}°C\n"
            f"\nAtmospheric pressure: {pressure} hPa\n"
            f"\nHumidity: {humidity}%\n"
            f"\nDescription: {weather_description}"
        )
        return weather_info
    elif response.get("cod") == "401":
        return "Invalid API key. Please check your OpenWeatherMap API key."
    else:
        return "City not found or another error occurred. Please check the city name and try again."


def main():
    if command == "Wikipedia Search":
        st.subheader("Wikipedia Search")
        query = st.text_input("Enter your search query:")
        if st.button("Search"):
            st.write("Searching on Wikipedia...")
            results = wikipedia.summary(query, sentences=2)
            st.write("According to Wikipedia")
            st.write(results)

    elif command == "Open Website":
        st.subheader("Open Website")
        website = st.text_input("Enter the website URL:")
        if st.button("Open"):
            st.write(f"Opening {website}. Please wait...")
            webbrowser.open(website)

    elif command == "Tell Time":
        st.subheader("Tell Time")
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        if st.button("Show"):
            speak(f"The time is {strTime}")

    elif command == "Get Weather Information":
        st.subheader("Get Weather Information")
        city = st.text_input("Enter the city name:")
        if st.button("Get Weather"):
            weather_info = get_weather(city)
            st.write(weather_info)

    elif command == "Send an Email":
        st.subheader("Send an Email")
        to = st.text_input("Enter recipient email:")
        content = st.text_area("Enter the email content:")
        if st.button("Send"):
            result = send_email(to, content)
            if result is True:
                st.success(f"Email sent to {to}")
            else:
                st.error(f"Failed to send email: {result}")

    elif command == "Play a YouTube Video":
        st.subheader("Play a YouTube Video")
        video = st.text_input("Enter the video title or URL:")
        if st.button("Play"):
            kit.playonyt(video)
            st.write(f"Playing {video} on YouTube")

    elif command == "Open Application":
        st.subheader("Open Application")
        app = st.selectbox("Select an application:", [
            "Visual Studio Code",
            "PowerPoint",
            "Word",
            "Excel",
            "Dev C++",
            "Notepad",
            "Calculator",
            "Paint",
            "Google Chrome"
        ])

        app_paths = {
            "PowerPoint": "C:\\Program Files\\Microsoft Office\\Office16\\POWERPNT.EXE",
            "Word": "C:\\Program Files\\Microsoft Office\\Office16\\WINWORD.EXE",
            "Visual Studio Code": r"C:\\Users\\dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
            "Excel": "C:\\Program Files\\Microsoft Office\\Office16\\EXCEL.EXE",
            "Dev C++": "C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe",
            "Notepad": "C:\\Windows\\system32\\notepad.exe",
            "Calculator": "C:\\Windows\\system32\\calc.exe",
            "Paint": "C:\\Windows\\system32\\mspaint.exe",
            "Google Chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        }

        if app in app_paths:
            if st.button("Open"):
                os.startfile(app_paths[app])
        else:
            st.error("Invalid choice")

    elif command == "Exit Jarvis":
        st.subheader("Exit Jarvis")
        if st.button("Exit"):
            speak("Goodbye!")
            st.stop()

if __name__ == "__main__":
    main()
