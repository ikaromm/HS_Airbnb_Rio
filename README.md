# HS_Airbnb_Rio

## Sumário:
- [Resumo](#resumo)
- [Descrição](#descrição)
- [Conclusão](#conclusão)
- [Próximos passos](#próximos-passos)
- [Aprendizado](#meu-aprendizado-com-o-projeto)

## Resumo 
Este projeto foi desenvolvido com base nas aulas oferecidas pela HashTag Treinamentos. Realizei alterações e o publiquei no GitHub para praticar e testar meus conhecimentos relacionados à ciência de dados. Além disso utilizei a AWS para efetuar o Deploy do projeto e testa-lo.

## Descrição

### Objetivo

Desenvolver um modelo de previsão de preços que permita a uma pessoa comum, proprietária de um imóvel, saber quanto deve cobrar pela diária do seu imóvel. Além disso, para o locatário comum, tendo em vista o imóvel que deseja alugar, este modelo ajudará a determinar se o preço do imóvel está atrativo (abaixo da média para imóveis com características semelhantes) ou não.

### O que temos disponível, inspirações e créditos

O Dataset utilizado pode ser encontrado no link: https://drive.google.com/drive/folders/1WhWbuvAyyF7XhzBpliB9lkGEn8doNCV-?usp=sharing

As bases de dados foram retiradas do site kaggle: https://www.kaggle.com/allanbruno/airbnb-rio-de-janeiro

Solução do usuário Allan Bruno do kaggle no Notebook: https://www.kaggle.com/allanbruno/helping-regular-people-price-listings-on-airbnb

- As bases de dados são os preços dos imóveis obtidos e suas respectivas características em cada mês.
- Os preços são dados em reais (R$)
- Temos bases de abril de 2018 a maio de 2020, com exceção de junho de 2018 que não possui base de dados

## Conclusão

### Coleta de Dados:
 O código inicia definindo um diretório de base (base_path) e realiza um loop sobre os arquivos dentro desse diretório. Com o objetivo de coletar dados de arquivos CSV relacionados ao Airbnb no Rio de Janeiro, organizando esses dados em um único DataFrame chamado airbnb_base. Os dados coletados incluem informações sobre acomodações, preços, avaliações e outros atributos.

### Limpeza de Dados: 
O projeto inclui etapas de limpeza de dados. Por exemplo, há um código para tratar valores nulos, onde colunas com mais de 300.000 valores nulos são removidas do DataFrame. Além disso, colunas como "price" e "extra_people" têm seus valores formatados para tipos numéricos.

### Engenharia de Recursos: 
O código realiza alguma engenharia de recursos, como a criação de colunas de variáveis ​​dummy para variáveis categóricas, como "property_type", "room_type", "bed_type" e "cancellation_policy".

### Modelagem e Avaliação: 
A parte final do código parece se concentrar na modelagem e avaliação. Duas técnicas de modelagem são mencionadas: regressão linear (model_lr) e regressão aleatória de floresta (model_rf). O desempenho desses modelos é avaliado usando métricas como R2, MSE (Erro Quadrático Médio) e RMSE (Raiz do Erro Quadrático Médio). Além disso, o código também avalia a importância das características no modelo.

Em geral, o projeto parece envolver a coleta e análise de dados relacionados a aluguéis do Airbnb no Rio de Janeiro, com o objetivo de criar modelos para prever preços.

### Remoção de colunas
Foi removida na parte de EDA algumas colunas que julguei não necessárias para a análise. Depois disso, com base no algoritmo de Random Forest, retirei as features que têm importância menor que 1%.
![](/img/importancia.png)
Podemos observar uma melhora no modelo após a retirada desta coluna. Além da melhora do modelo, temos uma melhora no tempo de execução na minha máquina, que foi de 3 minutos e 47 segundos para 2 minutos e 45 segundos.
![](/img/comparacao.png)

### Projeto em funcionamento
Aqui, podemos notar que a forma apresentada pelo Streamlit é muito amigável, proporcionando uma ótima experiência ao usuário. Utilizei valores aleatórios para esta previsão.
![](/img/serv1.png)
![](/img/serv2.png)

## Próximos passos:
Nos próximos passos do projeto, tenho a intenção de realizar as seguintes ações:

Deploy Completo na AWS: Planejo implementar um deploy completo do projeto na AWS (Amazon Web Services), tornando-o acessível a todos. Isso permitirá que outras pessoas acessem e utilizem as funcionalidades do modelo de forma conveniente.

Otimização do Modelo com Hiperparâmetros: Pretendo melhorar ainda mais o desempenho do modelo de regressão. Para isso, vou realizar uma busca de hiperparâmetros detalhada, explorando diferentes configurações para aumentar o valor do coeficiente de determinação (R2) e diminuir o erro quadrático médio (RMSE). Essa otimização visa tornar as previsões do modelo ainda mais precisas e úteis.



## Meu aprendizado com o projeto

Aqui colocarei algumas coisas que aprendi durante o projeto.

Ao trabalhar com projetos de Machine Learning (ML) e análise de dados, aprofundei meus conhecimentos no uso da biblioteca Pandas, uma ferramenta essencial para manipulação e análise de dados em Python. Em particular, explorei funcionalidades avançadas como get_dummies, técnicas de exclusão de outliers e aprimorei a visualização de dados com Matplotlib e Seaborn.


### AWS

Durante o processo de implementação de um projeto na Amazon Web Services (AWS), concentrei-me em aprofundar meu conhecimento sobre o serviço EC2 (Elastic Compute Cloud) e os grupos de segurança associados. Essa fase inicial envolveu a revisão de conceitos-chave relacionados à criação e configuração de instâncias EC2, bem como a importância dos grupos de segurança na definição de regras de acesso para proteger os recursos na nuvem.

Um aspecto prático significativo do meu trabalho foi aprender a utilizar comandos scp para transferir arquivos da minha máquina local para a instância EC2. Essa tarefa foi realizada por meio de uma conexão segura SSH, facilitando a movimentação segura de arquivos necessários para o deploy, como scripts Python e modelos de Machine Learning salvos, diretamente para o ambiente de execução na nuvem.

Para o deploy do projeto, foquei na configuração do servidor para aceitar conexões na porta TCP 8501, que é padrão para aplicações Streamlit. Adotei uma abordagem centrada na segurança, modificando as regras do grupo de segurança para permitir conexões à porta 8501 apenas do meu IP. Essa medida restritiva visou minimizar potenciais vulnerabilidades, limitando o acesso ao aplicativo apenas a usuários autorizados, neste caso, eu mesmo.

Após configurar o ambiente na AWS e ajustar as definições de segurança, procedi com o teste direto na instância EC2. Executei o aplicativo Streamlit sem problemas, indicando que todas as dependências estavam corretamente instaladas e que o ambiente estava adequadamente configurado. Esse sucesso validou não apenas a funcionalidade do aplicativo na nuvem, mas também a eficácia das medidas de segurança implementadas.

Esse processo foi uma oportunidade valiosa para reforçar minhas habilidades técnicas relacionadas à AWS, segurança de aplicações na nuvem, e deploy de projetos de software em um ambiente de produção. A capacidade de resolver desafios técnicos, como a questão do consumo de recursos e a otimização do desempenho do aplicativo, contribuiu ainda mais para o meu desenvolvimento profissional na área de desenvolvimento de software e administração de sistemas na nuvem.

### Utilizando o Streamlit: 
Aprendi a utilizar o Streamlit, uma biblioteca excepcional para a rápida criação de aplicativos web para projetos de dados e ML. Com o Streamlit, consegui desenvolver interfaces de usuário intuitivas e interativas que permitem aos usuários interagir com os modelos de ML em tempo real. A facilidade de uso do Streamlit, combinada com sua capacidade de transformar scripts Python em aplicativos compartilháveis, revelou-se uma ferramenta indispensável para a demonstração e teste de modelos de ML de forma prática e acessível.

### Perpetuação de Modelos com Joblib: 
No que diz respeito à perpetuação de modelos de ML, familiarizei-me com o joblib, uma biblioteca de serialização Python que se destaca pela sua eficiência em armazenar e recuperar objetos Python complexos, como os modelos de ML treinados. Aprendi a usar o joblib para salvar modelos de ML treinados no disco, permitindo a reutilização desses modelos sem a necessidade de re-treinamento. Isso não apenas otimizou o processo de deploy de modelos na AWS, mas também facilitou a manutenção e atualização dos modelos de ML, garantindo que as aplicações permaneçam atualizadas e eficientes.

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

### Diferença entre float64 e float32: 

1. **float32**:

Este é um tipo de dado de ponto flutuante de precisão simples.
Usa 32 bits (4 bytes) de memória.
Tem uma precisão de cerca de 7 dígitos decimais.
É menos preciso, mas consome menos memória e pode ser mais rápido em operações de ponto flutuante em hardware que não se beneficia de cálculos de precisão dupla.

2. **float64**:

Este é um tipo de dado de ponto flutuante de precisão dupla.
Usa 64 bits (8 bytes) de memória.
Tem uma precisão de cerca de 15 dígitos decimais.
É mais preciso e é o padrão em muitas operações de ponto flutuante no NumPy e outras bibliotecas científicas. No entanto, ele consome mais memória e pode ser mais lento em operações matemáticas, especialmente em grandes conjuntos de dados ou em hardware que não otimiza para precisão dupla.