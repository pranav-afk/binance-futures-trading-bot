import argparse
from bot.client import get_client
from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)
from bot.logging_config import setup_logger

def main():
    print(" CLI started")

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    logger = setup_logger()

    try:
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price, order_type)

        client = get_client()

        print("\n Order Request Summary")
        print(f"Symbol: {args.symbol.upper()}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")
        if order_type == "LIMIT":
            print(f"Price: {price}")

        result = place_order(
            client, logger, args.symbol, side, order_type, quantity, price
        )

        print("\n Order Placed Successfully")
        print(f"Order ID: {result['orderId']}")
        print(f"Status: {result['status']}")
        print(f"Executed Qty: {result['executedQty']}")
        print(f"Avg Price: {result['avgPrice']}")

    except Exception as e:
        logger.error(f"CLI error: {str(e)}")
        print(f"\n Order Failed: {str(e)}")

if __name__ == "__main__":
    main()
