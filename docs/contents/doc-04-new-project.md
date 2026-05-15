# 새 Jupyter Book 프로젝트 생성

## 개요

완성된 튜토리얼 구조를 복사하여 새 Jupyter Book 프로젝트를 시작하는 방법을 설명합니다.

> 이 튜토리얼은 **Jupyter Book v1 (1.0.4)** 기준으로 작성되었습니다.

---

## 복사 대상

기존 튜토리얼 프로젝트에서 아래 두 폴더를 새 프로젝트로 복사합니다.

```
jupyter_book_tutorial/docs/   →   new_project/docs/
jupyter_book_tutorial/src/    →   new_project/src/
```

---

## 필수 수정 파일 목록

```
new_project/
├── docs/
│   ├── _config.yml          ← 제목/저자/URL 수정
│   ├── _toc.yml             ← 새 문서 구조로 수정
│   ├── intro.md             ← 새 프로젝트 소개로 수정
│   └── contents/
│       ├── *.md             ← 새 문서로 교체
│       └── notebooks/
│           └── *.ipynb      ← 새 노트북으로 교체
└── setup.py                 ← name 변경
```

---

## `setup.py` 수정

`name` 을 새 프로젝트명으로 변경합니다.

```python
from setuptools import setup, find_packages

setup(
    name="new_project",      # ← 변경
    version="0.1.0",
    packages=find_packages(),
)
```

---

## `_config.yml` 수정

`docs/_config.yml` 에서 아래 항목을 수정합니다.

```yaml
title: "새 프로젝트 제목"          # ← 변경
author: "작성자명"                  # ← 변경
logo: ""

execute:
  execute_notebooks: "off"

kernelspec:
  name: pytorch_env

repository:
  url: https://github.com/<username>/new_project   # ← 변경
  branch: main
  path_to_book: docs

html:
  use_repository_button: true
  use_issues_button: true
```

---

## `intro.md` 수정

`docs/intro.md` 를 새 프로젝트 소개로 수정합니다.

```markdown
# 새 프로젝트 제목

프로젝트 소개 작성

## 문서 구성

- doc-01: 첫 번째 문서
- doc-02: 두 번째 문서
```

---

## `_toc.yml` 수정

### 섹션 구조 (챕터 없음)

`docs/_toc.yml` 에서 새 문서를 추가하거나 기존 항목을 교체합니다.

**기본 구조:**

```yaml
format: jb-book
root: intro

chapters:
  - file: contents/새문서1
  - file: contents/새문서2
  - file: contents/notebooks/새노트북
```

**하위 섹션 추가:**

```yaml
format: jb-book
root: intro

chapters:
  - file: contents/새문서1
    sections:
      - file: contents/새문서1-1
      - file: contents/새문서1-2
  - file: contents/새문서2
  - file: contents/notebooks/새노트북
```

> `_toc.yml` 에 등록된 파일만 사이드바에 표시됩니다.
> 새 파일을 추가할 때는 반드시 `_toc.yml` 에도 등록해야 합니다.

### 챕터 + 섹션 구조

**새 챕터 추가:**

```yaml
format: jb-book
root: intro

parts:
  - caption: "chapter-01. 기존 챕터"
    chapters:
      - file: contents/기존문서

  - caption: "chapter-02. 새 챕터"        ← 추가
    chapters:
      - file: contents/새문서1
      - file: contents/새문서2
        sections:
          - file: contents/새문서2-1
          - file: contents/새문서2-2
```

**기존 챕터에 문서 추가:**

```yaml
format: jb-book
root: intro

parts:
  - caption: "chapter-01. 기존 챕터"
    chapters:
      - file: contents/기존문서1
      - file: contents/새문서          ← 추가
```

**기존 문서에 하위 섹션 추가:**

```yaml
parts:
  - caption: "chapter-01. 기존 챕터"
    chapters:
      - file: contents/기존문서1
        sections:
          - file: contents/새하위문서   ← 추가
```

---

## 그대로 유지해도 되는 항목

| 항목 | 이유 |
|------|------|
| `.github/workflows/deploy.yml` | 레포명 자동 반영, 수정 불필요 |
| `.gitignore` | 동일하게 사용 가능 |

---

## 작업 순서

### 프로젝트 복사 및 수정

```
1. docs/ + src/ 복사
2. setup.py      → name 변경
3. _config.yml   → 제목/저자/URL 수정
4. _toc.yml      → 새 문서 구조로 수정
5. intro.md      → 새 프로젝트 소개 작성
6. contents/     → 새 문서/노트북으로 교체
```

### 로컬 빌드 확인

#### Windows + WinPython

```cmd
cd D:\projects\new_project
jupyter-book clean docs/
jupyter-book build docs/
start docs\_build\html\index.html
```

#### WSL + Anaconda

```bash
conda activate pytorch_env
cd ~/projects/new_project
jupyter-book clean docs/
jupyter-book build docs/
explorer.exe docs/_build/html/index.html
```

> `_toc.yml` 을 수정한 경우 반드시 `clean` 후 빌드합니다.

### GitHub 레포 생성

- GitHub 로그인 → **New repository**
- Repository name: `new_project`
- Visibility: **Public**
- Initialize: **체크 해제**
- **Create repository** 클릭

### 커밋 및 푸시

#### HTTPS 방식

```bash
git init
git remote add origin https://github.com/<username>/new_project.git
git add .
git commit -m "init: new jupyter book project"
git push -u origin main
```

#### SSH 방식

```bash
git init
git remote add origin git@github.com:<username>/new_project.git
git add .
git commit -m "init: new jupyter book project"
git push -u origin main
```

### GitHub Pages 설정 (최초 1회)

push 후 Actions 가 성공하면 GitHub Pages 를 활성화합니다.

1. GitHub 레포 → **Settings** 탭
2. 왼쪽 사이드바 → **Pages**
3. Source: `Deploy from a branch` 선택
4. Branch: **`gh-pages`** / **`/ (root)`** 선택
5. **Save** 클릭

### 배포 URL 확인

```
https://<username>.github.io/new_project/
```

---

## 이후 문서 수정 시 워크플로우

새 문서 추가 또는 기존 문서 수정 시 아래 순서로 진행합니다.

```
문서/노트북 편집
    ↓
_toc.yml 수정 (새 파일 추가 시)
    ↓
jupyter-book clean docs/  (_toc.yml 변경 시)
jupyter-book build docs/  (로컬 확인)
    ↓
git add .
git commit -m "docs: 변경 내용 요약"
git push origin main
    ↓
GitHub Actions 자동 배포
```
