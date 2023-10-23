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
I have the following program:


```program
DEF run m( REPEAT R=6 r( WHILE c( frontIsClear c) w( move IFELSE c( rightIsClear c) i( turnRight ) ELSE e( turnLeft ) ) w IFELSE c( markersPresent c) i( pickMarker ) ELSE e( putMarker ) ) r )
```

But I need to transform it like the following:

```expected program
DEF run m( REPEAT R=6 r( WHILE c( frontIsClear c) w( move IFELSE c( rightIsClear c) i( turnRight i) ELSE e( turnLeft e) w) IFELSE c( markersPresent c) i( pickMarker i) ELSE e( putMarker e) r) m)
```

Here, the condition in WHILE statement starts with "c(" and ends with "c)", the WHILE statement should \
start with "w(" and end with "w)", the IF statement should start with "i(" and end with "i)" and the \
ELSE statement should start with "e(" and end with "e)".

Write a python code that can transform the above program to the expected program.
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
