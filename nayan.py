import speech_recognition as sr
import requests
import pyttsx3
import cv2
import base64
import os
import sys

# -------------------------------
# CONFIG - load API key from file
# -------------------------------
KEY_FILE = "api_key.txt"

def load_api_key(path=KEY_FILE):
    if not os.path.exists(path):
        print(f"ERROR: API key file not found: {path}")
        print("Create the file and paste your Gemini API key inside (single line).")
        sys.exit(1)
    with open(path, "r", encoding="utf-8") as f:
        key = f.read().strip()
    if not key:
        print(f"ERROR: API key file {path} is empty.")
        sys.exit(1)
    return key

API_KEY = load_api_key()
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

WAKE_WORD = "hey"

# -------------------------------
# FUNCTIONS
# -------------------------------

def capture_webcam_image():
    """Capture a single frame from the webcam and return as base64 JPEG."""
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("⚠️ Could not open webcam (VideoCapture returned false).")
        return None
    ret, frame = cap.read()
    cap.release()

    if not ret or frame is None:
        print("⚠️ Could not capture frame from webcam")
        return None

    # Encode image as JPEG
    _, buffer = cv2.imencode(".jpg", frame)
    img_base64 = base64.b64encode(buffer).decode("utf-8")
    return img_base64


def ask_gemini(prompt, use_camera=False):
    """Send query (and optional webcam image) to Gemini and return text reply."""
    headers = {
        "Content-Type": "application/json",
        "X-goog-api-key": API_KEY
    }

    parts = [{"text": prompt}]

    if use_camera:
        img_data = capture_webcam_image()
        if img_data:
            parts.append({
                "inline_data": {
                    "mime_type": "image/jpeg",
                    "data": img_data
                }
            })

    payload = {"contents": [{"parts": parts}]}

    try:
        r = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        r.raise_for_status()
    except requests.RequestException as e:
        print("⚠️ Request error:", e)
        return "Sorry, I couldn't reach the AI service."

    data = r.json()

    try:
        return data["candidates"][0]["content"]["parts"][0]["text"]
    except Exception:
        print("⚠️ Unexpected Gemini response format:", data)
        return "Sorry, I couldn't understand."


# -------------------------------
# MAIN LOOP
# -------------------------------
def main():
    recognizer = sr.Recognizer()
    tts = pyttsx3.init()

    # Optionally: adjust for ambient noise for better accuracy
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("🎤 Listening... Say 'Nayan' to activate.")
        while True:
            try:
                audio = recognizer.listen(source, timeout=None, phrase_time_limit=8)
            except Exception as e:
                # micro timeout or other listen error
                continue

            try:
                text = recognizer.recognize_google(audio).lower()
                print("You said:", text)

                if WAKE_WORD in text:
                    query = text.replace(WAKE_WORD, "").strip()

                    if not query:
                        print("✅ Wake word detected, waiting for command...")
                        continue

                    # Decide if webcam needed
                    use_camera = any(word in query for word in ["camera", "see", "look", "front", "show"])

                    print("👉 Query:", query, "| Camera:", use_camera)
                    reply = ask_gemini(query, use_camera=use_camera)
                    print("🤖 Gemini:", reply)

                    # Speak reply
                    tts.say(reply)
                    tts.runAndWait()

            except sr.UnknownValueError:
                # Could not understand audio
                continue
            except Exception as e:
                print("⚠️ Error in main loop:", e)


if __name__ == "__main__":
    main()
