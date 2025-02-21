
# Homologação

Uma breve descrição sobre o que esse projeto faz e para quem ele é


## Criar ambiente virtual

Criar ambiente virtual

```bash
  python -m venv venv
```

Ativar ambiente virtual em Linux

```bash
  source venv/bin/activate
```

Ativar ambiente virtual em Windows

```bash
   venv/Scripts/activate
```

Instalar dependencias

```bash
    pip install -r requirements.txt
```

## Fluxo do Git

Entrar na branch de desenvolvimento:

```bash
  git checkout develop
```

Criar feature a ser trabalhada:

```bash
  git checkout -b name-feature
```

Finalizar a feature:

```bash
   git add
   git commit -m "descricao da feature"
```
Mandar para develop:

```bash
   git checkout develop
   git merge name-feature
   git push
   git branch -D name-feature
```