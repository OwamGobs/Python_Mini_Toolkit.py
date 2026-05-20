import random
import datetime

# Module: Quotes
# Provides generic and mood-specific motivational quotes and
# short challenges. The functions below return a quote, a small
# challenge, and a contextual bonus tip based on time/day.

# Generic quotes used when no mood-specific match is found.
quotes = [
    "Keep going, you are doing great!",
    "Believe in yourself and all that you are.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "Don't watch the clock; do what it does. Keep going.",
    "Small progress is still progress.",
]

# Generic challenge items used as a fallback.
Challenges = [
    "challenge: Review your notes for 30 minutes.",
    "challenge: Solve 5 practice problems.",
    "challenge: Teach a concept you learned to a friend or family member.",
    "challenge: Take breaks if you feel overwhelmed.",
]

# Mood-specific messages
# Each key maps to a dict with `quotes` and `challenges` lists.
# The `mood_based_motivation` function selects one item from each list when the user's input matches the mood.
mood_map = {
    "happy": {
        "quotes": [
            "Keep riding this wave — use the energy to make progress!",
            "Your positive moments are fuel for consistent success.",
        ],
        "challenges": [
            "challenge: Share what you learned with someone else.",
            "challenge: Tackle a difficult topic while you're focused.",
        ],
    },
    "sad": {
        "quotes": [
            "It's okay to feel down. Small steps count — keep going.",
            "Be kind to yourself today; progress isn't always linear.",
        ],
        "challenges": [
            "challenge: Do a 10-minute review — gentle and focused.",
            "challenge: Take one small action that makes you feel better.",
        ],
    },
    "stressed": {
        "quotes": [
            "Breathe. Break tasks into smaller parts and start with one.",
            "Stress is temporary — small consistent actions reduce it.",
        ],
        "challenges": [
            "challenge: Use the Pomodoro technique for 25 minutes.",
            "challenge: List three quick wins and complete one.",
        ],
    },
    "tired": {
        "quotes": [
            "Rest is productive too — recharge and come back stronger.",
            "Short, focused sessions beat long, exhausted ones.",
        ],
        "challenges": [
            "challenge: Do a 15-minute light review or summary.",
            "challenge: Choose one small task you can complete now.",
        ],
    },
    "anxious": {
        "quotes": [
            "Focus on one small step — clarity follows action.",
            "You're more capable than your anxiety suggests.",
        ],
        "challenges": [
            "challenge: Write down one worry then plan a tiny action.",
            "challenge: Practice 5 deep breaths, then study for 10 minutes.",
        ],
    },
    "bored": {
        "quotes": [
            "Switch things up — a small change can boost focus and curiosity.",
            "Boredom is a signal — try a short, different learning activity."
        ],
        "challenges": [
            "challenge: Try a new exercise or problem type for 20 minutes.",
            "challenge: Break a topic into tiny tasks and complete one now."
        ],
    },
    "confused": {
        "quotes": [
            "Confusion means you're learning — clarity comes with small steps.",
            "Ask one good question and you'll often find the path forward."
        ],
        "challenges": [
            "challenge: Write down what you understand, then list gaps to resolve.",
            "challenge: Watch a short explainer or re-read a single paragraph slowly."
        ],
    },
}


def display_quote():
    """Return a random generic quote and a random generic challenge.

    This is used as a fallback when the user's mood cannot be
    confidently mapped to one of the mood-specific keys.
    """
    return random.choice(quotes), random.choice(Challenges)


def get_bonus_Tip(weekday, hour):
    """Return a contextual bonus tip based on weekday and hour.

    - `weekday` follows Python's `datetime.weekday()` convention
      where Monday == 0 and Sunday == 6.
    - The tip varies for weekend mornings, weekday evenings,
      and specific weekdays (example: Monday/Thursday reminders).
    """
    if weekday >= 5 and hour < 12:
        return "Bonus Tip: It's the weekend morning, a great time to plan your week!"
    elif weekday < 5 and hour >= 18:
        return "Bonus Tip: It's weekday evening, a perfect time to review your progress!"
    elif weekday == 0 or weekday == 4:
        return "Bonus Tip: It's Monday or Thursday, a great time to set goals for the week and reflect on your progress!"
    else:
        return "Bonus Tip: Keep up the good work and stay consistent with your study routine!"


def mood_based_motivation(mood, weekday, hour):
    """Return (quote, challenge, bonus_tip) aligned with the user's mood.

    The function normalizes free-text mood input and compares it to a
    set of common keywords for each supported mood. If a matching
    mood is found we select one quote and one challenge from
    `mood_map`. Otherwise we fall back to generic messages.
    """
    m = (mood or "").strip().lower()

    # map common keywords to mood keys for more flexible user input
    keywords_map = {
        "happy": ["happy", "good", "great", "joy", "joyful", "excited", "motivated", "confident"],
        "sad": ["sad", "down", "unhappy", "blue", "depressed", "lonely"],
        "stressed": ["stress", "stressed", "overwhelm", "overwhelmed", "panic", "pressure"],
        "tired": ["tired", "exhaust", "sleepy", "drained", "fatigued"],
        "anxious": ["anx", "anxious", "nerv", "worried", "worry"],
        "bored": ["bored", "bore", "meh", "uninterested"],
        "confused": ["confused", "lost", "unclear", "stuck"],
    }

    # Find the first matching mood key
    key = None
    for k, kws in keywords_map.items():
        for kw in kws:
            if kw in m:
                key = k
                break
        if key:
            break

    # Choose mood-specific or generic messages
    if key and key in mood_map:
        quote = random.choice(mood_map[key]["quotes"])
        challenge = random.choice(mood_map[key]["challenges"])
    else:
        quote, challenge = display_quote()

    bonus = get_bonus_Tip(weekday, hour)
    return quote, challenge, bonus