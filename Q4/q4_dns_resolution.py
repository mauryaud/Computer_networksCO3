"""Iterative DNS resolution through root, TLD
and authoritative servers.
"""

SERVERS = {
    "root": {
        "in.": "tld-in",
        "com.": "tld-com"
    },

    "tld-in": {
        "ac.in.": "ns-ac"
    },

    "tld-com": {
        "example.com.": "ns-example"
    },

    "ns-ac": {
        "simats.ac.in.": "ns-simats"
    },

    "ns-simats": {
        "results.simats.ac.in.": "10.20.30.40"
    },

    "ns-example": {
        "www.example.com.": "93.184.216.34"
    },
}


cache = {}


def resolve(name):

    if name in cache:
        return cache[name], 0

    server = "root"
    queries = 0

    while True:

        queries += 1

        records = SERVERS[server]

        matches = [
            key
            for key in records
            if name.endswith(key)
        ]

        if not matches:
            raise ValueError(
                f"No DNS record found for {name}"
            )

        longest_key = max(
            matches,
            key=len
        )

        value = records[longest_key]

        # If the value contains a digit,
        # treat it as an IP address.
        if any(ch.isdigit() for ch in value):

            cache[name] = value

            return value, queries

        server = value


for name in (
    "results.simats.ac.in.",
    "www.example.com.",
    "results.simats.ac.in."
):

    ip, q = resolve(name)

    print(
        f"{name:<24} "
        f"{ip:<15} "
        f"queries sent: {q}"
    )