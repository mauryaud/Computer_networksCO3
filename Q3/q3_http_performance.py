"""HTTP performance calculation for Q3."""

RTT = 0.050       # 50 ms
OBJECTS = 80


def non_persistent_one_connection():
    # 1 RTT for HTML + 1 RTT for each object
    return (1 + OBJECTS) * RTT


def persistent_http11():
    # 1 RTT for HTML + 1 RTT for each object
    return (1 + OBJECTS) * RTT


def persistent_pipelining():
    # 1 RTT for HTML + 1 RTT for all pipelined objects
    return 2 * RTT


def six_parallel_connections():
    # HTML takes 1 RTT.
    # 80 objects / 6 connections = 14 rounds
    rounds = (OBJECTS + 5) // 6

    return (1 + rounds) * RTT


def bundled_objects():
    # Alternative concept: combine 80 objects into 8 bundles
    bundles = 8

    non_persistent = (1 + bundles) * RTT
    persistent = (1 + bundles) * RTT

    return non_persistent, persistent


print("HTTP PERFORMANCE ANALYSIS")
print("-" * 35)

print(
    f"Non-persistent HTTP: "
    f"{non_persistent_one_connection():.3f} seconds"
)

print(
    f"Persistent HTTP/1.1: "
    f"{persistent_http11():.3f} seconds"
)

print(
    f"Persistent HTTP/1.1 with pipelining: "
    f"{persistent_pipelining():.3f} seconds"
)

print(
    f"6 parallel non-persistent connections: "
    f"{six_parallel_connections():.3f} seconds"
)

non_persistent, persistent = bundled_objects()

print()
print("8-BUNDLE ALTERNATIVE")
print(
    f"Non-persistent HTTP with 8 bundles: "
    f"{non_persistent:.3f} seconds"
)

print(
    f"Persistent HTTP/1.1 with 8 bundles: "
    f"{persistent:.3f} seconds"
)

print()
print("HTTP/2 and HTTP/3 comparison:")
print("HTTP/2 uses one multiplexed connection.")
print("HTTP/3 uses QUIC and avoids TCP head-of-line blocking.")