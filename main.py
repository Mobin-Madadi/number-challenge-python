import random as r
import winsound
import os
import time
import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme('blue')

SAVE_FILE_SCORE = 'highscore.txt'
SAVE_FILE_BEST_TIME = 'besttime.txt'

window = ctk.CTk()
window.title("Number Generator")
window.geometry("900x650")
window.maxsize(900,650)
window.minsize(900,650)
window.configure(background="#669df6")

# Background
bg_image = ctk.CTkImage(
    light_image=Image.open('assets/Background.jpg'),
    dark_image=Image.open('assets/Background.jpg'),
    size=(900,650)
)

background_label = ctk.CTkLabel(
    window,
    image=bg_image,
    text=''
)

background_label.place(x=0,y=0,relwidth=1,relheight=1)

def  random_char():
    return r.choice(['+', '-', '*', '/'])


# High score
def load_highscore():
    if os.path.exists(SAVE_FILE_SCORE):
        with open(SAVE_FILE_SCORE, 'r') as f:
            try:
                return int(f.read())
            except:
                return 0

    return 0

def save_highscore(score):
    with open(SAVE_FILE_SCORE, 'w') as f:
        f.write(str(score))



# Record time
def load_best_time():
    if os.path.exists(SAVE_FILE_BEST_TIME):
        with open(SAVE_FILE_BEST_TIME, 'r') as f:
            try:
                return float(f.read())
            except:
                return 999.0
    return 999.0
def save_best_time(time):
    with open(SAVE_FILE_BEST_TIME, 'w') as f:
        f.write(str(time))


# Next Question
def new_question():
    global r1, r2, operator , start_time

    r1 = r.randrange(1,100)
    r2 = r.randrange(1,100)
    operator = random_char()
    title_one.configure(
        text="🧮 Number Challenge",
        text_color="white"
    )
    random_title.configure(text=f"{r1} {operator} {r2} = ?")
    hint_button.configure(text="💡 Hint")
    start_time = time.time()

r1 = r.randrange(1,100)
r2 = r.randrange(1,100)
operator = "+"



# Winner & Loser
win = 0
lose = 0
high_score = load_highscore()

# Timing
best_time = load_best_time()
start_time = time.time()

# Main Frame
main_frame = ctk.CTkFrame(
    window,
    width=750,
    height=560,
    corner_radius=10,
    # fg_color="#1E293B",
    fg_color=("#F8F9FA", "#1E293B"),
    border_width=1,
    border_color="#4F8EF7"
)
main_frame.place(relx=0.5,
                 rely=0.5,
                 anchor="center")

# Labels
title_one = ctk.CTkLabel(
    main_frame,
    text="🧮 Number Challenge",
    font=("Segoe UI",26,"bold")
)
title_one.place(x=375, y=30,anchor='center')

random_title = ctk.CTkLabel(
    main_frame,
    text=f"{r1} {operator} {r2} = ?",
    font=("Segoe UI",40,"bold")
)
random_title.place(x=375,y=90,anchor='center')

answer_text = ctk.CTkLabel(
    main_frame,
    text='Answer: ',
    font=('Arial', 15 , 'bold')
)
answer_text.place(x=150,y=135)


# Win Frame
win_frame = ctk.CTkFrame(
    window,
    width=140,
    height=100,
    corner_radius=10,
    fg_color=("black",'white'),

)
win_frame.place(
    relx=0.20,
    rely=0.68,
    anchor="center"
)

winner_text = ctk.CTkLabel(
    win_frame,
    text=f'🏆 Wins: {win}',
    font=('Arial', 15, 'bold'),
    text_color=("white",'black')

)
winner_text.place(relx=0.5, rely=0.5 ,anchor='center')


# Lose Frame
lose_frame = ctk.CTkFrame(
    window,
    width=140,
    height=100,
    corner_radius=10,
    fg_color=("black",'white')

)
lose_frame.place(
    relx=0.40,
    rely=0.68,
    anchor="center"
)

loser_text = ctk.CTkLabel(
    lose_frame,
    text=f'❌ Loses: {lose}',
    font=('Arial', 15, 'bold'),
    text_color=("white",'black')
)
loser_text.place(relx=0.5, rely=0.5 ,anchor='center')


progress = ctk.CTkProgressBar(
    main_frame,
    mode="determinate",
    corner_radius=10,
    width=350,
    height=15,
)
progress.place(x=375,y=300,anchor='center')
progress.set(1)

timer_label = ctk.CTkLabel(
    main_frame,
    text="10 s",
    font=("Segoe UI", 16, "bold")
)
timer_label.place(x=570, y=300, anchor="center")

# High Score Frame
high_score_frame = ctk.CTkFrame(
    window,
    width=140,
    height=100,
    corner_radius=10,
    fg_color=("black",'white')

)
high_score_frame.place(
    relx=0.60,
    rely=0.68,
    anchor="center"
)
high_score_label = ctk.CTkLabel(
    high_score_frame,
    text=f'⭐ High Score: {high_score}',
    font=('Arial', 15 , 'bold'),
    text_color=("white",'black')
)

high_score_label.place(relx=0.5, rely=0.5 ,anchor='center')

# Record Time Frame
record_time_frame = ctk.CTkFrame(
    window,
    width=140,
    height=100,
    corner_radius=10,
    fg_color=("black",'white')

)
record_time_frame.place(
    relx=0.80,
    rely=0.68,
    anchor="center"
)
record_time = ctk.CTkLabel(
    record_time_frame,
    text=f'Best Time: {best_time:.2f}',
    font=('Arial', 15, 'bold'),
    text_color=("white",'black')
)
record_time.place(relx=0.5,rely=0.5,anchor='center')

switch = ctk.CTkSwitch(
    main_frame,
    text="Dark Mode"
)

switch.place(x=60,y=25,anchor='center')


footer = ctk.CTkLabel(
    main_frame,
    text='Python • CustomTkinter • Version 1.0 \n Made with ❤️ by Mobin Madadi',

)
footer.place(relx=0.5,
             rely=0.98,
             anchor="s")

# Entry
answer_entry = ctk.CTkEntry(
    main_frame,
    font=("Segoe UI",18),
    placeholder_text="Enter your answer...",
    width=280,
    height=45
)
answer_entry.place(x=375,y=150,anchor='center')

# Sound answer
def play_correct():
    winsound.MessageBeep(winsound.MB_ICONASTERISK)
def play_incorrect():
    winsound.MessageBeep(winsound.MB_ICONHAND)

# Change Mode
def change_mode():
    if switch.get():
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("dark")

switch.configure(command=change_mode)

# Update Timer
timer_id = None
time_left = 10

def Timer():
    global timer_id, time_left, lose

    progress.set(time_left / 10)

    timer_label.configure(text=f"⏱ {time_left}s")
    if time_left > 5:
        timer_label.configure(text=f"⏱ {time_left}s", text_color="white")
    elif time_left > 2:
        timer_label.configure(text=f"⏱ {time_left}s", text_color="orange")
    else:
        timer_label.configure(text=f"⏱ {time_left}s", text_color="red")


    progress["value"] = time_left

    if time_left > 0:
        time_left -= 1
        timer_id = window.after(1000, Timer)
    else:
        lose += 1
        loser_text.configure(text=f"Lose: {lose}")
        title_one.configure(
            text="⏰ Time's Up!",
            text_color="red"
        )
        new_question()

        time_left = 10
        Timer()



# Checks
def Check():
    global win , lose , timer_id , time_left , best_time , record_time

    if timer_id:
        window.after_cancel(timer_id)


    time_left = 10
    Timer()



    try:
        user_val = int(answer_entry.get())
        if operator == '+':
            correct = r1 + r2
        elif operator == '-':
            correct = r1 - r2
        elif operator == '*':
            correct = r1 * r2
        else:
            correct = r1 // r2

        if user_val == correct:
            win += 1
            end_time = time.time()
            elapsed_time = end_time - start_time
            if elapsed_time < best_time:
                best_time = elapsed_time
                save_best_time((best_time))
                record_time.configure(text=f"Best Time: {best_time:.2f}s")



            winner_text.configure(text=f'Win: {win}')
            title_one.configure(
                text="✔ Correct!",
                text_color="#22C55E"
            )


            global high_score
            score = win - lose
            if score > high_score:
                high_score = score
                save_highscore(high_score)
                high_score_label.configure(text=f"⭐ High Score: {high_score}")


            play_correct()
            window.after(1000, new_question)
        else:
            lose += 1
            loser_text.configure(text=f'Lose: {lose}')
            title_one.configure(
                text="✖ Wrong!",
                text_color='#EF4444'
            )
            play_incorrect()
            new_question()


        answer_entry.delete(0, 'end')

    except ValueError:
        pass




# Hint
def hint():
    if operator == '+':
        correct = r1 + r2
    elif operator == '-':
        correct = r1 - r2
    elif operator == '*':
        correct = r1 * r2
    else:
        correct = r1 // r2

    hint_button.configure(text=f"💡: {correct}")


# Quit
def exit_game():
    window.destroy()


# Button
submit = ctk.CTkButton(
    main_frame,
    command=Check,
    text="✓ Submit",
    cursor="hand2",
    font=("Segoe UI",15,"bold"),
    hover_color='#1D4ED8',
    corner_radius=18,
    width=220,
    height=45,
    fg_color='#2563EB',

)
submit.place(x=375,y=210,anchor='center')

hint_button = ctk.CTkButton(
    main_frame,
    command=hint,
    text="💡 Hint",
    cursor="hand2",
    font=("Segoe UI",13,"bold"),
    corner_radius=18,
    height=45,
    text_color='black',
    fg_color="#EAB308",
    hover_color='#fdd982',
)
hint_button.place(relx=0.15,rely=0.90,anchor='center')

quit_button = ctk.CTkButton(
    main_frame,
    command=exit_game,
    text="✖ Quit",
    cursor="hand2",
    font=("Segoe UI",13,"bold"),
    corner_radius=18,
    height=45,
    fg_color="#DC2626",
    hover_color='#ff634d'
)
quit_button.place(relx=0.85,rely=0.90,anchor='center')


# Main Loop
window.mainloop()