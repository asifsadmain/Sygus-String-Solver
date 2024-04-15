import openai
import re

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
# Now your tasks are the following 1:
# 1. Understand all the symbols of the given CFG in the context of this given 'Climbing Monkey' environment.
# """

user_message = f"""
We have an environment called 'Poachers and Rangers' where 2 teams called poachers and rangers are competing with each other in a national park and its surroundings. The park has 60 gates in total. The goal for each team is to defeat the opponents.

Now I have the following CFG to write programs for poachers in the above environment:
    CFG for Poachers:
    ```
    S -> SA | A
    A -> attack(n)
    n -> 1 | 2 | 3 | ... | 59 | 60
    ```
    The following is the CFG to write programs for rangers:
    CFG for Rangers:
    ```
    S -> SA | A
    A -> defend(n)
    n -> 1 | 2 | 3 | ... | 59 | 60
    ```

The following is the explanation of the above CFG:
    CFG Explanation:
    ```
    S: Starting symbol that can contain one or multiple actions.
    A: Refers to the action taken by the team.
    attack(n): Refers to the action to attack the n-th gate of the park
    defend(n): Refers to the action to defend the n-th gate of the park
    n: Any positive integer up to 60.
    ...: It is not part of the CFG. It has been used to indicate all positive numbers in between.
    ```

The following are some guidelines for writing the strategy program:
Strategy Writing Guidelines:
```
1. There is NO NEED TO write classes or initiate objects such as Poachers, Rangers, Gates, etc. There is NO NEED TO write comments.
2. DO NOT write '...' in the program, since it is not a part of the CFG.
3. Write only the action or the sequence of actions such as 'attack(a)' or 'attack(a) attack(b) attack(c)' where a, b and c are positive integers.
```

Now I have the following strategy program for the rangers that satisfies the CFG, written inside <strategy1></strategy1> tag:
<strategy1>
attack(1) attack(12)
</strategy1>

Now your tasks are the following 5:
        1. Understand all the symbols of the given CFG in the context of this given 'Poachers and Rangers' environment.
        2. Write an improved strategy2 for rangers that can defeat strategy1.
        3. You must not use any symbols (for example 'S ->', '->', '|', etc.) outside the given CFG. Write only the action or the sequence of action as mentioned in the strategy writing guideline.
        4. Write only the new strategy program inside the <rangersStrategy></rangersStrategy> tag.
        5. Check the strategy program and ensure it does not violate the rules of the CFG or the guidelines for writing the strategy.
"""

response = openai.ChatCompletion.create(
model="gpt-3.5-turbo",
messages=[
        {"role": "user", "content": user_message}
    ],
temperature=1
)

print(response['choices'][0]['message']['content'])

# pattern = r'<strategy>(.*?)<\/strategy>'
pattern = r'<rangersStrategy>(.*?)<\/rangersStrategy>'

matches = re.findall(pattern, response['choices'][0]['message']['content'], re.DOTALL)

#     # Print the extracted text
program = matches[0].strip()
print(program)
