# HS_Airbnb_Rio

## Resumo 

Este é um projeto feito com base nas aulas dadas na HashTag Treinamentos, efetuei mudanças e subi para o GitHub para treinar e testar meus conhecimentos a cerca de conteúdos voltados a ciências de dados.

## Descrição

### Objetivo

Construir um modelo de previsão de preço que permita uma pessoa comum que possui um imóvel possa saber quanto deve cobrar pela diária do seu imóvel.

Ou ainda, para o locador comum, dado o imóvel que ele está buscando, ajudar a saber se aquele imóvel está com preço atrativo (abaixo da média para imóveis com as mesmas características) ou não.

### O que temos disponível, inspirações e créditos

As bases de dados foram retiradas do site kaggle: https://www.kaggle.com/allanbruno/airbnb-rio-de-janeiro

Solução do usuário Allan Bruno do kaggle no Notebook: https://www.kaggle.com/allanbruno/helping-regular-people-price-listings-on-airbnb

- As bases de dados são os preços dos imóveis obtidos e suas respectivas características em cada mês.
- Os preços são dados em reais (R$)
- Temos bases de abril de 2018 a maio de 2020, com exceção de junho de 2018 que não possui base de dados

## Meu aprendizado com o projeto

Aqui colocarei algumas coisas que aprendi durante o projeto.

### Upload Arquivos 100mb +

Para fazer este tipo de upload precisei utilizar da ferramenta de LFS do git. Para mais informações entre no site [Git LFS](https://github.com/git-lfs/git-lfs?tab=readme-ov-file).

Caso utilize linux segue o comando para baixar diretamente.

```
sudo apt-get install git-lfs
```

Depois disso adicionei os arquivos .csv no track do LFS:

```
git lfs track "*.csv"
```

Agora toda vez que um arquivo .csv for comitado ele ira sem problemas. Basta seguir com o git add e commit.

### GitHub
Eu já utilizava diariamente o GitHub, porém, não sabia que existia um limite de 1GB para o projeto no plano gratuito. Testei fazer o upload no GitLab e deu certo. Como desejo postar no GitHub este projeto utilizei um gitignore para que os arquivos .csv não fossem para o repositório.