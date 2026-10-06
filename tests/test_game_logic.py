from logic_utils import check_guess, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_too_high_message_says_go_lower():
    # A guess above the secret should tell the player to go lower
    _, message = check_guess(60, 50)
    assert "LOWER" in message

def test_too_low_message_says_go_higher():
    # A guess below the secret should tell the player to go higher
    _, message = check_guess(40, 50)
    assert "HIGHER" in message

def test_numeric_not_lexicographic_comparison():
    # 9 < 50 numerically, even though "9" > "50" as strings
    outcome, _ = check_guess(9, 50)
    assert outcome == "Too Low"

def test_range_changes_with_difficulty():
    # Each difficulty should return its own range
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)
