import autenticar_usuario_solved

def test_valid_user_valid_password():
    assert autenticar_usuario_solved.authenticateUser("Lara", "b2l9d544") == True
    assert autenticar_usuario_solved.authenticateUser("Alejandro", "6589ab27") == True
    assert autenticar_usuario_solved.authenticateUser("Alba", "2@#%ppLO") == True

def test_valid_user_invalid_password():
    assert autenticar_usuario_solved.authenticateUser("Lara", "notLara'sPassword") == False
    assert autenticar_usuario_solved.authenticateUser("Lara", "6589ab27") == False
    assert autenticar_usuario_solved.authenticateUser("Alejandro", "") == False

def test_invalid_user():
    assert autenticar_usuario_solved.authenticateUser("notAuthUser", "doesn't matter") == False
    assert autenticar_usuario_solved.authenticateUser("", "doesn't matter") == False
    assert autenticar_usuario_solved.authenticateUser("\n", "doesn't matter") == False