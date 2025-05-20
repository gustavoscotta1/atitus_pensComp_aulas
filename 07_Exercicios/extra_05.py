def status_aluno(notas):
    if None in notas:
        return False  

    if len(notas) == 0:
        return False  

    if all(nota == 10 for nota in notas):
        return True  

    media = sum(notas) / len(notas)
    return media >= 7


def test():
    assert status_aluno([10, 10, 10, 10]) == True
    assert status_aluno([10, None, 10, 10]) == False  
    assert status_aluno([10, 5, None, 5]) == False
    assert status_aluno([5, 5, 5, 5]) == False
    assert status_aluno([0, 0, 0, 0]) == False
    assert status_aluno([]) == False
    assert status_aluno([7, 7, 7, 7]) == True
    assert status_aluno([6.9, 7, 7, 7]) == False