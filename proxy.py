from better_proxy import Proxy

def get_proxy_dict(proxy: str):
    try:
        proxy = Proxy.from_str(proxy=proxy.strip())

        proxy_dict = dict(
            scheme=proxy.protocol,
            hostname=proxy.host,
            port=proxy.port,
            username=proxy.login,
            password=proxy.password,
        )

        return proxy_dict
    except ValueError:
        return None