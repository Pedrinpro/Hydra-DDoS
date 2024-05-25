
from http.server import HTTPServer, BaseHTTPRequestHandler

# Define a classe de manipulador de solicitação
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/Server.html'
        try:
            # Abre o arquivo solicitado
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "Arquivo não encontrado"
            self.send_response(404)
        self.end_headers()
        # Envia o conteúdo do arquivo
        self.wfile.write(bytes(file_to_open, 'utf-8'))

# Cria e inicia o servidor HTTP
def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Servidor rodando em http://localhost:{port}/")
    httpd.serve_forever()

# Executa o servidor
if __name__ == "__main__":
    run()
