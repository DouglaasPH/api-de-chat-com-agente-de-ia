# 📡 API de Chat com Agente de IA (FastAPI + Strands Agents + Ollama)

Este projeto implementa uma API de chat integrada a um Agente de IA capaz de responder perguntas gerais e executar cálculos usando uma _Math Tool_.
A aplicação utiliza **FastAPI**, **Strands Agents SDK** e o modelo **llama3.1** rodando localmente via **Ollama**.

---

## 📁 Código-Fonte

O repositório contém:

```
api/
    routes/
        math.py              → Endpoint "/chat" da API para operações matemáticas
    schemas/
        math_message.py      → Modelos Pydantic para validar request
application/
    agent_service.py         → Lógica do agente de IA (gerencia criação do agente, configuração do modelo e execução das mensagens)
    math_tool.py             → Ferramenta usada pelo agente para cálculos
domain/
    math_service.py          → Regras de negócio das operações matemáticas
infrastructure/
    llm_ollama.py            → Integração com o provedor Ollama (cria e configura o modelo de IA usando variáveis do .env)
    settings.py              → Carrega e gerencia variáveis de ambiente usando Pydantic Settings
.env.example                 → Exemplo das variáveis de ambiente necessárias
.gitignore                   → Arquivos e pastas ignorados pelo Git
main.py                      → Entrada principal da API (FastAPI)
pyproject.toml               → Configuração do Poetry e dependências
poetry.lock                  → Versões exatas das dependências instaladas
README.md                    → Instruções para instalar, rodar e usar o projeto

```

---

# 🚀 Instalação e Execução

## 1. 🔧 Pré-requisitos

- **Python ≥ 3.14**
- Ollama instalado
- Modelo local **llama3.1**

### Instalar Ollama

Baixe em: [https://ollama.com/download](https://ollama.com/download)

Inicie o servidor:

```sh
ollama serve
```

Baixe o modelo exigido:

```sh
ollama pull llama3.1
```

---

## 2. 📦 Instalar dependências

### Usando Poetry

```sh
poetry install
```

---

## 3. 🔐 Configurar variáveis de ambiente

O projeto inclui um arquivo **`.env.example`** com as configurações iniciais necessárias.
Basta copiá-lo e renomear para **`.env`**:

```sh
cp .env.example .env
```

---

## 4. ▶️ Executar o servidor FastAPI

### Com uvicorn:

```sh
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Com Poetry:

```sh
poetry run uvicorn main:app --host 0.0.0.0 --port 8000
```

Acesse a API:

```
http://localhost:8000
```

Swagger UI:

```
http://localhost:8000/docs
```

---

# 💬 Endpoint de Chat

### POST `/chat`

📤 Exemplo de requisição:

```json
{
  "message": "Quanto é 12 * 19?"
}
```

📥 Exemplo de resposta:

```json
{
  "response": "A resposta para a pergunta é: 228."
}
```

---

# 🧠 Funcionamento do Agente de IA

- Perguntas gerais → respondidas pelo modelo **llama3.1**
- Perguntas matemáticas → encaminhadas automaticamente para a _Math Tool_
- A tool resolve:

  - Soma
  - Subtração
  - Multiplicação
  - Divisão
  - Raiz quadrada
  - Potenciação

---

# 📄 .gitignore

Inclui:

```
.env
*.pyc
**/__pycache__/
.venv/
.cache/
```

---

# ✅ Requisitos do Case Atendidos

✔ Python ≥ 3.14  
✔ API FastAPI com POST `/chat`  
✔ Modelos e agentes configurados via `.env`  
✔ Strands Agents SDK integrado  
✔ Ferramenta matemática funcionando  
✔ Execução local com Ollama + llama3.1  
✔ Código limpo e organizado
