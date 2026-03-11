import random
import time
import difflib

# -----------------------------
# Practice Content Generators
# -----------------------------

PUNCTUATION_SNIPPETS = [
    'for i in range(10):',
    'if __name__ == "__main__":',
    'def test_convert_to_datetime(value):',
    'result = my_function(arg1, arg2)',
    'while True:',
    'try:',
    'except ValueError as e:',
    'class MyClass(object):',
    'print("Hello, world!")',
    'with open("file.txt", "r") as f:',
    'data_dict = {"key": "value"}',
    'student_name = row["name"]',
    'lambda x: x * 2',
    'x, y = y, x',
    'items = [x for x in range(10)]',
    'self._private_var = value',
]

KEY_WORDS = [
    "convert", "date", "get", "manager", "process", "validate",
    "serialize", "deserialize", "request", "count",
    "response", "database", "connection", "data", "generator",
    "average", "argument", "temporary", "analyse", "explore"
]

# Common variable-name-like words (new primary pool)
WORDS = [
    "transaction", "total", "first_name", "last_name", "full_name",
    "age", "score", "words", "price", "numbers", "level", "record",
    "report", "pet", "train", "building", "battery"
]

# Combined list used by generators
ALL_WORDS = WORDS + KEY_WORDS


def random_snake_case():
    count = random.randint(2, 4)
    return "_".join(random.choice(ALL_WORDS) for _ in range(count))


def random_camel_case():
    count = random.randint(2, 4)
    words = [random.choice(ALL_WORDS).capitalize() for _ in range(count)]
    return "".join(words)


def random_mixed_phrase():
    patterns = [
        lambda: f"def {random_snake_case()}():",
        lambda: f"for i in range({random.randint(5, 50)}):",
        lambda: f"{random_snake_case()} = {random.randint(1, 100)}",
        lambda: f'class {random_camel_case()}:',
        lambda: f'print("{random_snake_case()}")',
    ]
    return random.choice(patterns)()


def get_random_prompt():
    generators = [
        lambda: random.choice(PUNCTUATION_SNIPPETS),
        random_snake_case,
        random_camel_case,
        random_mixed_phrase,
    ]
    return random.choice(generators)()


# -----------------------------
# Typing Session
# -----------------------------

def calculate_accuracy(target, typed):
    matcher = difflib.SequenceMatcher(None, target, typed)
    return matcher.ratio()


def run_session(duration_seconds):
    print("\nTyping session started! Type exactly what you see.\n")
    start_time = time.time()
    end_time = start_time + duration_seconds

    total_chars = 0
    total_typed_chars = 0
    total_correct_chars = 0
    total_mistakes = 0
    prompt_count = 0

    while time.time() < end_time:
        prompt = get_random_prompt()
        print("\nType this:")
        print(prompt)
        print()

        typed = input("> ")

        prompt_count += 1
        total_chars += len(prompt)
        total_typed_chars += len(typed)

        accuracy_ratio = calculate_accuracy(prompt, typed)
        correct_chars = int(accuracy_ratio * len(prompt))
        mistakes = len(prompt) - correct_chars

        total_correct_chars += correct_chars
        total_mistakes += mistakes

    elapsed_minutes = duration_seconds / 60
    words_typed = total_correct_chars / 5
    wpm = words_typed / elapsed_minutes if elapsed_minutes > 0 else 0
    accuracy_percent = (
        (total_correct_chars / total_chars) * 100 if total_chars > 0 else 0
    )

    print("\n" + "=" * 40)
    print("Session Complete!")
    print("=" * 40)
    print(f"Prompts completed: {prompt_count}")
    print(f"Total characters typed: {total_typed_chars}")
    print(f"Correct characters: {total_correct_chars}")
    print(f"Mistakes (approx): {total_mistakes}")
    print(f"Accuracy: {accuracy_percent:.2f}%")
    print(f"Words Per Minute (WPM): {wpm:.2f}")
    print("=" * 40)


# -----------------------------
# Main Program
# -----------------------------

def main():
    print("=== Programming Typing Speed Trainer ===")
    while True:
        try:
            duration = int(input("Enter session length in seconds: "))
            if duration <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a positive number.")

    run_session(duration)


if __name__ == "__main__":
    main()
