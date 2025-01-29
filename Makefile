.ONESHELL:
browser:
	& "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222
push:
	cls
	git add .
	git commit -m "$(msg)"
	git push -u origin main