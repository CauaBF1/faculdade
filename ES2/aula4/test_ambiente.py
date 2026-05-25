from ambiente import ambiente_suportado


# Testes da versão do Python
def test_python_39_invalido():
    # validar o limite inferior aceito do Python.
    assert ambiente_suportado(3.9, "linux", 7.0) is False


def test_python_312_valido_linux():
    # como caso comum dentro da faixa suportada.
    assert ambiente_suportado(3.12, "linux", 7.0) is True


def test_python_313_valido_linux():
    # versão mais alta de Python permitida.
    assert ambiente_suportado(3.13, "linux", 8.2) is True


def test_python_314_invalido():
    # validar o limite superior aceito do Python.
    assert ambiente_suportado(3.14, "linux", 8.2) is False


# Testes da versão do pytest
def test_pytest_69_invalido():
    # validar o limite inferior aceito do pytest.
    assert ambiente_suportado(3.12, "linux", 6.9) is False


def test_pytest_70_valido():
    # garantir que o limite mínimo do pytest seja aceito.
    assert ambiente_suportado(3.12, "linux", 7.0) is True


def test_pytest_81_valido_com_python_312():
    # separar a regra geral do pytest da regra especial do Python 3.13.
    assert ambiente_suportado(3.12, "linux", 8.1) is True


def test_pytest_81_invalido_com_python_313():
    # validar a exigência extra aplicada ao Python 3.13.
    assert ambiente_suportado(3.13, "linux", 8.1) is False


def test_pytest_82_valido_com_python_313():
    # garantir que o requisito mínimo do Python 3.13 seja aceito.
    assert ambiente_suportado(3.13, "linux", 8.2) is True


# Testes do sistema linux


def test_sist_op_linux_valido_python_310():
    # validar Linux no menor Python aceito
    assert ambiente_suportado(3.10, "linux", 7.0) is True


def test_sist_op_linux_valido_python_313():
    # Linux com o maior Python aceito.
    assert ambiente_suportado(3.13, "linux", 8.2) is True


def test_sist_op_linux_invalido_python_39():
    # confirmar que o sistema não ignora a regra do Python.
    assert ambiente_suportado(3.9, "linux", 7.0) is False


def test_sist_op_linux_invalido_pytest_69():
    # confirmar que o sistema não ignora a regra do pytest.
    assert ambiente_suportado(3.12, "linux", 6.9) is False


# Testes do sistema macos


def test_sist_op_macos_valido_python_310():
    # validar macos no menor Python aceito
    assert ambiente_suportado(3.10, "macos", 7.0) is True


def test_sist_op_macos_valido_python_313():
    # combinar macos com o maior Python aceito.
    assert ambiente_suportado(3.13, "macos", 8.2) is True


def test_sist_op_macos_invalido_pytest_81_com_python_313():
    # garantir que macos também respeite a regra do Python 3.13.
    assert ambiente_suportado(3.13, "macos", 8.1) is False


def test_sist_op_macos_invalido_python_314():
    # confirmar o limite superior de Python no macos.
    assert ambiente_suportado(3.14, "macos", 8.2) is False


# Testes do sistema windows


def test_sist_op_windows_invalido_python_310():
    # validar a restrição específica do Windows.
    assert ambiente_suportado(3.10, "windows", 7.0) is False


def test_sist_op_windows_valido_python_311():
    # garantir que o mínimo do Windows seja aceito.
    assert ambiente_suportado(3.11, "windows", 7.0) is True


def test_sist_op_windows_valido_python_313():
    # cobrir Windows com a versão mais alta de Python.
    assert ambiente_suportado(3.13, "windows", 8.2) is True


def test_sist_op_windows_invalido_python_313_pytest_81():
    # verificar a regra do Python 3.13 também no Windows.
    assert ambiente_suportado(3.13, "windows", 8.1) is False


def test_sist_op_windows_invalido_python_314():
    # confirmar o limite superior de Python no Windows.
    assert ambiente_suportado(3.14, "windows", 8.2) is False


# Testes de sistemas inválidos


def test_sist_op_android_invalido():
    # validar a rejeição de sistemas fora da lista permitida.
    assert ambiente_suportado(3.12, "android", 7.0) is False
