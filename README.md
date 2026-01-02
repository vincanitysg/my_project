# my_project

## Setup (WSL/Ubuntu)
```bash
cd ~/projects/my_project
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip


cat > README.md <<'EOF'
# my_project

## Setup (WSL/Ubuntu)
```bash
cd ~/projects/my_project
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip

# example
python -c "print('hello')"

# example
python -m unittest -q


Then verify:

```bash
cat README.md

git add README.md
git commit -m "Improve README"
git push

cat > README.md <<'EOF'
# my_project

## Setup (WSL/Ubuntu)
```bash
cd ~/projects/my_project
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip

python -c "print('hello')"
