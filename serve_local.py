"""
Servidor HTTP simples para servir os arquivos localmente
Acesse: http://localhost:8000/hybrid_workflow_knowledge.html
"""
import http.server
import socketserver
import os

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Adicionar CORS headers se necessário
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"🚀 Servidor rodando em http://localhost:{PORT}")
        print(f"📄 Acesse: http://localhost:{PORT}/hybrid_workflow_knowledge.html")
        print(f"⏹️  Pressione Ctrl+C para parar")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Servidor parado")

if __name__ == "__main__":
    main()

