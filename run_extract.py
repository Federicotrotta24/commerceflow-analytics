from include.extract.extract_raw import extract_raw

if __name__ == "__main__":
    endpoints = ["products", "users", "carts"]

    for endpoint in endpoints:
        extract_raw(endpoint)