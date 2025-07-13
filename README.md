# Simulador de Reality Show

Um projeto final para a disciplina de Estruturas de Dados da Pós-Graduação em Ciência da Computação (PPGCC) da UFERSA/UERN.

Este projeto é um simulador interativo de reality show construído com **Python** e **Tkinter**. Ele permite que você configure e observe a dinâmica de participantes em uma casa, onde eventos diários, interações sociais e eliminações ocorrem, influenciando o humor e o número de participantes.

-----

## 🚀 Funcionalidades

* **Geração de Participantes Dinâmica**: Insira nomes para criar participantes com características, aptidões (física e raciocínio lógico) e humores iniciais gerados aleatoriamente, além de gostos e desgostos que influenciam suas relações.
* **Simulação por Dias**: Avance dia a dia na simulação, observando os eventos que afetam os participantes.
* **Eventos Variados**:
    * **Provas de Aptidão Física**: Eliminam o participante com menor aptidão.
    * **Provas de Raciocínio Lógico**: Eliminam o participante com menor raciocínio.
    * **Interações Sociais**: Alteram o humor dos participantes com base em suas características e relações.
    * **Paredão**: Participantes votam para eliminar quem tem a pior relação.
* **Log de Eventos Detalhado**: Acompanhe o que acontece na casa através de um log de texto que registra as ações, mudanças de humor e eliminações.
* **Atualização em Tempo Real**: Visualize a lista de participantes restantes e seu status (aptidão, raciocínio e humor) sendo atualizada a cada dia.
* **Interface Gráfica Intuitiva**: Desenvolvido com Tkinter para uma experiência de usuário simples e funcional.

-----

## 🛠️ Como Rodar o Projeto

### Pré-requisitos

Certifique-se de ter o **Python 3** (versão 3.11.6) instalado em sua máquina.

### Instalação

1.  **Clone este repositório**:
    ```bash
    git clone https://github.com/PedroDavid2001/Trabalho_ED_PPgCC.git
    cd Trabalho_ED_PPgCC
    ```
2.  **Nenhuma biblioteca externa adicional** é necessária além das que já vêm com a instalação padrão do Python (Tkinter).

### Execução

1.  Navegue até o diretório do projeto no seu terminal.
2.  Execute o arquivo principal:
    ```bash
    python main_app.py
    ```

-----

## 📂 Estrutura do Projeto

* `main_app.py`: Controla a interface gráfica, a inicialização da simulação e a orquestração dos eventos diários.
* `participante.py`: Define a classe `Participante`, seus atributos (nome, características, aptidões, humor, gostos, desgostos) e métodos para geração e manipulação.
* `evento.py`: Contém a classe `Evento`, que gerencia os diferentes tipos de eventos (provas, interações, paredão) e a lógica de como afetam os participantes.
* `relacoes.py`: Implementa a classe `MatrizRelacoes` para calcular e armazenar os níveis de relacionamento entre os participantes.
* `caracteristica.py`: Define as características dos participantes e as relações de similaridade entre elas.
* `humor.py`: Define constantes para os estados de humor dos participantes.

-----

## 🧠 Conceitos de Estrutura de Dados Aplicados

Este projeto utiliza e demonstra conceitos importantes de Estruturas de Dados e Algoritmos:

* **Grafos (Matriz de Adjacência)**: A relação de semelhança entre as características dos participantes é modelada como um grafo, implementado através de uma matriz de adjacência. Isso permite indicar similaridade entre traços de forma bidirecional.
* **Matrizes (Dicionário de Dicionários)**: As relações entre os participantes são armazenadas em uma matriz implementada como um dicionário de dicionários em Python. As chaves são os nomes dos participantes para facilitar o acesso e manipulação. Essa matriz é fundamental para calcular a afinidade e desafinidade entre eles, crucial para o sistema de votação do paredão.
* **Listas Enumeradas**: Utilizadas para simular e representar as características que moldam a personalidade de uma pessoa, como "Inteligente", "Proativo", "Amigável", entre outras.
* **Listas e Dicionários**: Usados extensivamente para armazenar e manipular participantes, suas propriedades (aptidões, humor, gostos, desgostos) e o registro dos eventos diários de forma eficiente.
* **Algoritmos de Busca/Seleção**: Em eventos de eliminação, algoritmos simples são usados para encontrar o participante com o menor atributo (aptidão ou raciocínio). No paredão, a busca pelo participante mais votado e a resolução de empates envolvem lógica de seleção.
* **Modularização e Encapsulamento**: O projeto é dividido em módulos e classes, organizando a lógica em componentes reutilizáveis e fáceis de manter, um princípio fundamental da engenharia de software baseada em estruturas de dados bem definidas.

---

## ⚠️ Limitações e Dificuldades Enfrentadas

Durante o desenvolvimento, algumas limitações e dificuldades foram observadas:

* **Complexidade do Comportamento Humano**: A modelagem do humor e das interações sociais é uma simplificação, visto que comportamentos humanos reais são muito mais complexos e imprevisíveis do que o modelo atual permite.
* **Aleatoriedade e Controlabilidade**: A grande aleatoriedade na geração de características e eventos pode, por vezes, levar a simulações menos "realistas" ou com resultados muito variados, dificultando a análise de padrões específicos.
* **Interface Gráfica (Tkinter)**: Embora funcional, o Tkinter possui limitações estéticas e de personalização comparado a frameworks GUI mais modernos, o que pode impactar a experiência visual.
* **Escalabilidade**: Para um número muito grande de participantes, a complexidade computacional do cálculo da matriz de relações poderia se tornar um gargalo, exigindo otimizações mais avançadas.
* **Refatoração e Manutenção**: A transição de funções para métodos de classe e métodos estáticos exigiu uma refatoração significativa, que, embora benéfica para a organização, representou um desafio inicial na adaptação do código existente.

-----

## 👨‍💻 Desenvolvedores

  * Pedro David Rocha Saldanha
  * Pedro Vinícius Medeiros Crescencio

-----
