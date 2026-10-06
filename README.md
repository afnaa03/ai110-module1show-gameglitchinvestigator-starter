# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.
### Game Purpose
The purpose of the game is for the player to guess a randomly generated secret number within a certain range. The game gives the player hints and a limited number of attempts based on the selected difficulty.

### Bugs I Found
I found several bugs while testing the game. The hint would tell the player to guess lower even when the secret number was higher. Changing the difficulty did not correctly update the number range. I also found that starting a new game did not fully reset the previous game because the guess history remained and the game did not work correctly after restarting.

### Fixes I Applied
I fixed the high and low hint logic so the game gives the correct hint based on the player's guess. I also fixed the difficulty logic so the number range updates based on the selected difficulty. Lastly, I fixed the new game functionality so the game state resets properly, including the attempts and guess history.
## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. I selected Easy difficulty and confirmed that the number range updated correctly.
2.  I entered a guess that was lower than the secret number. 
3. The game correctly gave me a hint to guess higher.
4. I continued entering guesses until the game ended.
5. I clicked New Game and confirmed that the previous guess history was cleared. 
6.  The attempts reset and I was able to start guessing again. 


**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

python -m pytest -v
================= test session starts =================
platform darwin -- Python 3.12.4, pytest-7.4.4, pluggy-1.0.0 -- /opt/anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/afnanalmakhleh/CodePath/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.2.0
collected 7 items                                     

tests/test_game_logic.py::test_winning_guess PASSED [ 14%]
tests/test_game_logic.py::test_guess_too_high PASSED [ 28%]
tests/test_game_logic.py::test_guess_too_low PASSED [ 42%]
tests/test_game_logic.py::test_too_high_message_says_go_lower PASSED [ 57%]
tests/test_game_logic.py::test_too_low_message_says_go_higher PASSED [ 71%]
tests/test_game_logic.py::test_numeric_not_lexicographic_comparison PASSED [ 85%]
tests/test_game_logic.py::test_range_changes_with_difficulty PASSED [100%]

================== 7 passed in 0.01s ==================
(base) afnanalmakhleh@Afnans-Air-3 ai110-module1show-gameglitchinvestigator-starter %

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
