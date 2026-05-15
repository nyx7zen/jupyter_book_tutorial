# 환경 설정 및 프로젝트 생성

## 개요

이 문서는 Jupyter Book 튜토리얼 프로젝트를 시작하기 위한 환경 설정 및 프로젝트 생성 방법을 설명합니다.

대상 환경은 아래 2가지입니다.

- Windows + WinPython
- WSL + Anaconda

GitHub 연동은 아래 2가지 인증 방식을 지원합니다.

- HTTPS + PAT 방식
- SSH 방식

### Jupyter Book 버전 안내

이 튜토리얼은 **Jupyter Book v1 (1.x)** 을 기준으로 작성되었습니다.

| 항목 | v1 (이 튜토리얼) | v2 |
|------|-----------------|-----|
| 설정 파일 | `_config.yml` + `_toc.yml` | `myst.yml` (통합) |
| 빌드 명령 | `jupyter-book build docs/` | `jupyter book build docs/` (공백) |
| 기반 엔진 | Sphinx | MyST-MD (새 엔진) |
| 안정성 | 안정 버전 | 아직 개발 중 (2025년 기준) |

> v2 는 설정 파일 구조와 빌드 명령이 완전히 다릅니다. pip 설치 시 최신 버전(v2)이 설치될 수 있으므로 반드시 버전을 지정해야 합니다.

---

## 사전 요구사항

### Windows + WinPython

| 항목 | 내용 |
|------|------|
| OS | Windows 10/11 |
| Python | WinPython (환경 활성화 불필요) |
| Git | Git for Windows 설치 |

### WSL + Anaconda

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

## jupyter-book 설치

> **버전 주의:** `pip install jupyter-book` 만 실행하면 v2 (최신 버전) 가 설치됩니다. 이 튜토리얼은 v1 기준이므로 반드시 버전을 지정합니다.

### Windows + WinPython

```cmd
pip install jupyter-book==1.0.4 ghp-import

# 설치 확인 (v1.0.4 가 표시되어야 합니다)
jupyter-book --version
```

### WSL + Anaconda

```bash
conda activate pytorch_env
pip install jupyter-book==1.0.4 ghp-import

# 설치 확인 (v1.0.4 가 표시되어야 합니다)
jupyter-book --version
```

---

## 프로젝트 폴더 구조

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
│       ├── doc-04-new-project.md
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

## 폴더 생성

### Windows + WinPython

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

### WSL + Anaconda

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

## setup.py 작성

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

## 패키지 설치 (pip install -e .)

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

## GitHub 레포 생성 및 연동

### 레포 생성

GitHub 에 접속하여 새 레포지토리를 생성합니다.

- GitHub 로그인 → New repository
- Repository name: `myrepo`
- Visibility: Public (GitHub Pages 무료 사용)
- Initialize: 체크 해제 (로컬에서 push 할 예정)
- Create repository 클릭

### Git 전역 설정

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

### 인증 방식

환경과 인증 방식에 따라 아래 4가지 조합이 있습니다.

| 환경 | 인증 방식 | 참조 문서 |
|------|-----------|-----------|
| Windows | HTTPS + PAT | {doc}`git-01-setup-https` |
| Windows | SSH | {doc}`git-02-setup-ssh` |
| WSL | HTTPS + PAT | {doc}`git-01-setup-https` |
| WSL | SSH | {doc}`git-02-setup-ssh` |

**HTTPS + PAT 방식** 은 설정이 간단하며 Windows 자격증명 관리자를 사용합니다.

**SSH 방식** 은 초기 설정이 필요하지만 이후 인증이 자동으로 처리됩니다. 여러 GitHub 계정을 사용하는 경우에 유리합니다.

### remote 연결 및 최초 push

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

## GitHub Pages 설정

GitHub Pages 는 빌드된 Jupyter Book 을 웹에 공개하는 기능입니다.

**최초 1회 설정 순서:**

1. 먼저 `git push` 로 Actions 를 실행하여 `gh-pages` 브랜치를 생성합니다.
2. Actions 가 성공한 후 아래 설정을 진행합니다.
3. GitHub 레포 → **Settings** 탭 클릭
4. 왼쪽 사이드바 → **Pages** 클릭
5. **Source** 섹션에서:
   - `Deploy from a branch` 선택
   - Branch: **`gh-pages`** 선택
   - 폴더: **`/ (root)`** 선택
6. **Save** 클릭

> `gh-pages` 브랜치는 GitHub Actions 가 최초 배포 시 자동으로 생성합니다.
> Actions 실행 전에는 목록에 나타나지 않습니다.

**배포 URL:**

```
https://<username>.github.io/myrepo/
```

---

## 로컬 빌드 확인

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
_build/
docs/.jupyter_cache/
__pycache__/
*.pyc
*.egg-info/
.ipynb_checkpoints/
```

> `_build/` 항목은 레포 루트에 빌드 캐시가 생성될 경우를 대비하여 추가합니다.

---

## GitHub Actions 배포 설정

`.github/workflows/deploy.yml` 파일을 생성합니다.

```yaml
name: Deploy Jupyter Book

on:
  push:
    branches: [main]

permissions:
  contents: write

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install jupyter-book==1.0.4 ghp-import
          pip install -e .

      - name: Build
        run: jupyter-book build docs/

      - name: Deploy
        run: ghp-import -n -p -f docs/_build/html
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

주요 설정 항목:

| 항목 | 설명 |
|------|------|
| `permissions: contents: write` | `gh-pages` 브랜치 push 권한 부여 |
| `jupyter-book==1.0.4` | v1 버전 고정 (미지정 시 v2 설치됨) |
| `actions/checkout@v4` | 최신 checkout action |
| `actions/setup-python@v5` | 최신 Python setup action |

---

## 일상 워크플로우

문서를 수정하거나 새 문서를 추가할 때마다 아래 순서로 진행합니다.

### 문서 수정 / 노트북 작업

VSCode 에서 `.md` 파일 또는 `.ipynb` 파일을 편집합니다.

- 마크다운 문서: 내용 수정 후 저장
- 노트북: 셀 실행 후 `Ctrl+S` 로 출력 포함 저장

### 로컬 빌드 확인

#### Windows + WinPython

```cmd
cd D:\projects\myrepo
jupyter-book build docs/
start docs\_build\html\index.html
```

#### WSL + Anaconda

```bash
conda activate pytorch_env
cd ~/projects/myrepo
jupyter-book build docs/
explorer.exe docs/_build/html/index.html
```

### clean 옵션 사용 시점

`jupyter-book clean docs/` 는 `docs/_build/` 폴더를 삭제하여 처음부터 다시 빌드합니다.

| 상황 | clean 필요 여부 |
|------|----------------|
| 단순 내용 수정 (`.md`, `.ipynb`) | 불필요 |
| `_toc.yml` 구조 변경 | 권장 |
| `_config.yml` 변경 | 권장 |
| 파일 삭제 또는 이름 변경 | 권장 |
| 빌드 오류 발생 시 | 권장 |
| 빌드 결과가 이상하게 보일 때 | 권장 |

```bash
# 캐시 삭제 후 재빌드
jupyter-book clean docs/
jupyter-book build docs/
```

### 커밋 및 푸시

로컬에서 확인 후 GitHub 에 push 합니다.

```bash
git add .
git commit -m "docs: 변경 내용 요약"
git push origin main
```

### 배포 확인

push 후 GitHub Actions 가 자동으로 빌드 및 배포합니다.

- GitHub 레포 → **Actions** 탭 → 초록색 체크 확인
- 배포 URL: `https://<username>.github.io/myrepo/`

> GitHub Actions 배포까지 보통 1~3분 소요됩니다.
