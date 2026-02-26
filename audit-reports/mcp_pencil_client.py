import subprocess
import json
import time

html_path = "/Users/jameshou/Desktop/DS revamp trial/audit-reports/webapp-ds-audit-2026-02-25.html"
pen_path = "/Users/jameshou/Desktop/DS revamp trial/audit-reports/webapp-ds-audit-2026-02-25.pen"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

ops = f'page = I(document, {{"type": "frame", "name": "Pencil Page (Code)", "layout": "vertical", "width": 1000, "height": "fit_content", "padding": 40, "fill": {{"type": "color", "color": "#1e1e1e"}} }})\n'
ops += f'I(page, {{"type": "text", "content": {json.dumps(html)}, "fill": "#d4d4d4", "fontSize": 12, "fontFamily": "Geist Mono", "textGrowth": "fixed-width", "width": "fill_container"}})'

proc = subprocess.Popen(
    ['/Users/jameshou/.antigravity/extensions/highagency.pencildev-0.6.28-universal/out/mcp-server-darwin-arm64', '--app', 'antigravity'],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    text=False  # binary mode to write \r\n explicitly and read precisely
)

def send_message(msg):
    data = json.dumps(msg).encode('utf-8')
    header = f"Content-Length: {len(data)}\r\n\r\n".encode('utf-8')
    proc.stdin.write(header + data)
    proc.stdin.flush()

def read_message():
    # Read headers
    content_length = 0
    while True:
        line = proc.stdout.readline().decode('utf-8')
        if not line or line == '\r\n':
            break
        if line.lower().startswith("content-length:"):
            content_length = int(line.split(":")[1].strip())
    if content_length > 0:
        data = proc.stdout.read(content_length).decode('utf-8')
        return json.loads(data)
    return None

init_req = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
        "protocolVersion": "2024-11-05",
        "capabilities": {},
        "clientInfo": {"name": "python", "version": "1.0"}
    }
}
send_message(init_req)

while True:
    resp = read_message()
    if resp and resp.get("id") == 1:
        break

send_message({"jsonrpc": "2.0", "method": "notifications/initialized"})

call_req = {
    "jsonrpc": "2.0",
    "id": 2,
    "method": "tools/call",
    "params": {
        "name": "batch_design",
        "arguments": {
            "filePath": pen_path,
            "operations": ops
        }
    }
}
send_message(call_req)

while True:
    resp = read_message()
    if resp and resp.get("id") == 2:
        print("Response:", json.dumps(resp, indent=2))
        break

proc.terminate()
