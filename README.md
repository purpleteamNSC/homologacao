# homologacao
homologacao de api

Passos para contribuir no projeto:

1 - Criar ambiente virtual:
    python -m venv venv

2 - Ativar ambiente virtual:
    source venv/bin/activate

3 - Instalar dependencias:
    pip install -r requirements.txt

Fluxo do git:

1 - Entrar na branch de desenvolvimento:
    git checkout develop

2 - Criar feature a ser trabalhada:
    git checkout -b name-feature

3 - Finalizar a feature e mandar para develop:
    git checkout develop
    git merge name-feature