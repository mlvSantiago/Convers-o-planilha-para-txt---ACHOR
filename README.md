# 🧩 Gerador de Configurações PJSIP a partir de Planilha Excel

Este script em **Python** lê uma planilha Excel contendo informações de ramais e gera automaticamente um arquivo de configuração **`pjsip_additional.txt`** para sistemas **Asterisk**.

---

## 📘 Descrição

O script automatiza a criação de blocos de configuração **PJSIP** a partir de dados estruturados em uma planilha `.xlsx`.

Cada linha da planilha representa um ramal e seus respectivos parâmetros, que são convertidos em blocos de configuração formatados conforme o padrão do **Asterisk**.

---

## ⚙️ Funcionamento

1. O programa recebe o nome (sem extensão) de uma planilha `.xlsx` como argumento.
2. Lê o conteúdo da planilha usando a biblioteca **pandas**.
3. Para cada linha, extrai as colunas:
   - `username`
   - `call group`
   - `pick group`
   - `display`
   - `password`
   - `contexto`
4. Gera um bloco de configuração PJSIP e o escreve no arquivo **`pjsip_additional.txt`**.

---

## 🚀 Como Executar

No terminal (ou prompt de comando):

```bash
python3 gerar_pjsip.py ramais

Onde "ramais" é o nome da planilha, sem extensão, contendo os ramais a serem cadastrados 


---

##🧰 Requisitos

Antes de executar , instale as dependencias se nescessarias

```bash
pip install pandas openpyxl


