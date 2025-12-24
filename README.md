<h1 align="center">🎙️ Neon Voice Calculator</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Tkinter-00599C?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Speech_Recognition-FF6F00?style=for-the-badge&logo=google-cloud&logoColor=white" />
</p>

<p align="center">
  <b>A sleek, high-performance voice-activated calculator featuring a modern Neon aesthetic and real-time speech processing.</b>
</p>

---

## 📺 Live Demo
<p align="center">
  <img src="demo.gif" width="300" alt="Neon Calculator Animation">
  <br>
  <i>(If you only have demo.mp4, drag it into a GitHub Issue comment to generate a link, or convert it to GIF)</i>
</p>

---

## ✨ Key Features

* **⚡ Real-Time VUI**: Seamless Voice User Interface integration using Google Speech API.
* **🎨 Neon Dark Mode**: Custom-styled Tkinter UI with a high-contrast palette.
* **🔄 Multi-Threading**: Non-blocking background threads for smooth microphone listening.
* **🔊 TTS Feedback**: Instant auditory confirmation of results using `pyttsx3`.
* **💓 Pulse Animation**: Dynamic button color cycling to indicate "active listening" state.

---

## 🛠️ Tech Stack & Logic


| Module | Implementation |
| :--- | :--- |
| **Frontend** | Tkinter (Grid Layout) |
| **Speech-to-Text** | `SpeechRecognition` + PyAudio |
| **Text-to-Speech** | `pyttsx3` (Sapi5/NSSS engine) |
| **Processing** | Python `eval()` with String Mapping |

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python 3.x installed. You will also need `PyAudio` (which might require specific wheels for Windows).

### 2. Installation
```bash
# Clone the repository
git clone [https://github.com/SIDDUSPACE/Voice-Calculator-Python.git](https://github.com/SIDDUSPACE/Voice-Calculator-Python.git)

# Install dependencies
pip install SpeechRecognition pyaudio pyttsx3
```
