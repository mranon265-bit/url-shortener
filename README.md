## URL SHORTENER
This is a tiny url shortener under 200 lines of python made with hashlib and flask. 
It converts long URLs into short, hash-based codes and redirects users when
they visit the short link.

## Features
- Shortens URLs into short codes
- Redirects users when the short code is visited 

## Getting started
### Clone the repo
```bash
git clone https://github.com/mranon265-bit/url-shortener.git
cd url-shortener

```

### Create Virtual environment and install dependencies 

```bash 
python -m venv venv
source venv/bin/activate
pip install flask 
```

### Run the app and test
```bash
python app.py


curl -X POST http://127.0.0.1:5000/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com/some/really/long/path"}'

curl http://127.0.0.1:5000/short_code

```