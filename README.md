# Binance Futures Trading CLI Bot

A command-line trading bot built in Python to place MARKET and LIMIT orders on Binance USDT-M Futures using the Binance Futures API.  
The bot logs all order requests and responses and provides a structured CLI workflow.

---

## Features
- Place MARKET orders  
- Place LIMIT orders  
- Binance USDT-M Futures API integration  
- CLI-based order execution flow  
- Structured logging system (bot.log)  
- Environment variable support for secure API keys  
- Modular project structure (services, utils, config)

---

## Setup Instructions

1. Clone the repository  
git clone <your-repo-link>  
cd binance_futures_bot  

2. Create virtual environment  
python -m venv venv  
venv\Scripts\activate  

3. Install dependencies  
pip install -r requirements.txt  

4. Configure environment variables  

Create a `.env` file in the root directory:

BINANCE_API_KEY=your_api_key  
BINANCE_API_SECRET=your_api_secret  

---

## Run the Bot

python main.py

You will be prompted to enter:
- Symbol (e.g., BTCUSDT)  
- Side (BUY/SELL)  
- Order Type (MARKET/LIMIT)  
- Quantity  
- Price (only for LIMIT)  

---

## Sample Order Log Output

CLI started

 Order Request Summary  
Symbol: BTCUSDT  
Side: BUY  
Type: MARKET  
Quantity: 0.01  

 Raw API response: {...}  

 Order Placed Successfully  
Order ID: 12329808764  
Status: NEW  
Executed Qty: 0.000  
Avg Price: 0.00  

---

## Logs

All order activity is stored in:  
logs/bot.log  

Includes:  
- MARKET order logs  
- LIMIT order logs  
- API responses  
- Error handling logs  

---

## Security Notes
- API keys are stored in `.env`  
- `.env` is excluded via `.gitignore`  
- Do NOT commit API keys to GitHub  

