# Projeto de Cálculo de Perfil de Matriz (Matrix Profile)

### **Analisando Padrões em Séries Temporais com Eficiência**

O **Perfil de Matriz** (Matrix Profile) é uma poderosa técnica utilizada para encontrar padrões e similaridades em **sequências temporais**, sendo amplamente aplicada em áreas como aprendizado de máquina, análise de dados e reconhecimento de padrões. Este projeto implementa um algoritmo eficiente para calcular o **perfil de matriz** de uma sequência de números, facilitando a detecção de similaridades e anomalias em séries temporais.

---

## 🚀 Funcionalidades

### **1. Cálculo de Distância Euclidiana**
A função `calculoDistancia(seq1, seq2)` calcula a distância euclidiana entre duas subsequências de uma sequência maior. Essa métrica é fundamental para entender o quão semelhantes ou distantes essas subsequências são, permitindo identificar padrões recorrentes.

### **2. Geração do Perfil de Matriz**
A função `matrix_profile(lista, tamanho)` gera o perfil de matriz para uma sequência de números. O perfil de matriz é uma lista onde cada valor representa a **menor distância** entre uma subsequência e todas as outras subsequências da sequência original. Ele ajuda a identificar os **vizinhos mais próximos** e padrões ocultos na sequência.

---

## 💻 Exemplo de Entrada e Saída

### **Entrada**
Dada uma lista de números e o tamanho de subsequências para análise:

```python
lista = [0, 1, 3, 2, 9, 1, 14, 15, 1, 2, 2, 10, 7]
tamanho = 4
```

### **Saída**
O algoritmo retornará uma lista com as distâncias euclidianas mínimas entre subsequências:

```python
Vizinhos mais Proximos: [6.0, 2.0, 3.0, 3.0, 8.0, 7.0, 11.0, 8.0, 5.0, 6.0]
```
# 📊 Como Funciona?
Passo 1: Inicialização do Perfil de Matriz
A função matrix_profile() cria inicialmente um vetor de distâncias, chamado matrix_prof, preenchido com valores infinitos. Esse vetor será atualizado com as menores distâncias entre subsequências durante a execução.

Passo 2: Comparação das Subsequências
Para cada subsequência da sequência original, calculamos a distância euclidiana em relação a todas as outras subsequências e mantemos a menor distância para cada uma delas.

Passo 3: Identificação dos Padrões
Após calcular todas as distâncias, o vetor final matrix_prof nos dá o perfil da sequência, revelando padrões de repetição e anomalias que podem ser explorados em diversas áreas como previsão de séries temporais, análise de padrões e até detecção de falhas.

# 💡 Exemplo Prático
### **Código** 
Você pode testar o algoritmo com o seguinte código:

```python
lista = [0, 1, 3, 2, 9, 1, 14, 15, 1, 2, 2, 10, 7]
tamanho = 4
vizinhos = matrix_profile(lista, tamanho)
print("Vizinhos mais Proximos:", vizinhos)
```

### **Saída Esperada**

```python
Vizinhos mais Proximos: [6.0, 2.0, 3.0, 3.0, 8.0, 7.0, 11.0, 8.0, 5.0, 6.0]
```

# 🛠️ Requisitos
Python 3.x ou superior
Bibliotecas Padrão (sem dependências externas)
Este projeto foi construído com base na biblioteca padrão do Python, o que facilita sua integração em diferentes sistemas e sua utilização em diversos cenários de análise de dados.

# 🔍 Como esse Algoritmo Pode Ser Útil?
Este algoritmo tem uma ampla gama de aplicações práticas, incluindo:

Análise de Séries Temporais: Encontrar padrões em dados temporais de sensores, financeiros ou médicos.
Detecção de Anomalias: Identificar desvios inesperados em séries de dados.
Reconhecimento de Padrões: Detectar padrões repetitivos em sequências de dados.
Previsão de Tendências: Auxiliar na previsão de comportamento futuro de séries temporais.

# 📜 Licença
Este projeto está licenciado sob a MIT License. Sinta-se à vontade para contribuir, modificar e usar o código conforme sua necessidade.
