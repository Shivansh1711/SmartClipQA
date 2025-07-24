# ✨ Gemini Clipboard MCQ Solver ✂️🤖

An intelligent clipboard automation tool that **monitors your clipboard**, detects **MCQs or questions**, and instantly uses the **Gemini API** to generate a concise **one-line answer**, showing it in both a **system tray notification** and a **popup UI**.

---

## 📌 Features

- 🔍 **Clipboard Watcher** — Detects new copied text automatically.
- 🧠 **Gemini Integration** — Uses Google's Gemini (Gemini 1.5 Flash) to answer.
- 🖼️ **System Tray App** — Runs in the background, easy to exit.
- 🪟 **Popup Dialogs** — Lightweight Tkinter UI shows quick answers.
- 🔔 **Desktop Notifications** — Pops a notification with the Gemini response.

---

## 📷 Preview

> ✂️ Copy this to see the magic:
```
Which data structure uses FIFO?
A) Stack
B) Queue
C) Tree
D) Graph
```

> 💬 Output:
> `[✅ Gemini Answer]: Queue`

---

## 🚀 Getting Started

### 1. 🔧 Requirements

Install dependencies:

```bash
pip install pyperclip requests plyer pystray pillow
```

> 🐍 Python 3.7+ required  
> 💡 Works on Windows (Linux/Mac support in progress)

---

### 2. 🔑 Gemini API Key

Get your **Gemini API Key** from:  
👉 [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

Then replace:
```python
API_KEY = "Your_API_KEY"
```

---

### 3. ▶️ Run the Script

```bash
python mcq_automation.py
```

You should see:
```bash
📋 Gemini Clipboard Solver is running in the background...
```

> 📌 Your tray will now show a circle icon. Right-click > Exit to close.

---

## 💻 How It Works

| Action                        | Result                               |
|------------------------------|--------------------------------------|
| Copy any question or MCQ     | Gemini gives answer in one line      |
| Runs silently in tray        | No console blocking                  |
| System notification appears  | Shows the one-line answer            |
| Popup window (optional)      | Displays answer in small dialog box  |

---

## 🧪 Sample Questions to Try

```
What is the capital of Australia?
A) Sydney
B) Melbourne
C) Canberra
D) Brisbane
```

```
Which gas is essential for photosynthesis?
- Nitrogen
- Oxygen
- Carbon Dioxide
- Helium
```

---

## 📁 File Structure

```
mcq_automation.py    # Main script
README.md            # This file
```

---

## ❌ Troubleshooting

- ❗ Popup not showing? → Ensure `tkinter` is installed and no thread conflict.
- 🛑 Script crashes instantly? → Check your internet and API key validity.
- 🔕 No notifications? → Windows Focus Assist or notification permissions.

---

## ❤️ Author

> Built with 💻 and ☕ by **@Shivansh Ojha**  
> Uses Gemini, Tkinter, Plyer, and Python standard libraries.

---

## 📜 License

MIT License — Free to use, share, or extend.