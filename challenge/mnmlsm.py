from os import path
from flask import *
from datetime import datetime
from pyppeteer import launch
app = Flask(__name__)

DEFAULT_MESSAGE = {'name': 'NadirH', 'date': '16:04 Apr 10, 2023'}
message_log = [DEFAULT_MESSAGE]

# Add CSP globally
@app.after_request
def add_csp(resp):
	resp.headers['Content-Security-Policy'] = "script-src 'self' 'unsafe-eval'; object-src 'none'; base-uri 'none';"
	return resp

@app.route('/')
def main_page():
	return render_template('main_page.html', message_log_enum=enumerate(message_log))

@app.route('/api/clear', methods=['GET', 'POST'])
def clear():
	global message_log
	message_log = [DEFAULT_MESSAGE]
	return '', 201

@app.route('/api/mark', methods=['GET', 'POST'])
def mark():
	name = request.values.get('name', 'Anon')
	if len(name) > 8:
		name = name[:8] + "..."
	message_log.append({
		'name': name,
		'date': datetime.now().strftime('%-H:%m %b %-m, %Y')
	})
	return '', 201

@app.route('/api/check')
async def check():
	browser = await launch(
		args=['--no-sandbox', '--disable-setuid-sandbox'],
		executablePath='/usr/bin/chromium-browser' if path.exists('/usr/bin/chromium-browser') else '',
		handleSIGINT=False,
		handleSIGTERM=False,
		handleSIGHUP=False
	)
	page = await browser.newPage()
	await page.setExtraHTTPHeaders({'flag': 'MNMLSM{{<_is_>}}'}) # Please submit the payload as a solution, and not the flag
	await page.goto('http://127.0.0.1:8005/', waitUntil=['load', 'domcontentloaded', 'networkidle2'])
	await page.close()
	await browser.close()
	return 'Your marks have been reviewed.'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8005)
