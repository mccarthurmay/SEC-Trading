from alpaca_trade_api.rest import REST, TimeFrame
import os
import time as tm

try:
    api = REST(
    key_id=os.getenv("APCA_API_KEY_ID"),
    secret_key=os.getenv("APCA_API_SECRET_KEY"),
    base_url="https://paper-api.alpaca.markets"
    )
    account = api.get_account()
except:
    print("API Environment not set up. Please refer to 'config.py' or 'README'.")


def buy(ticker):
    try:
        buy_order = api.submit-order(
            symbol = ticker,
            qty = quantity,
            side = 'buy',
            type = 'market',     
            time_in_force = 'gtc'
        )

    except Exception as e:
        print(e, "Buy order not submitted")
    
    order_filled = False
    print(f"Waiting for {ticker} to be filled.")
    while not order_filled:
        order = api.get_order(buy_order.id)
        stop_order = api.get_order(stop_order.id)
        if order.status == 'filled':
            order_filled = True
            fill_price = order.filled_avg_price
            print(f"{ticker} has filled.")
        else:
            tm.sleep(2)
    if order_filled:
        pass

def monitor_position(ticker):
    trailing_percent = 0.0005
    highest_price = 0
    trailing_stop_active =  False

    while True:

        position = api.get_position(ticker)

        quantity = float(position.qty)
        current_price = float(position.current_price)
        buy_price = float(position.avg_entry_price)

        if current_price > buy_price:
            trailing_stop_active = True
            highest_price = current_price
        else:
            print("Waiting for trail to end.")
            tm.sleep(30)
            continue
        highest_price = max(highest_price, current_price)

        stop_price = highest_price * (1 - trailing_percent)

        if current_price <= stop_price:
            close_all_orders(ticker)
            order = api.submit_order(
                symbol = ticker,
                qty = quantity,
                side = 'sell',
                type = 'market',
                time_in_force = 'gtc',
            )
            print(f"{ticker} sold. Order ID: {order.id}")
            break

def close_all_orders(ticker):
    orders = api.list_orders(status='open', symbols = [ticker])
    for order in orders:
        try:
            api.cancel_order(order.id)
            
        except Exception as e:
            print(f"Error cancelling order for {ticker}")


if __name__ == "__main__":
    open_positions, num_positions = get_open_positions()
    max_positions = 5
    with concurrent.futures.ThreadPoolExecutor() as executor:

        while True:
            open_positions, num_positions = get_open_positions()
            futures = {}
            futures_positions = {}
            print(f"Outer loop, num = {num_position}")

            while num_position >= max_positions:
                for ticker in open_positions:
                    if ticker not in future_positions:
                        futures_p = executor.submit(monitor_position, ticker)
                        futres_positions[ticker] = futures_p
                open_positions, num_position = get_open_positions()
                print(f"Waiting for sell")
                tm.sleep(30)
