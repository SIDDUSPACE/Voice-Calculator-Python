import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
import pyttsx3
import threading

class StylishVoiceCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Calculator")
        self.root.geometry("350x550")
        self.root.configure(bg="#1e1e1e")  
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.is_listening = False
        self.display = tk.Entry(root, font=("Segoe UI", 32), bg="#1e1e1e", fg="#00ffcc", 
                                borderwidth=0, justify='right', insertbackground='white')
        self.display.pack(pady=30, padx=20, fill="x")
        self.btn_frame = tk.Frame(root, bg="#1e1e1e")
        self.btn_frame.pack(pady=10)
        self.create_buttons()
        self.v_btn = tk.Button(root, text="🎤 START LISTENING", font=("Segoe UI", 12, "bold"),
                               bg="#00ffcc", fg="#1e1e1e", activebackground="#00cca3",
                               relief="flat", height=2, command=self.start_voice_thread)
        self.v_btn.pack(side="bottom", fill="x", padx=30, pady=20)

    def create_buttons(self):
        buttons = [
            ('7', '#333333'), ('8', '#333333'), ('9', '#333333'), ('/', '#ff9500'),
            ('4', '#333333'), ('5', '#333333'), ('6', '#333333'), ('*', '#ff9500'),
            ('1', '#333333'), ('2', '#333333'), ('3', '#333333'), ('-', '#ff9500'),
            ('C', '#ff3b30'), ('0', '#333333'), ('=', '#00ffcc'), ('+', '#ff9500')
        ]
        
        row, col = 0, 0
        for (text, color) in buttons:
            fg_color = "#1e1e1e" if text in ['=', '/','*','-','+'] else "white"
            btn = tk.Button(self.btn_frame, text=text, width=5, height=2, font=("Segoe UI", 14, "bold"),
                            bg=color, fg=fg_color, relief="flat", activebackground="#555555",
                            command=lambda x=text: self.click_event(x))
            btn.grid(row=row, column=col, padx=8, pady=8)
            col += 1
            if col > 3:
                col = 0
                row += 1
    def pulse_animation(self):
        """Creates a red glowing pulse effect while the mic is active"""
        if self.is_listening:
            current_color = self.v_btn.cget("bg")
            next_color = "#ff3b30" if current_color == "#b32a22" else "#b32a22"
            self.v_btn.config(bg=next_color, text="Listening...", fg="white")
            self.root.after(500, self.pulse_animation)
        else:
            self.v_btn.config(bg="#00ffcc", text="🎤 START LISTENING", fg="#1e1e1e")
    def start_voice_thread(self):
        """Runs listening in a background thread to prevent the UI from freezing"""
        self.is_listening = True
        self.pulse_animation()
        thread = threading.Thread(target=self.listen_voice)
        thread.start()

    def listen_voice(self):
        with sr.Microphone() as source:
            try:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.7)
                audio = self.recognizer.listen(source, timeout=5)
                text = self.recognizer.recognize_google(audio).lower()
                replacements = {
                    'plus': '+',
                    'minus': '-',
                    'times': '*',
                    'multiply': '*',
                    'multiplied by': '*',
                    'into': '*',
                    'x': '*',
                    'divide': '/',
                    'divided by': '/',
                    'by': '/'
                }
                
                for word, symbol in replacements.items():
                    text = text.replace(word, symbol)
                text = text.replace(" ", "")
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, text)
                self.root.after(800, self.calculate)
                
            except Exception:
                self.engine.say("Sorry, I didn't catch that.")
                self.engine.runAndWait()
            
            self.is_listening = False

    def click_event(self, key):
        if key == '=': self.calculate()
        elif key == 'C': self.display.delete(0, tk.END)
        else: self.display.insert(tk.END, key)

    def calculate(self):
        try:
            expr = self.display.get()
            if not expr: return
            result = eval(expr)
            if isinstance(result, float) and result.is_integer():
                result = int(result)
                
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
            self.engine.say(f"The answer is {result}")
            self.engine.runAndWait()
        except Exception:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")

if __name__ == "__main__":
    root = tk.Tk()
    app = StylishVoiceCalculator(root)
    root.mainloop()