# Desafio de Cálculo de Taxa de Administração

Este projeto contém uma API REST desenvolvida em Python para resolver o desafio proposto de cálculo da taxa de administração para cotistas de um fundo de investimento.

## 📜 Enunciado

O objetivo é implementar uma API que recebe dados diários sobre o valor da cota de um fundo e a quantidade de cotas de cada investidor. A partir desses dados, a API calcula o valor monetário total da taxa de administração devida por cada investidor ao final do período, com base na seguinte fórmula:

$$a_j = \sum_{i=0}^{N-1} \frac{c_{i,j} v_i t}{252}$$

## 🛠️ Tecnologias Utilizadas

* **Python 3.12+**
* **FastAPI**: Para a construção da API, escolhido por sua alta performance, simplicidade e documentação automática.
* **Pydantic**: Utilizado pelo FastAPI para validação robusta e automática dos dados de entrada.
* **Uvicorn**: Como servidor ASGI para rodar a aplicação.

## 🚀 Como Rodar Localmente

Siga os passos abaixo para executar o projeto em sua máquina.

**1. Clone o repositório:**
```bash
git clone https://github.com/DaniloM05/desafio-cotas-sparta.git
cd desafio-cotas-sparta
```

**2. Crie e ative um ambiente virtual:**
```bash
# Crie o ambiente
python -m venv venv

# Ative o ambiente
# No Windows:
.\venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate
```

**3. Instale as dependências:**
```bash
python3 -m pip install -r requirements.txt
```

**4. Inicie o servidor da API:**
```bash
python3 -m uvicorn main:app --reload
```

**5. Acesse a documentação interativa:**
Abra seu navegador e acesse a seguinte URL para testar a API:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 🧠 Decisões Principais

1.  **Escolha do FastAPI**: Optei pelo FastAPI por ser um framework web Python moderno e de alta performance. Sua integração nativa com Pydantic para validação de dados e a geração automática de documentação interativa (Swagger UI) agilizam o desenvolvimento e garantem uma API robusta e fácil de usar.

2.  **Validação de Dados com Pydantic**: Em vez de validar manualmente o JSON de entrada, utilizei os modelos do Pydantic (`BaseModel`). Isso torna o código mais limpo e seguro, retornando erros claros automaticamente caso a requisição não siga o formato esperado.

3.  **Estrutura do Cálculo**: A lógica de cálculo foi implementada com uma estrutura de loops aninhados que espelha diretamente a fórmula matemática do somatório. Essa abordagem é clara, legível e garante a corretude do resultado. Uma lista de resultados é inicializada com zeros e acumulada a cada iteração, o que é uma forma eficiente de realizar a soma.
