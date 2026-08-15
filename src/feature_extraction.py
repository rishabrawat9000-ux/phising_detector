from urllib.parse import urlparse
from collections import Counter
import math
import re
import ipaddress


# ============================================================
# ENTROPY
# ============================================================

def entropy(s: str) -> float:
    """
    Calculate Shannon entropy of a string.
    """
    if not s:
        return 0.0

    counts = Counter(s)
    length = len(s)

    return -sum(
        (count / length) * math.log2(count / length)
        for count in counts.values()
    )


# ============================================================
# FEATURE EXTRACTION
# ============================================================

def extract_features(url):
    features = {}

    # --------------------------------------------------------
    # Basic URL features
    # --------------------------------------------------------

    features["url_length"] = len(url)

    features["dots"] = url.count(".")
    features["hyphens"] = url.count("-")
    features["digits"] = sum(c.isdigit() for c in url)
    features["slashes"] = url.count("/")
    features["question_marks"] = url.count("?")
    features["equal_signs"] = url.count("=")
    features["at_symbol"] = url.count("@")
    features["ampersand"] = url.count("&")
    features["percent"] = url.count("%")
    features["underscore"] = url.count("_")
    features["tilde"] = url.count("~")

    # --------------------------------------------------------
    # Parse URL
    # --------------------------------------------------------

    # urlparse needs a scheme to correctly identify hostname
    parse_url = url

    if "://" not in parse_url:
        parse_url = "http://" + parse_url

    parsed = urlparse(parse_url)

    scheme = parsed.scheme.lower()
    hostname = parsed.hostname or ""
    path = parsed.path or ""
    query = parsed.query or ""
    fragment = parsed.fragment or ""

    # --------------------------------------------------------
    # URL structure
    # --------------------------------------------------------

    features["scheme_len"] = len(scheme)

    features["hostname_len"] = len(hostname)

    features["query_len"] = len(query)

    features["fragment_len"] = len(fragment)

    features["path_len"] = len(path)

    features["has_query"] = int(bool(query))

    features["has_fragment"] = int(bool(fragment))

    features["has_https"] = int(scheme == "https")

    features["has_www"] = int(hostname.lower().startswith("www."))

    # --------------------------------------------------------
    # Port
    # --------------------------------------------------------

    try:
        features["has_port"] = int(parsed.port is not None)
    except ValueError:
        features["has_port"] = 0

    # --------------------------------------------------------
    # Subdomains
    # --------------------------------------------------------

    hostname_parts = hostname.split(".")

    if len(hostname_parts) >= 2:

        # Remove www from subdomain calculation
        if hostname_parts[0].lower() == "www":
            features["num_subdomains"] = max(
                len(hostname_parts) - 2,
                0
            )
        else:
            features["num_subdomains"] = max(
                len(hostname_parts) - 2,
                0
            )

    else:
        features["num_subdomains"] = 0

    # --------------------------------------------------------
    # IP address
    # --------------------------------------------------------

    try:
        ipaddress.ip_address(hostname)
        features["has_ip_address"] = 1
    except ValueError:
        features["has_ip_address"] = 0

    # --------------------------------------------------------
    # Punycode
    # --------------------------------------------------------

    features["has_punycode"] = int(
        "xn--" in hostname.lower()
    )

    # --------------------------------------------------------
    # Encoded characters
    # --------------------------------------------------------

    encoded_chars = re.findall(
        r"%[0-9a-fA-F]{2}",
        url
    )

    features["num_encoded_chars"] = len(encoded_chars)

    # --------------------------------------------------------
    # Suspicious keywords
    # --------------------------------------------------------

    suspicious_words = [
        "login",
        "signin",
        "sign-in",
        "secure",
        "security",
        "account",
        "update",
        "verify",
        "verification",
        "confirm",
        "confirmation",
        "password",
        "bank",
        "banking",
        "payment",
        "invoice",
        "wallet",
        "billing",
        "credential",

        # Popular brands commonly impersonated
        "paypal",
        "ebay",
        "amazon",
        "apple",
        "google",
        "microsoft",
        "facebook",
        "twitter",
        "instagram",
        "linkedin",
        "youtube",
        "netflix",
        "dropbox",
        "adobe",
        "steam",
        "spotify",
        "slack",
        "zoom",
        "twitch",
        "discord",
        "reddit",
        "pinterest",
        "wordpress",
        "blogspot"
    ]

    url_lower = url.lower()

    features["suspicious_word_count"] = sum(
        word in url_lower
        for word in suspicious_words
    )

    # --------------------------------------------------------
    # Entropy
    # --------------------------------------------------------

    features["url_entropy"] = entropy(url)

    features["domain_entropy"] = entropy(hostname)

    features["path_entropy"] = entropy(path)

    # --------------------------------------------------------
    # Character ratios
    # --------------------------------------------------------

    url_len = len(url)

    if url_len > 0:

        features["digit_ratio"] = (
            features["digits"] / url_len
        )

        features["letter_ratio"] = (
            sum(c.isalpha() for c in url) / url_len
        )

    else:

        features["digit_ratio"] = 0.0

        features["letter_ratio"] = 0.0

    # --------------------------------------------------------
    # Special character ratio
    # --------------------------------------------------------

    special_chars = set(
        "!@#$%^&*()-_=+[]{};:'\",.<>/?\\|`~"
    )

    if url_len > 0:

        features["special_char_ratio"] = (
            sum(
                c in special_chars
                for c in url
            ) / url_len
        )

    else:

        features["special_char_ratio"] = 0.0

    # --------------------------------------------------------
    # Maximum consecutive special characters
    # --------------------------------------------------------

    special_runs = re.findall(
        r"[^a-zA-Z0-9]+",
        url
    )

    features["max_special_run"] = max(
        (len(run) for run in special_runs),
        default=0
    )

    # --------------------------------------------------------
    # Return
    # --------------------------------------------------------

    return features