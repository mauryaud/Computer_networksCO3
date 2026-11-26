"""M/M/1 model of a router output link:
arrivals at rate lam, service at rate mu.
"""


def mm1(lam, mu):

    if lam >= mu:
        return None

    rho = lam / mu

    L = rho / (1 - rho)

    W = 1 / (mu - lam)

    return rho, L, W


mu = 1000

for lam in (
    500,
    800,
    900,
    950,
    990,
    1000
):

    result = mm1(lam, mu)

    if result is None:

        print(
            f"load {lam:4d} pkt/s: "
            f"unstable, queue grows without limit"
        )

    else:

        rho, L, W = result

        print(
            f"load {lam:4d} pkt/s: "
            f"rho {rho:.2f} "
            f"L {L:6.1f} pkts "
            f"W {W * 1000:6.1f} ms"
        )