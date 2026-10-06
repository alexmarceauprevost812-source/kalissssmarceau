# cookie_manager.py

import http.cookiejar
import urllib.request

class CookieManager:
    def __init__(self, filename):
        self.filename = filename
        self.cookie_jar = http.cookiejar.MozillaCookieJar(filename)

    def load_cookies(self):
        try:
            self.cookie_jar.load(ignore_discard=True, ignore_expires=True)
            print("Cookies loaded successfully.")
        except Exception as e:
            print(f"Error loading cookies: {e}")

    def save_cookies(self):
        try:
            self.cookie_jar.save(ignore_discard=True, ignore_expires=True)
            print("Cookies saved successfully.")
        except Exception as e:
            print(f"Error saving cookies: {e}")

    def add_cookie(self, url, name, value):
        try:
            cookie = http.cookiejar.Cookie(version=0, name=name, value=value, port=None, port_specified=False, domain=url, domain_specified=False, domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=None, discard=True, comment=None, comment_url=None, rest={'HttpOnly': None, 'Secure': None})
            self.cookie_jar.set_cookie(cookie)
            print(f"Cookie added: {name}={value}")
        except Exception as e:
            print(f"Error adding cookie: {e}")

    def get_cookies(self, url):
        try:
            cookies = self.cookie_jar._cookies[url]
            cookie_str = "; ".join([f"{c.name}={c.value}" for c in cookies.values()])
            print(f"Cookies for {url}: {cookie_str}")
            return cookie_str
        except Exception as e:
            print(f"Error getting cookies: {e}")
            return None

if __name__ == "__main__":
    cookie_manager = CookieManager("cookies.txt")
    cookie_manager.load_cookies()
    cookie_manager.add_cookie("http://cible.8000", "session_id", "1234567890")
    cookie_manager.save_cookies()
    cookies = cookie_manager.get_cookies("http://cible.8000")