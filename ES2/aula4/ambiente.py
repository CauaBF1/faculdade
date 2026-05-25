def ambiente_suportado(versao_python, sistema, versao_pytest):
    if versao_python < 3.10 or versao_python > 3.13:
        return False

    if sistema not in ["linux", "macos", "windows"]:
        return False

    if versao_pytest < 7.0:
        return False

    if versao_python == 3.13 and versao_pytest < 8.2:
        return False

    if sistema == "windows" and versao_python < 3.11:
        return False

    return True
