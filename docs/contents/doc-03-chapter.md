# doc-03. 북 튜토리얼 (챕터와 섹션 구조)

## 1. 개요

### 1.1 이 문서의 목적

챕터와 섹션으로 구성된 Jupyter Book 북을 작성하는 방법을 설명합니다.
섹션 구조와의 차이점을 중심으로 설명하며, 동일한 내용은 {doc}`doc-02-section` 을 참고하세요.

> 이 튜토리얼은 **Jupyter Book v1 (1.0.4)** 기준으로 작성되었습니다.
> 버전 설치 및 v1/v2 차이점은 {doc}`doc-01-setup` 을 참고하세요.

### 1.2 doc-02 와의 관계

doc-02 에서 다룬 내용 중 아래 3가지만 다릅니다.

- 폴더 구조 (챕터별 하위 폴더 추가)
- `_toc.yml` 구조 (`parts` / `chapters` / `sections` 계층)
- `_config.yml` 일부 항목

src 코드, 마크다운 문서 작성법, 노트북 작성법, 빌드 및 배포 방법은 doc-02 와 동일합니다.

### 1.3 완성 후 폴더 구조

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

### 1.4 완성 후 사이드바 구조

```
Jupyter Book 튜토리얼
├── 소개
├── chapter-01. 환경 설정
│   └── doc-01. 환경 설정 및 프로젝트 생성
│       ├── git-01. GitHub 연동 (HTTPS 방식)
│       └── git-02. GitHub 연동 (SSH 방식)
├── chapter-02. 마크다운 예제
│   ├── doc-02. 문서 튜토리얼 (섹션 구조)
│   └── doc-03. 북 튜토리얼 (챕터와 섹션 구조)
└── chapter-03. 노트북 예제
    └── nb-01. 신호 생성 및 시각화
```

---

## 2. 섹션 구조 vs 챕터 + 섹션 구조 비교

### 2.1 _toc.yml 구조 비교

**doc-02 — 섹션 구조 (`chapters` 사용)**

```yaml
format: jb-book
root: intro

chapters:
  - file: contents/doc-01-setup
    sections:
      - file: contents/git-01-setup-https
      - file: contents/git-02-setup-ssh
  - file: contents/doc-02-section
  - file: contents/doc-03-chapter
  - file: contents/notebooks/nb-01-signals
```

**doc-03 — 챕터 + 섹션 구조 (`parts` 사용)**

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

  - caption: "chapter-03. 노트북 예제"
    chapters:
      - file: contents/notebooks/nb-01-signals
```

### 2.2 사이드바 결과 비교

**섹션 구조**

```
├── doc-01. 환경 설정 및 프로젝트 생성
│   ├── git-01. GitHub 연동 (HTTPS 방식)
│   └── git-02. GitHub 연동 (SSH 방식)
├── doc-02. 문서 튜토리얼 (섹션 구조)
├── doc-03. 북 튜토리얼 (챕터와 섹션 구조)
└── nb-01. 신호 생성 및 시각화
```

**챕터 + 섹션 구조**

```
├── chapter-01. 환경 설정
│   └── doc-01. 환경 설정 및 프로젝트 생성
│       ├── git-01. GitHub 연동 (HTTPS 방식)
│       └── git-02. GitHub 연동 (SSH 방식)
├── chapter-02. 마크다운 예제
│   ├── doc-02. 문서 튜토리얼 (섹션 구조)
│   └── doc-03. 북 튜토리얼 (챕터와 섹션 구조)
└── chapter-03. 노트북 예제
    └── nb-01. 신호 생성 및 시각화
```

---

## 3. 폴더 구조 변경점

### 3.1 doc-02 와의 차이

폴더 구조는 doc-02 와 동일합니다.
챕터 구분은 `_toc.yml` 의 `parts` 설정으로만 이루어지며,
별도의 챕터별 하위 폴더를 만들 필요가 없습니다.

> 문서 파일이 많아지면 챕터별 하위 폴더로 분리하는 것이 관리에 유리합니다.
> 이 튜토리얼에서는 파일 수가 적으므로 단일 `contents/` 폴더를 유지합니다.

---

## 4. _config.yml 변경점

### 4.1 doc-02 와 동일한 항목

```yaml
title: "Jupyter Book 튜토리얼"
author: "Nam"
execute:
  execute_notebooks: "off"
kernelspec:
  name: pytorch_env
html:
  use_repository_button: true
  use_issues_button: true
```

### 4.2 변경 항목

`repository.path_to_book` 은 동일하게 `docs` 로 유지합니다.

```yaml
repository:
  url: https://github.com/<username>/myrepo
  branch: main
  path_to_book: docs
```

`_config.yml` 전체는 doc-02 와 동일합니다. 변경 없이 그대로 사용합니다.

---

## 5. _toc.yml 변경점

### 5.1 _toc.yml 주요 키워드

`format: jb-book` 에서 사용하는 키워드는 아래와 같습니다.

| 키워드 | 역할 |
|--------|------|
| `root` | 첫 페이지 파일 지정 (필수) |
| `chapters` | root 다음에 오는 페이지 목록 (필수 키워드) |
| `parts` | 챕터 그룹 지정. `caption` 으로 챕터 제목 설정 |
| `sections` | 특정 파일의 하위 페이지 목록 |

> `chapters` 는 "챕터 구조"를 의미하는 것이 아닙니다.
> `format: jb-book` 에서 페이지 목록을 나열할 때 반드시 필요한 필수 키워드입니다.
> 챕터로 그룹화하려면 `chapters` 대신 `parts` 를 사용합니다.

구조별 키워드 사용:

| 구조 | 키워드 |
|------|--------|
| 섹션만 (doc-02) | `root` + `chapters` |
| 챕터 + 섹션 (이 문서) | `root` + `parts` + `chapters` |
| 파일 하위 구조 | `sections` |

### 5.2 parts / chapters / sections 계층 구조 설명

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

### 5.3 예제 _toc.yml 전체

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

  - caption: "chapter-03. 노트북 예제"
    chapters:
      - file: contents/notebooks/nb-01-signals
```

---

## 6. 로컬 빌드 및 확인

doc-02 와 동일합니다. {doc}`doc-02-section` 의 `8. 로컬 빌드 및 확인` 을 참고하세요.

> **빌드 오류 시:** `EISDIR` 오류가 발생하면 v2 가 설치된 것입니다. `pip install jupyter-book==1.0.4` 로 재설치합니다.

---

## 7. GitHub push 및 배포 확인

doc-02 와 동일합니다. {doc}`doc-02-section` 의 `9. GitHub push 및 배포 확인` 을 참고하세요.
