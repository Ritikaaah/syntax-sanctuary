import random
mood= input("How are you feeling today? (happy, tired, sad, angry): ").lower()
messages = {
    "happy": [
        "Keep smiling, sunshine! ☀️",
        "Your happiness is contagious! 💕",
        "You’re glowing — stay that way! ✨"
    ],
    "sad": [
        "It’s okay to feel down sometimes 💙",
        "Sending you a big virtual hug 🤗",
        "You’re stronger than you think 💫"
    ],
    "tired": [
        "Rest, recharge, and rise again 🌙",
        "You deserve a cozy nap 😴",
        "Even stars need to rest before they shine ✨"
    ],
    "angry": [
        "Take a deep breath — peace will find you 🌿",
        "It’s okay to cool down first 💧",
        "Let it out gently; you’ll feel lighter ❤️"
    ]
}
if mood in messages:
    print(random.choice(messages[mood]))
else:
    print("Hmm, I don't know that mood — but you're amazing anyway! 💖")