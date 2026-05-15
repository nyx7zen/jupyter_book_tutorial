# 북 튜토리얼 (챕터와 섹션 구조)

## 개요

### 이 문서의 목적

챕터와 섹션으로 구성된 Jupyter Book 북을 작성하는 방법을 설명합니다.
섹션 구조와의 차이점을 중심으로 설명하며, 동일한 내용은 {doc}`doc-02-section` 을 참고하세요.

> 이 튜토리얼은 **Jupyter Book v1 (1.0.4)** 기준으로 작성되었습니다.
> 버전 설치 및 v1/v2 차이점은 {doc}`doc-01-setup` 을 참고하세요.

### doc-02 와의 관계

doc-02 에서 다룬 내용 중 아래 3가지만 다릅니다.

- 폴더 구조 (챕터별 하위 폴더 추가)
- `_toc.yml` 구조 (`parts` / `chapters` / `sections` 계층)
- `_config.yml` 일부 항목

src 코드, 마크다운 문서 작성법, 노트북 작성법, 빌드 및 배포 방법은 doc-02 와 동일합니다.

### 완성 후 폴더 구조

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

### 완성 후 사이드바 구조

```
Jupyter Book 튜토리얼
├── 소개
├── chapter-01. 환경 설정
│   └── 환경 설정 및 프로젝트 생성
│       ├── GitHub 연동 (HTTPS 방식)
│       └── GitHub 연동 (SSH 방식)
├── chapter-02. 마크다운 예제
│   ├── 문서 튜토리얼 (섹션 구조)
│   └── 북 튜토리얼 (챕터와 섹션 구조)
├── chapter-03. 활용
│   └── 새 Jupyter Book 프로젝트 생성
└── chapter-04. 노트북 예제
    └── [예제] 신호 생성 및 시각화
```

---

## 섹션 구조 vs 챕터 + 섹션 구조 비교

### _toc.yml 구조 비교

**doc-02 — 섹션 구조 (`jb-article`)**

```yaml
format: jb-article
root: intro

sections:
  - file: contents/doc-01-setup
    sections:
      - file: contents/git-01-setup-https
      - file: contents/git-02-setup-ssh
  - file: contents/doc-02-section
  - file: contents/doc-03-chapter
  - file: contents/doc-04-new-project
  - file: contents/notebooks/nb-01-signals
```

**doc-03 — 챕터 + 섹션 구조 (`jb-book`)**

```yaml
format: jb-book
root: intro

parts:
  - caption: "chapter-01. 환경 설정"
    chapters:
      - file: contents/doc-01-setup
        sections:
          - file: contents/git-01-setup-https
          - file: contents/git-02-setup-ssh

  - caption: "chapter-02. 마크다운 예제"
    chapters:
      - file: contents/doc-02-section
      - file: contents/doc-03-chapter

  - caption: "chapter-03. 활용"
    chapters:
      - file: contents/doc-04-new-project

  - caption: "chapter-04. 노트북 예제"
    chapters:
      - file: contents/notebooks/nb-01-signals
```

### 사이드바 결과 비교

**섹션 구조 (jb-article)**

```
├── 환경 설정 및 프로젝트 생성
│   ├── GitHub 연동 (HTTPS 방식)
│   └── GitHub 연동 (SSH 방식)
├── 문서 튜토리얼 (섹션 구조)
├── 북 튜토리얼 (챕터와 섹션 구조)
├── 새 Jupyter Book 프로젝트 생성
└── [예제] 신호 생성 및 시각화
```

**챕터 + 섹션 구조 (jb-book)**

```
├── chapter-01. 환경 설정
│   └── 환경 설정 및 프로젝트 생성
│       ├── GitHub 연동 (HTTPS 방식)
│       └── GitHub 연동 (SSH 방식)
├── chapter-02. 마크다운 예제
│   ├── 문서 튜토리얼 (섹션 구조)
│   └── 북 튜토리얼 (챕터와 섹션 구조)
├── chapter-03. 활용
│   └── 새 Jupyter Book 프로젝트 생성
└── chapter-04. 노트북 예제
    └── [예제] 신호 생성 및 시각화
```

---

## 폴더 구조 변경점

### doc-02 와의 차이

폴더 구조는 doc-02 와 동일합니다.
챕터 구분은 `_toc.yml` 의 `parts` 설정으로만 이루어지며,
별도의 챕터별 하위 폴더를 만들 필요가 없습니다.

> 문서 파일이 많아지면 챕터별 하위 폴더로 분리하는 것이 관리에 유리합니다.
> 이 튜토리얼에서는 파일 수가 적으므로 단일 `contents/` 폴더를 유지합니다.

---

## _config.yml 변경점

### doc-02 와 동일한 항목

```yaml
title: "Jupyter Book 튜토리얼"
author: "nyx7zen"
execute:
  execute_notebooks: "off"
kernelspec:
  name: pytorch_env
html:
  use_repository_button: true
  use_issues_button: true
```

### 변경 항목

`repository.path_to_book` 은 동일하게 `docs` 로 유지합니다.

```yaml
repository:
  url: https://github.com/<username>/myrepo
  branch: main
  path_to_book: docs
```

`_config.yml` 전체는 doc-02 와 동일합니다. 변경 없이 그대로 사용합니다.

---

## _toc.yml 변경점

### _toc.yml 주요 키워드

`format: jb-book` 에서 사용하는 키워드는 아래와 같습니다.

| 키워드 | 역할 |
|--------|------|
| `root` | 첫 페이지 파일 지정 (필수) |
| `parts` | 챕터 그룹 지정. `caption` 으로 챕터 제목 설정 |
| `chapters` | `parts` 안의 문서 목록 |
| `sections` | 특정 파일의 하위 문서 목록 |

구조별 format 비교:

| format | 구조 | 키워드 |
|--------|------|--------|
| `jb-article` (doc-02) | 섹션만 | `root` + `sections` |
| `jb-book` (이 문서) | 챕터 + 섹션 | `root` + `parts` + `chapters` |

### parts / chapters / sections 계층 구조 설명

| 키 | 역할 |
|----|------|
| `parts` | 최상위 챕터 그룹. `caption` 으로 챕터 제목 지정 |
| `chapters` | `parts` 안의 문서 목록 |
| `sections` | `chapters` 안의 하위 문서 목록 |

계층 구조:

```
parts
└── caption (챕터 제목)
    └── chapters (문서 목록)
        └── file (문서 파일)
            └── sections (하위 문서 목록)
                └── file (하위 문서 파일)
```

### 예제 _toc.yml 전체

`docs/_toc.yml` 을 아래 내용으로 교체합니다.

```yaml
format: jb-book
root: intro

parts:
  - caption: "chapter-01. 환경 설정"
    chapters:
      - file: contents/doc-01-setup
        sections:
          - file: contents/git-01-setup-https
          - file: contents/git-02-setup-ssh

  - caption: "chapter-02. 마크다운 예제"
    chapters:
      - file: contents/doc-02-section
      - file: contents/doc-03-chapter

  - caption: "chapter-03. 활용"
    chapters:
      - file: contents/doc-04-new-project

  - caption: "chapter-04. 노트북 예제"
    chapters:
      - file: contents/notebooks/nb-01-signals
```

### 자동 넘버링 (numbered)

`numbered: true` 를 각 `parts` 항목에 추가하면 사이드바와 페이지 제목에 자동으로 번호가 붙습니다.

```yaml
format: jb-book
root: intro

parts:
  - caption: "chapter-01. 환경 설정"
    numbered: true
    chapters:
      - file: contents/doc-01-setup
        sections:
          - file: contents/git-01-setup-https
          - file: contents/git-02-setup-ssh

  - caption: "chapter-02. 마크다운 예제"
    numbered: true
    chapters:
      - file: contents/doc-02-section
      - file: contents/doc-03-chapter

  - caption: "chapter-03. 활용"
    numbered: true
    chapters:
      - file: contents/doc-04-new-project

  - caption: "chapter-04. 노트북 예제"
    numbered: true
    chapters:
      - file: contents/notebooks/nb-01-signals
```

적용 결과 (사이드바):

```
chapter-01. 환경 설정
  1. 환경 설정 및 프로젝트 생성
     1.1 GitHub 연동 (HTTPS 방식)
     1.2 GitHub 연동 (SSH 방식)
chapter-02. 마크다운 예제
  2. 문서 튜토리얼 (섹션 구조)
  3. 북 튜토리얼 (챕터와 섹션 구조)
chapter-03. 활용
  4. 새 Jupyter Book 프로젝트 생성
chapter-04. 노트북 예제
  5. [예제] 신호 생성 및 시각화
```

| 항목 | 설명 |
|------|------|
| 적용 범위 | 사이드바 + 페이지 `#` 제목 |
| 마크다운 수정 불필요 | `.md` 파일의 `##`, `###` 수동 번호 제거 후 자동 적용 |
| `##` 이하 헤딩 | 페이지 내 `##`, `###` 에는 적용되지 않음 |

---

## 로컬 빌드 및 확인

doc-02 와 동일합니다. {doc}`doc-02-section` 의 `8. 로컬 빌드 및 확인` 을 참고하세요.

> **빌드 오류 시:** `EISDIR` 오류가 발생하면 v2 가 설치된 것입니다. `pip install jupyter-book==1.0.4` 로 재설치합니다.

---

## GitHub push 및 배포 확인

doc-02 와 동일합니다. {doc}`doc-02-section` 의 `9. GitHub push 및 배포 확인` 을 참고하세요.
