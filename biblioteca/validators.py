from datetime import date

from django.core.exceptions import ValidationError

def validar_ano_publicacao(ano):
    ano_atual = date.today().year
    if ano < 1450 or ano > ano_atual:
        raise ValidationError(
            f"O ano precisa estar entre 1450 e {ano_atual}. Confira o ano de publicação do livro.",
            code="ano_invalido",
        )

