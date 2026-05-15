# doc-01. 환경 설정 및 프로젝트 생성

## 1. 개요

이 문서는 Jupyter Book 튜토리얼 프로젝트를 시작하기 위한 환경 설정 및 프로젝트 생성 방법을 설명합니다.

대상 환경은 아래 2가지입니다.

- Windows + WinPython
- WSL + Anaconda

GitHub 연동은 아래 2가지 인증 방식을 지원합니다.

- HTTPS + PAT 방식
- SSH 방식

---

## 2. 사전 요구사항

### 2.1 Windows + WinPython

| 항목 | 내용 |
|------|------|
| OS | Windows 10/11 |
| Python | WinPython (환경 활성화 불필요) |
| Git | Git for Windows 설치 |

### 2.2 WSL + Anaconda

| 항목 | 내용 |
|------|------|
| OS | Windows 10/11 + WSL2 (Ubuntu) |
| Python | Anaconda, conda 환경: `pytorch_env` |
| Git | WSL 내 git 설치 |

VSCode 필수 확장:

- Remote - WSL
- Python
- Jupyter
- MyST-Markdown

---

## 3. jupyter-book 설치

### 3.1 Windows + WinPython

```cmd
pip install jupyter-book ghp-import

# 설치 확인
jupyter-book --version
```

### 3.2 WSL + Anaconda

```bash
conda activate pytorch_env
pip install jupyter-book ghp-import

# 설치 확인
jupyter-book --version
```

---

## 4. 프로젝트 폴더 구조

```
myrepo/
├── src/
│   ├── __init__.py
│   ├── signals.py
│   └── plotter.py
├── docs/
│   ├── _config.yml
│   ├── _toc.yml
│   ├── intro.md
│   └── contents/
│       ├── doc-01-setup.md
│       ├── doc-02-section.md
│       ├── doc-03-chapter.md
│       ├── git-01-setup-https.md
│       ├── git-02-setup-ssh.md
│       └── notebooks/
│           └── nb-01-signals.ipynb
├── .github/
│   └── workflows/
│       └── deploy.yml
├── .gitignore
├── setup.py
└── README.md
```

---

## 5. 폴더 생성

### 5.1 Windows + WinPython

```cmd
cd D:\projects
mkdir myrepo
cd myrepo
mkdir src
mkdir docs
mkdir docs\contents
mkdir docs\contents\notebooks
mkdir .github
mkdir .github\workflows
```

### 5.2 WSL + Anaconda

```bash
cd ~/projects
mkdir myrepo
cd myrepo
mkdir src
mkdir docs
mkdir docs/contents
mkdir docs/contents/notebooks
mkdir .github
mkdir .github/workflows
```

---

## 6. setup.py 작성

레포 루트에 `setup.py` 파일을 생성합니다.

```python
from setuptools import setup, find_packages

setup(
    name="myrepo",
    version="0.1.0",
    packages=find_packages(),
)
```

`src/__init__.py` 파일도 생성합니다. 내용은 비워도 됩니다.
역할과 기능에 대한 상세 설명은 {doc}`doc-02-section` 을 참고하세요.

---

## 7. 패키지 설치 (pip install -e .)

editable 모드로 설치하면 `src/` 코드 수정이 즉시 반영됩니다.

### Windows + WinPython

```cmd
cd D:\projects\myrepo
pip install -e .
```

### WSL + Anaconda

```bash
conda activate pytorch_env
cd ~/projects/myrepo
pip install -e .
```

설치 확인:

```python
# 노트북 또는 Python 에서 확인
from src.signals import generate_sine
print("import 성공")
```

---

## 8. GitHub 레포 생성 및 연동

### 8.1 레포 생성

GitHub 에 접속하여 새 레포지토리를 생성합니다.

- GitHub 로그인 → New repository
- Repository name: `myrepo`
- Visibility: Public (GitHub Pages 무료 사용)
- Initialize: 체크 해제 (로컬에서 push 할 예정)
- Create repository 클릭

### 8.2 Git 전역 설정

최초 1회 설정합니다.

#### Windows

```cmd
git config --global user.name "<사용자명>"
git config --global user.email "<이메일>"
git config --global init.defaultBranch main
git config --global core.autocrlf true
git config --global core.editor "code --wait"

# 설정 확인
git config --list --global
```

#### WSL

```bash
git config --global user.name "<사용자명>"
git config --global user.email "<이메일>"
git config --global init.defaultBranch main
git config --global core.autocrlf input
git config --global core.editor "code --wait"

# 설정 확인
git config --list --global
```

### 8.3 인증 방식

환경과 인증 방식에 따라 아래 4가지 조합이 있습니다.

| 환경 | 인증 방식 | 참조 문서 |
|------|-----------|-----------|
| Windows | HTTPS + PAT | {doc}`git-01-setup-https` |
| Windows | SSH | {doc}`git-02-setup-ssh` |
| WSL | HTTPS + PAT | {doc}`git-01-setup-https` |
| WSL | SSH | {doc}`git-02-setup-ssh` |

**HTTPS + PAT 방식** 은 설정이 간단하며 Windows 자격증명 관리자를 사용합니다.

**SSH 방식** 은 초기 설정이 필요하지만 이후 인증이 자동으로 처리됩니다. 여러 GitHub 계정을 사용하는 경우에 유리합니다.

### 8.4 remote 연결 및 최초 push

인증 방식에 따라 remote URL 형식이 다릅니다.

#### HTTPS 방식

```bash
git init
git remote add origin https://github.com/<username>/myrepo.git
```

#### SSH 방식

```bash
git init
git remote add origin git@github.com:<username>/myrepo.git
```

최초 push:

```bash
git add .
git commit -m "init"
git push -u origin main
```

---

## 9. GitHub Pages 설정

GitHub Pages 는 빌드된 Jupyter Book 을 웹에 공개하는 기능입니다.

**최초 1회 설정:**

- GitHub 레포 → Settings → Pages
- Source: `Deploy from a branch` 선택
- Branch: `gh-pages` 선택 → Save

> `gh-pages` 브랜치는 GitHub Actions 가 최초 배포 시 자동으로 생성합니다.
> 따라서 최초 push 후 Actions 가 실행된 다음 설정하면 됩니다.

**배포 URL:**

```
https://<username>.github.io/myrepo/
```

---

## 10. 로컬 빌드 확인

GitHub Actions 배포 전에 로컬에서 먼저 확인합니다.

### Windows + WinPython

```cmd
cd D:\projects\myrepo
jupyter-book build docs/

# 브라우저로 확인
start docs\_build\html\index.html
```

### WSL + Anaconda

```bash
conda activate pytorch_env
cd ~/projects/myrepo
jupyter-book build docs/

# 브라우저로 확인
explorer.exe docs/_build/html/index.html
```

빌드 오류 시:

```bash
# 캐시 삭제 후 재빌드
jupyter-book clean docs/
jupyter-book build docs/
```

---

## .gitignore

레포 루트에 `.gitignore` 파일을 생성합니다.

```
docs/_build/
docs/.jupyter_cache/
__pycache__/
*.pyc
*.egg-info/
.ipynb_checkpoints/
```

---

## GitHub Actions 배포 설정

`.github/workflows/deploy.yml` 파일을 생성합니다.

```yaml
name: Deploy Jupyter Book

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install jupyter-book ghp-import
          pip install -e .

      - name: Build
        run: jupyter-book build docs/

      - name: Deploy
        run: ghp-import -n -p -f docs/_build/html
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```
