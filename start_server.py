import argparse
import http.server
import socketserver

DEFAULT_PORT = 8091
DEFAULT_BIND = "127.0.0.1"


class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True


def main():
    parser = argparse.ArgumentParser(description="读名著静态站点本地服务器")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT,
                        help=f"监听端口（默认 {DEFAULT_PORT}）")
    parser.add_argument("--bind", default=DEFAULT_BIND,
                        help=f"监听地址（默认 {DEFAULT_BIND}）")
    args = parser.parse_args()

    with ReusableTCPServer((args.bind, args.port), http.server.SimpleHTTPRequestHandler) as httpd:
        print(f"Server running at http://{args.bind}:{args.port}")
        httpd.serve_forever()


if __name__ == "__main__":
    main()
