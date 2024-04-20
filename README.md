# 🚀 TimeWise

Em um mundo cada vez mais acelerado, onde as demandas pessoais e profissionais competem pela nossa atenção a todo momento, a habilidade de gerenciar eficazmente o nosso tempo torna-se crucial.

Quantas vezes nos vemos perdidos em uma pilha de tarefas, sem saber por onde começar ou como priorizá-las? Ou então, dedicamos horas a uma atividade apenas para perceber que poderíamos ter sido mais eficientes?

É aqui que entra a necessidade de uma ferramenta de gerenciamento de tempo como a nossa aplicação. Com ela, você pode registrar todas as suas atividades diárias, desde o tempo dedicado ao trabalho até o lazer, e analisar como está distribuindo seu tempo ao longo do dia.

Além disso, ao classificar suas tarefas por categoria, como estudo, trabalho ou lazer, você terá uma visão clara de onde está concentrando sua energia e onde pode ser necessário fazer ajustes.

Com dados concretos e relatórios detalhados à sua disposição, você poderá identificar padrões, eliminar desperdícios de tempo e adotar hábitos mais produtivos.

Portanto, se você deseja conquistar uma rotina mais equilibrada, produtiva e satisfatória, nossa aplicação de gerenciamento de tempo é a ferramenta que você precisa. Não deixe o tempo passar, comece hoje mesmo a tomar o controle da sua vida.

## Descrição

Este é um projeto de backend desenvolvido em Flask para a PUC. Ele fornece uma API para gerenciar tarefas.

## Instalação

Para instalar e executar este projeto, você precisará ter Python e pip instalados em seu ambiente. Siga estas etapas:

1. Clone o repositório:

```bash
git clone https://github.com/saulodiasnt/backend-mvp-sprint1.git
```

2. Navegue até o diretório do projeto:

```bash
cd backend-mvp-sprint1
```

3. Crie um ambiente virtual:

```bash
python -m venv venv
```

4. Ative o ambiente virtual:

No Windows:

```bash
.\venv\Scripts\activate
```

No Linux/Mac:

```bash
source venv/bin/activate
```

5. Instale as dependências:

```bash
pip install -r requirements.txt
```

6. Execute as migrations:

```bash
flask db migrate
flask db upgate
```

## Uso

Para iniciar o servidor, execute o seguinte comando:

```bash
flask run
```

Agora você pode acessar a API em `http://localhost:5000`.

Para acessar a documentação da api acesse a url `http://localhost:5000/openapi`

## Contribuição

Contribuições são bem-vindas! Por favor, leia as diretrizes de contribuição antes de enviar uma pull request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
