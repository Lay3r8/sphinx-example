# Sphinx Example
This is a very simple example of how to autogenerate Google style docs from code using Sphinx with autodoc and napoleon extensions on a Linux machine.

## Installation
```bash
git clone git@github.com:Lay3r8/sphinx-example.git
cd sphinx-example

# Python setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Node JS setup (optional if you don't want something to serve the docs)
npm install
```

## Usage
```bash
# Generate the docs
cd docs
chmod +x generate_doc.sh
./generate_doc.sh

# Serve the docs
npm run start
```
