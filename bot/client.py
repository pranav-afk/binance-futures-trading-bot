import os
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()

def get_client():
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        raise ValueError("API key/secret not found. Check .env file")

    # Correct Futures Testnet connection
    client = Client(
        api_key,
        api_secret,
        testnet=True
    )

    # Override futures URL explicitly
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    return client
