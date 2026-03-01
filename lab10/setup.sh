#!/bin/bash
# Lab 10: Setup nginx with proxy_pass to Python API
# Run as root or with sudo

echo "=== Installing nginx ==="
sudo apt update -q && sudo apt install -y nginx

echo ""
echo "=== Creating HTML page ==="
sudo bash -c 'cat > /var/www/html/my_site.html << HTML
<!DOCTYPE html>
<html>
<body>
  <h1>My site on port 8000</h1>
  <p>Try: <a href="/api/status">/api/status</a> — proxied to Python API on :5000</p>
</body>
</html>
HTML'

echo ""
echo "=== Installing nginx config ==="
sudo cp nginx_proxy.conf /etc/nginx/sites-available/lab10
sudo ln -sf /etc/nginx/sites-available/lab10 /etc/nginx/sites-enabled/lab10

echo ""
echo "=== Testing nginx config ==="
sudo nginx -t

echo ""
echo "=== Reloading nginx ==="
sudo systemctl reload nginx

echo ""
echo "=== Starting API server (background) ==="
python3 api_server.py &
API_PID=$!
sleep 1

echo ""
echo "=== Testing static page ==="
curl -s http://localhost:8000/ 

echo ""
echo "=== Testing proxy_pass to API ==="
curl -s http://localhost:8000/api/status | python3 -m json.tool

echo ""
echo "=== Cleanup ==="
kill $API_PID 2>/dev/null
sudo rm -f /etc/nginx/sites-enabled/lab10
sudo rm -f /etc/nginx/sites-available/lab10
sudo systemctl reload nginx
echo "Done."
