import tkinter as tk
from tkinter import messagebox
import time
import random

sentences = [
    "Python programming is fun and useful.",
    "Typing speed improves with regular practice.",
    "Debugging helps find errors in code.",
    "Fonts should display characters consistently.",
    "Learning by building projects is effective.",
    "Students at SB Jain College Nagpur work on innovative technology projects.",
    "The campus of SB Jain Institute encourages learning and creativity.",
    "Many engineering students practice coding daily in the computer labs.",
    "SB Jain College Nagpur organizes technical events and workshops.",
    "The library provides useful books for programming and research.",
    "Students collaborate on Python and C plus plus development projects.",
    "Faculty members guide students in building practical applications.",
    "Hackathons and coding competitions are popular among students.",
    "The institute supports innovation and problem solving skills.",
    "Engineering students improve typing and coding speed regularly.",
    "Computer science labs are equipped with modern systems.",
    "Students learn data structures and algorithms step by step.",
    "Practical learning is an important part of college education.",
    "Teamwork helps students complete academic projects successfully.",
    "Technology based learning is encouraged across all departments.",
    "Many students participate in research and development activities.",
    "Workshops help students understand real world applications.",
    "The college environment motivates students to learn programming.",
    "Regular practice improves both typing accuracy and speed.",
    "Projects like typing testers help students understand Python better."
]

# Automatically generate more SB Jain sentences until we reach 500
topics = [
    "coding practice",
    "technical workshops",
    "software development",
    "innovation projects",
    "engineering education",
    "computer science labs",
    "team collaboration",
    "research activities",
    "technology learning",
    "programming skills"
]

actions = [
    "improves student knowledge",
    "helps build strong careers",
    "encourages practical learning",
    "develops problem solving ability",
    "supports modern education",
    "creates better opportunities",
    "motivates innovation",
    "strengthens technical skills",
    "builds confidence",
    "prepares students for industry"
]

while len(sentences) < 1000:
    topic = random.choice(topics)
    action = random.choice(actions)
    new_sentence = f"At SB Jain College Nagpur, {topic} {action} for engineering students."
    sentences.append(new_sentence)

start_time = 0
selected_sentence = ""

def start_test():
    global start_time, selected_sentence
    selected_sentence = random.choice(sentences)
    sentence_label.config(text=selected_sentence)
    input_box.delete("1.0", tk.END)
    result_label.config(text="")
    start_time = time.time()

def submit_test():
    global start_time
    end_time = time.time()
    typed_text = input_box.get("1.0", tk.END).strip()

    time_taken = end_time - start_time
    word_count = len(typed_text.split())
    wpm = (word_count / time_taken) * 60 if time_taken > 0 else 0

    correct_chars = 0
    for i in range(min(len(typed_text), len(selected_sentence))):
        if typed_text[i] == selected_sentence[i]:
            correct_chars += 1

    accuracy = (correct_chars / len(selected_sentence)) * 100

    font_status = check_font_issues(typed_text)

    result = f"Speed: {int(wpm)} WPM\nAccuracy: {accuracy:.2f}%\nFont Status: {font_status}"
    result_label.config(text=result)

def check_font_issues(text):
    unstable_chars = []
    for ch in text:
        if ch in "@#$%^&*~`":
            unstable_chars.append(ch)

    if unstable_chars:
        return f"Inconsistent characters detected {set(unstable_chars)}"
    else:
        return "Font looks stable"

# GUI
root = tk.Tk()
root.title("Typing Tester")
root.geometry("700x450")
root.configure(bg="#1f1f2e")

# Title
title = tk.Label(
    root,
    text="Typing Tester",
    font=("Segoe UI", 26, "bold"),
    bg="#1f1f2e",
    fg="#ffffff"
)
title.pack(pady=15)

# Sentence container
sentence_frame = tk.Frame(root, bg="#2c2c3e", padx=20, pady=15)
sentence_frame.pack(pady=10)

sentence_label = tk.Label(
    sentence_frame,
    text="Click Start test to begin typing test",
    wraplength=600,
    font=("Segoe UI", 14),
    bg="#2c2c3e",
    fg="#ffffff",
    justify="center"
)
sentence_label.pack()

# Input box
input_box = tk.Text(
    root,
    height=5,
    width=65,
    font=("Consolas", 12),
    bd=0,
    relief="flat",
    highlightthickness=2,
    highlightbackground="#4CAF50"
)
input_box.pack(pady=15)

# Buttons frame
button_frame = tk.Frame(root, bg="#1f1f2e")
button_frame.pack(pady=10)

start_btn = tk.Button(
    button_frame,
    text="Start Test",
    font=("Segoe UI", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    activebackground="#45a049",
    width=14,
    command=start_test
)
start_btn.grid(row=0, column=0, padx=10)

submit_btn = tk.Button(
    button_frame,
    text="Submit",
    font=("Segoe UI", 12, "bold"),
    bg="#2196F3",
    fg="white",
    activebackground="#1e88e5",
    width=14,
    command=submit_test
)
submit_btn.grid(row=0, column=1, padx=10)

# Result box
result_frame = tk.Frame(root, bg="#2c2c3e", padx=20, pady=10)
result_frame.pack(pady=15)

result_label = tk.Label(
    result_frame,
    text="Results will appear here",
    font=("Segoe UI", 13, "bold"),
    bg="#2c2c3e",
    fg="#00ffcc"
)
result_label.pack()

root.mainloop()