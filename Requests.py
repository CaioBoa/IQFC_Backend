from fastapi import FastAPI, HTTPException
from datetime import date

app = FastAPI()

# Simulação de banco de dados com tickers e datas
fake_db = {
    "2024-10-01": [
        {"ticker": "AAPL", "price": 174.99},
        {"ticker": "MSFT", "price": 311.65},
        {"ticker": "GOOGL", "price": 137.88},
    ],
    "2024-10-02": [
        {"ticker": "AAPL", "price": 176.80},
        {"ticker": "MSFT", "price": 315.00},
        {"ticker": "GOOGL", "price": 138.90},
    ]
}

@app.get("/index1/{requested_date}")
def get_data_by_date(requested_date: str):
    # Verifica se a data fornecida está no formato correto e existe no "banco de dados"
    try:
        date_obj = date.fromisoformat(requested_date)
    except ValueError:
        raise HTTPException(status_code=400, detail="Data inválida. Use o formato YYYY-MM-DD.")
    
    data = fake_db.get(requested_date)
    if not data:
        raise HTTPException(status_code=404, detail="Dados não encontrados para a data fornecida.")
    
    return {"date": requested_date, "data": data}

# Inicialização da aplicação com uvicorn
# Para rodar o servidor: uvicorn main:app --reload
