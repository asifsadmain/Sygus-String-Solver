import openai

openai.api_key = "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"

# user_message = f"""
# The following is the Context Free Grammar (CFG) for the Karel domain:

# ```
# Program ρ := DEF run m( s m)
# Repetition n := Number of repetitions
# Perception h := frontIsClear | leftIsClear | rightIsClear | markerPresent | noMarkerPresent
# Condition b := perception h | not perception h
# Action a := move | turnLeft | turnRight | putMarker | pickMarker
# Statements := while c( b c) w( s w) | s1;s2 | a | repeat R=n r( s r) | if c( b c) i( s i) |
# ifelse c( b c) i(s1 i) else e( s2 e)
# ```

# Now, I have an 6x6 grid where the bot needs to pick a marker from a stair. The marker is at the top of the stairs. \
# If the row and column indices are from 0 to 5 and the bottomleft cell is (0,0), then the stairs create block at \
# (0,1), (0,2), (1,2), (1,3), (2,3),(2,4), (3,4), (3,5) and (4,5). The marker is placed at (5,5). This problem is called "StairClimber".

# Your task is to write a program following the above CFG that can complete the "StairClimber" task.
# """

user_message = f"""
I have the following code segment:
```
found = False
last_program = None
latest_io_log = None
error_message = None
count = 0

while(not found):
    if (count == 3):
        break

    try:
        program, found, io_log = synthesize(last_program, error_message, latest_io_log)
        latest_io_log = io_log
    except Exception as e:
        error_message = e
    finally:
        last_program = program

    count += 1
```

When the code throws exception, the "last_program" becomes "None". But I want to have the last_program assigned as program even when the exception is thrown.
"""

response = openai.ChatCompletion.create(
model="gpt-4",
messages=[
        {"role": "user", "content": user_message}
    ],
temperature=0,
max_tokens=256
)

print(response['choices'][0]['message']['content'])
