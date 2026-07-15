from typing import Generator


# 1. Define the Risk Engine function that processes data on the fly
def check_risk_breach(price: float, threshold: float) -> None:
    """Processes a single price point and flags if it breaches our risk floor."""
    if price > threshold:
        print(f"   [Risk Engine] Price {price:.2f} is Safe.")
    else:
        print(
            f"   [Risk Engine] CRITICAL! Price {price:.2f} breached threshold ({threshold})!"
        )


# 2. Define the Generator (Streams data, flat memory footprint)
def stream_prices(total_steps: int) -> Generator[float, None, None]:
    """Generates simulated asset prices one at a time."""
    start_price = 100.0

    for i in range(total_steps):
        # A simple deterministic path alternating up and down
        shock = (i * 0.4) if (i % 2 == 0) else (-i * 0.5)
        simulated_price = start_price + shock

        print(f"[Generator] Yielding next price: {simulated_price:.2f}")
        yield simulated_price  # <--- PAUSES HERE. Hands execution back to the loop.
        print("[Generator] Resuming execution...")


# 3. Put it together (Execution Flow)
if __name__ == "__main__":
    risk_floor = 99.0
    steps_to_simulate = 5

    print(
        f"Starting simulation streaming. Risk Floor set to: {risk_floor}\n" + "-" * 60
    )

    # The 'for' loop requests one value at a time from stream_prices()
    for price in stream_prices(total_steps=steps_to_simulate):
        print(f" -> [Main Loop] Received price: {price:.2f}")
        check_risk_breach(price, threshold=risk_floor)
        print("-" * 60)

    print("Simulation complete. Memory remained flat throughout.")
