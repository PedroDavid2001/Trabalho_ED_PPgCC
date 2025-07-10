# Simulador de Reality Show

Um projeto final para a disciplina de Estrutura de Dados da Pós-Graduação em Ciência da Computação (PPGCC) da UFERSA/UERN.

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

Certifique-se de ter o **Python 3** instalado em sua máquina.

### Instalação

1.  **Clone este repositório**:

    ```bash
    git clone https://github.com/PedroDavid2001/Trabalho_ED_PPgCC.git
    cd Trabalho_ED_PPgCC
    ```

2.  **Nenhuma biblioteca externa adicional** é necessária além das que já vêm com a instalação padrão do Python (Tkinter, `random`, `math`).

### Execução

1.  Navegue até o diretório do projeto no seu terminal.
2.  Execute o arquivo principal:
    ```bash
    python main_app.py
    ```

-----

## 📂 Estrutura do Projeto

  * `main_app.py`: O arquivo principal da aplicação, contendo a interface gráfica e a lógica de simulação diária.
  * `participante.py`: Define a classe `Participante`, responsável por gerenciar os atributos de cada indivíduo (nome, características, aptidão, raciocínio, humor, gostos e desgostos). Inclui métodos estáticos e de classe para a geração e definição de atributos.
  * `evento.py`: Contém a classe `Evento`, que encapsula a lógica para diferentes tipos de acontecimentos na casa, como provas de eliminação (físicas e lógicas), interações sociais e o paredão.
  * `relacoes.py`: Define a classe `MatrizRelacoes` para calcular e gerenciar o nível de relacionamento entre os participantes.
  * `caracteristica.py`: Enumera as possíveis características dos participantes e define as relações de semelhança entre elas.
  * `humor.py`: Define uma classe simples com constantes para os diferentes estados de humor dos participantes.

-----

## 🧠 Conceitos de Estrutura de Dados Aplicados

Este projeto utiliza e demonstra conceitos importantes de Estruturas de Dados e Algoritmos:

  * **Grafos**: A relação entre as **características** (`caracteristica.py`) é modelada como um grafo (através de uma matriz de adjacência `semelhantes`), permitindo a geração de características coerentes para os participantes.
  * **Matrizes**: A **matriz de relações** (`relacoes.py`) é fundamental para calcular a afinidade entre os participantes, que é crucial para o sistema de votação do paredão.
  * **Listas e Dicionários**: Usados extensivamente para armazenar e manipular participantes, suas características, gostos, desgostos e votos de forma eficiente.
  * **Algoritmos de Busca/Seleção**: Em eventos de eliminação, algoritmos simples são usados para encontrar o participante com o menor atributo (aptidão ou raciocínio). No paredão, a busca pelo participante mais votado e a resolução de empates envolvem lógica de seleção.
  * **Modularização e Encapsulamento**: O projeto é dividido em módulos (arquivos Python) e classes, organizando a lógica em componentes reutilizáveis e fáceis de manter — um princípio fundamental da engenharia de software baseada em estruturas de dados bem definidas.

-----

## 👨‍💻 Desenvolvedores

  * Pedro David Rocha Saldanha
  * Pedro Vinícius Medeiros Crescencio

-----
