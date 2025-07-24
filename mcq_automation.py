import pyperclip
import time
import threading
import requests
from plyer import notification
from PIL import Image, ImageDraw
import pystray
import tkinter as tk
from tkinter import messagebox

# 🔐 Gemini API Configuration
API_KEY = "Your_API_KEY"  # Replace with your full Gemini API key
MODEL = "gemini-2.0-flash"

# 🔍 Tkinter setup (must run in main thread)
root = tk.Tk()
root.withdraw()  # Hide root window

def show_popup(title, msg):
    def _popup():
        top = tk.Toplevel()
        top.title(title)
        top.attributes("-topmost", True)  # Always on top
        top.geometry("420x160+600+300")   # Slightly wider
        top.resizable(False, False)
        top.configure(bg="#1e1e2f")

        top.focus_force()  # 🔥 Focus popup so Esc works immediately

        # Frame for styling
        frame = tk.Frame(top, bg="#1e1e2f")
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        label = tk.Label(
            frame,
            text=msg,
            wraplength=380,
            justify="left",
            padx=10,
            pady=10,
            bg="#1e1e2f",
            fg="#ffffff",
            font=("Segoe UI", 11)
        )
        label.pack(pady=(10, 10))

        btn = tk.Button(
            frame,
            text="✖ Close",
            command=top.destroy,
            bg="#3a3a4f",
            fg="#ffffff",
            activebackground="#5a5a7f",
            activeforeground="#ffffff",
            relief="flat",
            padx=12,
            pady=6,
            font=("Segoe UI", 10)
        )
        btn.pack()

        # 🔑 Esc key shortcut to close
        top.bind("<Escape>", lambda event: top.destroy())

        # ⏱️ Auto close after 15 seconds
        top.after(15000, top.destroy)

    root.after(0, _popup)



# 🧠 Gemini API request
def ask_gemini_clipboard(text):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"
    headers = {"Content-Type": "application/json"}

    prompt = f"""
You are an expert at solving MCQs and general questions.

Given the following text, extract or infer the best possible answer in one line.
Options may be labeled A/B/C or bullets or not present at all.

Text:
{text}

Answer:
"""
    data = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    try:
        res = requests.post(url, headers=headers, json=data)
        res.raise_for_status()
        return res.json()["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        return f"Error: {e}"

# 📋 Clipboard watcher
def watch_clipboard():
    prev_text = ""
    while True:
        try:
            text = pyperclip.paste().strip()
            if text and text != prev_text:
                print(f"[📋 Copied] {text}")
                answer = ask_gemini_clipboard(text)
                print(f"[✅ Gemini Answer]: {answer}\n")

                # 🔔 System notification
                notification.notify(
                    title="Gemini Answer",
                    message=answer,
                    timeout=5
                )

                # 🧊 Optional GUI popup (non-blocking)
                show_popup("Gemini Answer", answer)

                prev_text = text
        except Exception as e:
            print(f"Error: {e}")

        time.sleep(1)

# 🖼️ System tray icon
def create_image():
    image = Image.new('RGB', (64, 64), color='black')
    draw = ImageDraw.Draw(image)
    draw.ellipse((16, 16, 48, 48), fill='lightblue')
    return image

def on_exit(icon, item):
    icon.stop()
    root.quit()  # Quit tkinter safely

# 🔽 Tray icon setup
def setup_tray_icon():
    icon = pystray.Icon("GeminiClipboard")
    icon.icon = create_image()
    icon.title = "Gemini Clipboard MCQ Solver"
    icon.menu = pystray.Menu(
        pystray.MenuItem("Exit", on_exit)
    )

    threading.Thread(target=watch_clipboard, daemon=True).start()
    icon.run()

# ▶️ Entry point
if __name__ == "__main__":
    print("📋 Gemini Clipboard Solver is running in the background...")
    threading.Thread(target=setup_tray_icon, daemon=True).start()
    root.mainloop()  # Tkinter main loop (must run in main thread)
