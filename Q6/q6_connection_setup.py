"""Q6 - Connection setup time comparison.

RTT = 100 ms
"""

RTT = 0.100


def tcp_tls12():
    # TCP handshake = 1 RTT
    # TLS 1.2 handshake = 2 RTT
    return 3 * RTT


def tcp_tls13():
    # TCP handshake = 1 RTT
    # TLS 1.3 handshake = 1 RTT
    return 2 * RTT


def quic_first_visit():
    # QUIC combines transport and TLS handshake
    return 1 * RTT


def quic_0rtt():
    # Resumed QUIC connection can send application
    # data immediately with 0-RTT
    return 0


print("CONNECTION SETUP TIME")
print("-" * 35)

print(
    f"TCP + TLS 1.2 : "
    f"{tcp_tls12() * 1000:.0f} ms"
)

print(
    f"TCP + TLS 1.3 : "
    f"{tcp_tls13() * 1000:.0f} ms"
)

print(
    f"QUIC first visit: "
    f"{quic_first_visit() * 1000:.0f} ms"
)

print(
    f"QUIC 0-RTT     : "
    f"{quic_0rtt() * 1000:.0f} ms"
)

print()
print("RTT used:", RTT * 1000, "ms")