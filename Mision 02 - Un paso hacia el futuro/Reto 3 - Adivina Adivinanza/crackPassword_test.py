import crackPassword_solved as solution


def test_challenge():
    stolenPassword_hashed = "d77bd8482003072cc056575c0478476a3af1993c"
    assert solution.find_password(stolenPassword_hashed) == "Chemita12"