import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title='TaskFlow API')

@app.get('/', response_class=HTMLResponse)
def home():
    return '<html><head><title>TaskFlow</title></head><body style="font-family:system-ui;margin:60px"><h1>TaskFlow API</h1><p>Your task service is running.</p><p><a href="/docs">API documentation</a> | <a href="/health">Health check</a></p></body></html>'

@app.get('/health')
def health():
    return {'status': 'healthy', 'version': os.getenv('APP_VERSION', '1.0.0')}

@app.get('/tasks')
def tasks():
    return [{'id': 1, 'title': 'Review deployment', 'completed': False}, {'id': 2, 'title': 'Check application health', 'completed': True}]
