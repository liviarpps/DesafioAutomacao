# Integração Supabase + Z-API
Script em Python que lê contatos no Supabase e envia mensagem personalizada via Z-API.

Mensagem enviada: `Olá, {nome} tudo bem com você?`

## Setup da tabela
Execute no SQL Editor do Supabase:
```sql
create table contatos (
    id bigint generated always as identity primary key,
    nome text,
    telefone text
);
```

## Variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto:
```env
SUPABASE_URL=
SUPABASE_KEY=
ZAPI_INSTANCE=
ZAPI_TOKEN=
```

## Rodando Projeto
```bash
git clone https://github.com/liviarpps/DesafioAutomacao
cd DesafioAutomacao
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

## Autor
Lívia Ramires Papassoni