import random
import datetime

print ("🤖 RiZZ Bot: Welcome, Hooman! Let's get to know each other First")

name = input("What's your name? ")
gender = input("Are you male or female?").lower()

if gender == "female":
    bot_name = "💘 CupidBot"
    intro = f"{bot_name}: Oh hello, {name} 💖! Ready to be charmed and slightly roasted?"
else:
    bot_name = "😎 LOLBot"
    intro = f"{bot_name}: Yo {name}! Hope you're ready to get roasted like your last code review 🔥"

print("\n" + intro)
print(f"{bot_name}: Type 'help' to see what I can do. Type 'bye' to escape my rizz 😏")

    
jokes_female = [
    "You're like a semicolon... optional but powerful 😏",
    "If debugging removes bugs, you're the feature 🐞",
    "Roses are red, code is fine, you’re the commit I’d never decline 💻💘"
]

jokes_male = [
    "Your code runs slower than Monday morning ☕",
    "You debug like it’s a guessing game 🎲",
    "You have more bugs than a picnic in summer 🐜"
]

motivation_female = [
    "You're not a coder. You're a queen of logic 👑💻",
    "Keep slaying those bugs, one line at a time 💅🔥",
    "You’re the if-statement in my else-world 💘"
]

motivation_male = [
    "Push through like Git — commit to greatness 🛠️",
    "Bro, you got this! StackOverflow believes in you 😤",
    "You’re like a dark theme — low key but powerful 💻🖤"
]

roasts_female = [
    "You’re the reason 'undefined' exists in JavaScript 💁‍♀️",
    "If being dramatic was a function, you'd be recursive 🔁",
    "You're like CSS — all about looks but hard to control 😈"
]

roasts_male = [
    "You’re like a try block without an except — crashing constantly 💥",
    "If intelligence was RAM, you'd be a floppy disk 💾",
    "Even Ctrl+Z can't undo your bad decisions 💀"
]

while True:
    print("\n💬 Suggestions: hello | time | joke | motivation | weather | your name | help | bye")
    user_input = input("You: ").lower()
    
    if user_input == "hello":
        if gender == "female":
            print(f"{bot_name}: Heyyy {name} 💖! Your smile could fix all syntax errors!")
        else:
            print(f"{bot_name}: Sup {name}? You look... like a merge conflict 😎")

    elif user_input == "time":
        now = datetime.datetime.now().strftime("%H:%M:%S")
        if gender == "female":
            print(f"{bot_name}: It's {now} — time to slay, queen 👑")
        else:
            print(f"{bot_name}: It's {now} — time to drink water & pretend you're working ⏰")

    elif user_input == "joke":
        if gender == "female":
            print(f"{bot_name}: {random.choice(jokes_female)}")
        else:
            print(f"{bot_name}: {random.choice(jokes_male)}")

    elif user_input == "motivation":
        if gender == "female":
            print(f"{bot_name}: {random.choice(motivation_female)}")
        else:
            print(f"{bot_name}: {random.choice(motivation_male)}")

    elif user_input == "weather":
        if gender == "female":
            print(f"{bot_name}: It’s raining compliments today — you better carry confidence ☔💅")
        else:
            print(f"{bot_name}: The only storm is in your error logs ⛈️💻")

    elif user_input == "your name":
        print(f"{bot_name}: I’m {bot_name}, the CEO of charm and chaos 💋🔥")

    elif user_input == "roast":
        if gender == "female":
            print(f"{bot_name}: {random.choice(roasts_female)}")
        else:
            print(f"{bot_name}: {random.choice(roasts_male)}")
        print("💌 P.S. Sorry if that roast stung... it comes from a place of ❤️")

    elif user_input == "help":
        print(f"""
📘 {bot_name} Command List:
- hello (I say hi in style)
- time (because clocks are boring)
- joke (I throw shade)
- motivation (fake it till you make it)
- weather (I’m not Google, but I try)
- your name (spoiler: it’s me, not you)
- help (this)
- bye (you sure?)
    """)
        

    elif user_input == "bye":
        if gender == "female":
            print(f"{bot_name}: Awww you're leaving already, {name}? I'll miss roasting you 💔👋")
        else:
            print(f"{bot_name}: Peace out, {name}. Don’t forget to `git commit` your life choices 😎👋")
        break

    else:
        print(f"{bot_name}: I didn’t understand that, but I'll act like I did. Type 'help' , genius 😏")