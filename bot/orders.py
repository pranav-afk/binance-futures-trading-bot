from binance.exceptions import BinanceAPIException, BinanceRequestException

def place_order(client, logger, symbol, side, order_type, quantity, price=None):
    try:
        logger.info(
            f"Placing {order_type} order: {side} {quantity} {symbol} price={price}"
        )

        params = {
            "symbol": symbol.upper(),
            "side": side,
            "type": order_type,
            "quantity": quantity,
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        # 🔹 Place Futures order
        response = client.futures_create_order(**params)

        # 🔹 Print and log raw response
        print("\n🔎 Raw API response:", response)
        logger.info(f"Raw order response: {response}")

        # 🔹 Validate response
        if "orderId" not in response:
            raise Exception(f"Invalid API response: {response}")

        order_id = response.get("orderId")
        status = response.get("status")
        executed_qty = response.get("executedQty")

        # avgPrice may be "0.0" initially for MARKET orders
        avg_price = response.get("avgPrice")
        if not avg_price or avg_price == "0.0":
            avg_price = "N/A"

        return {
            "orderId": order_id,
            "status": status,
            "executedQty": executed_qty,
            "avgPrice": avg_price,
        }

    except BinanceAPIException as e:
        logger.error(f"Binance API error: {e.message}")
        raise Exception(f"Binance API error: {e.message}")

    except BinanceRequestException as e:
        logger.error(f"Network error: {str(e)}")
        raise Exception("Network error while placing order")

    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise
