# 문서 튜토리얼 (섹션 구조)

## 개요

### 이 문서의 목적

섹션만으로 구성된 Jupyter Book 문서를 처음부터 완성까지 작성하는 방법을 설명합니다.
챕터 없이 섹션만 나열하는 구조로, 단순하고 작은 규모의 문서에 적합합니다.

챕터 + 섹션 구조는 {doc}`doc-03-chapter` 를 참고하세요.

> 이 튜토리얼은 **Jupyter Book v1 (1.0.4)** 기준으로 작성되었습니다.
> 버전 설치 및 v1/v2 차이점은 {doc}`doc-01-setup` 을 참고하세요.

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

완성된 사이드바 구조:

```
Jupyter Book 튜토리얼
├── 소개
├── 환경 설정 및 프로젝트 생성
│   ├── GitHub 연동 (HTTPS 방식)
│   └── GitHub 연동 (SSH 방식)
├── 문서 튜토리얼 (섹션 구조)
├── 북 튜토리얼 (챕터와 섹션 구조)
├── 새 Jupyter Book 프로젝트 생성
└── [예제] 신호 생성 및 시각화
```

---

## _config.yml 작성

### _config.yml 역할

Jupyter Book 전체의 설정을 담당합니다. 제목, 저자, 실행 방식, GitHub 연동 등을 지정합니다.

### 주요 설정 항목 설명

| 항목 | 설명 |
|------|------|
| `title` | 책 제목 |
| `author` | 저자명 |
| `execute.execute_notebooks` | 빌드 시 노트북 재실행 여부 |
| `kernelspec.name` | 노트북 커널 이름 |
| `repository.url` | GitHub 레포 URL |
| `repository.path_to_book` | 레포 루트 기준 book 폴더 경로 |
| `html.use_repository_button` | 페이지마다 GitHub 링크 버튼 표시 여부 |

### 예제 _config.yml 전체

`docs/_config.yml` 파일을 생성합니다.

```yaml
title: "Jupyter Book 튜토리얼"
author: "nyx7zen"
logo: ""

execute:
  execute_notebooks: "off"

kernelspec:
  name: pytorch_env

repository:
  url: https://github.com/<username>/myrepo
  branch: main
  path_to_book: docs

html:
  use_repository_button: true
  use_issues_button: true
```

> `execute_notebooks: "off"` 로 설정하면 빌드 시 노트북을 재실행하지 않습니다.
> 노트북은 로컬에서 미리 실행 후 출력을 저장한 상태로 push 합니다.

---

## _toc.yml 작성

### _toc.yml 역할

사이드바에 표시되는 문서 목차 구조를 정의합니다.
등록된 순서대로 사이드바에 나타납니다.

### _toc.yml 주요 키워드

`format: jb-article` 에서 사용하는 키워드는 아래와 같습니다.

| 키워드 | 역할 |
|--------|------|
| `root` | 첫 페이지 파일 지정 (필수) |
| `sections` | root 다음에 오는 페이지 목록 |

> `jb-article` 은 `sections:` 키워드만 사용합니다.
> 챕터 없이 섹션만 나열하는 단순한 구조입니다.
> 챕터로 그룹화하려면 `format: jb-book` 을 사용합니다. → {doc}`doc-03-chapter` 참고

구조별 format 비교:

| format | 구조 | 키워드 |
|--------|------|--------|
| `jb-article` (이 문서) | 섹션만 | `root` + `sections` |
| `jb-book` | 챕터 + 섹션 | `root` + `parts` + `chapters` |

### 섹션 구조 개념

`jb-article` 은 챕터 없이 파일을 직접 나열합니다.

```
root (intro.md)
├── 환경 설정 및 프로젝트 생성 (doc-01-setup.md)
│   ├── GitHub 연동 (HTTPS 방식) (git-01-setup-https.md)
│   └── GitHub 연동 (SSH 방식) (git-02-setup-ssh.md)
├── 문서 튜토리얼 (섹션 구조) (doc-02-section.md)
├── 북 튜토리얼 (챕터와 섹션 구조) (doc-03-chapter.md)
├── 새 Jupyter Book 프로젝트 생성 (doc-04-new-project.md)
└── [예제] 신호 생성 및 시각화 (notebooks/nb-01-signals.ipynb)
```

### 예제 _toc.yml 전체

`docs/_toc.yml` 파일을 생성합니다.

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

### 섹션 등록 방법 상세

- `root` 는 첫 페이지로 표시될 파일을 지정합니다. 확장자 `.md` 는 생략합니다.
- `sections` 아래에 `file` 로 각 문서를 등록합니다.
- 경로는 `docs/` 를 기준으로 작성합니다.
- `.md` 와 `.ipynb` 모두 확장자를 생략합니다.

### 자동 넘버링 (numbered)

`options: numbered: true` 를 추가하면 사이드바와 페이지 제목에 자동으로 번호가 붙습니다.

```yaml
format: jb-article
root: intro

options:
  numbered: true

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

적용 결과 (사이드바):

```
1. 환경 설정 및 프로젝트 생성
   1.1 GitHub 연동 (HTTPS 방식)
   1.2 GitHub 연동 (SSH 방식)
2. 문서 튜토리얼 (섹션 구조)
3. 북 튜토리얼 (챕터와 섹션 구조)
4. 새 Jupyter Book 프로젝트 생성
5. [예제] 신호 생성 및 시각화
```

| 항목 | 설명 |
|------|------|
| 적용 범위 | 사이드바 + 페이지 `#` 제목 |
| 마크다운 수정 불필요 | `.md` 파일의 `##`, `###` 수동 번호는 그대로 유지 |
| `##` 이하 헤딩 | 페이지 내 `##`, `###` 에는 적용되지 않음 |

---

## intro.md 작성

### 역할

Jupyter Book 의 첫 페이지입니다. `_toc.yml` 의 `root` 에 지정된 파일입니다.

### 예제 intro.md 전체

`docs/intro.md` 파일을 생성합니다.

```markdown
# Jupyter Book 튜토리얼

이 문서는 Jupyter Book 을 이용한 문서 작성 방법을 설명합니다.

## 대상 환경

- Windows + WinPython
- WSL + Anaconda

## 문서 구성

- 환경 설정 및 프로젝트 생성
- 문서 튜토리얼 (섹션 구조)
- 북 튜토리얼 (챕터와 섹션 구조)
- 새 Jupyter Book 프로젝트 생성
- [예제] 신호 생성 및 시각화
```

---

## src 코드 작성

노트북에서 import 할 Python 코드를 먼저 작성합니다.

### __init__.py

`src/__init__.py` 파일을 생성합니다. 내용은 비워도 됩니다.

```python
# src/__init__.py
```

`__init__.py` 의 역할:

- 해당 폴더가 Python 패키지임을 Python 인터프리터에게 알려주는 파일입니다.
- 이 파일이 없으면 `from src.signals import ...` 와 같은 import 가 동작하지 않습니다.
- 내용은 비워도 되며, 패키지 수준의 초기화 코드가 필요한 경우에만 내용을 추가합니다.

### signals.py

`src/signals.py` 파일을 생성합니다.

```python
import numpy as np


def generate_sine(freq: float = 1.0, samples: int = 200, duration: float = 1.0):
    """사인파 생성

    Args:
        freq: 주파수 (Hz)
        samples: 샘플 수
        duration: 시간 길이 (초)

    Returns:
        x: 시간축 배열
        y: 사인파 배열
    """
    x = np.linspace(0, duration, samples)
    y = np.sin(2 * np.pi * freq * x)
    return x, y


def generate_cosine(freq: float = 1.0, samples: int = 200, duration: float = 1.0):
    """코사인파 생성

    Args:
        freq: 주파수 (Hz)
        samples: 샘플 수
        duration: 시간 길이 (초)

    Returns:
        x: 시간축 배열
        y: 코사인파 배열
    """
    x = np.linspace(0, duration, samples)
    y = np.cos(2 * np.pi * freq * x)
    return x, y


def add_noise(y: np.ndarray, std: float = 0.1):
    """가우시안 노이즈 추가

    Args:
        y: 입력 신호 배열
        std: 노이즈 표준편차

    Returns:
        y_noisy: 노이즈가 추가된 신호 배열
    """
    noise = np.random.normal(0, std, size=y.shape)
    return y + noise


def generate_composite(freq1: float = 1.0, freq2: float = 3.0,
                        samples: int = 200, duration: float = 1.0):
    """사인파 + 코사인파 합성파 생성

    Args:
        freq1: 사인파 주파수 (Hz)
        freq2: 코사인파 주파수 (Hz)
        samples: 샘플 수
        duration: 시간 길이 (초)

    Returns:
        x: 시간축 배열
        y: 합성파 배열
    """
    x = np.linspace(0, duration, samples)
    y = np.sin(2 * np.pi * freq1 * x) + np.cos(2 * np.pi * freq2 * x)
    return x, y
```

### plotter.py

`src/plotter.py` 파일을 생성합니다.

```python
import matplotlib.pyplot as plt
import numpy as np


def plot_signal(x: np.ndarray, y: np.ndarray, title: str = "Signal"):
    """단일 신호 플롯

    Args:
        x: 시간축 배열
        y: 신호 배열
        title: 그래프 제목
    """
    fig, ax = plt.subplots(figsize=(8, 3))
    ax.plot(x, y, color="steelblue", linewidth=1.5)
    ax.set_title(title)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")
    ax.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()


def plot_multiple(x: np.ndarray, signals: list, labels: list,
                  title: str = "Signals"):
    """여러 신호 비교 플롯

    Args:
        x: 시간축 배열
        signals: 신호 배열 리스트
        labels: 각 신호의 레이블 리스트
        title: 그래프 제목
    """
    fig, ax = plt.subplots(figsize=(8, 3))
    colors = ["steelblue", "tomato", "seagreen", "orange"]
    for i, (y, label) in enumerate(zip(signals, labels)):
        ax.plot(x, y, label=label, color=colors[i % len(colors)], linewidth=1.5)
    ax.set_title(title)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()


def plot_with_noise(x: np.ndarray, y_clean: np.ndarray, y_noisy: np.ndarray,
                    title: str = "Signal with Noise"):
    """원본 신호 vs 노이즈 추가 신호 비교 플롯

    Args:
        x: 시간축 배열
        y_clean: 원본 신호 배열
        y_noisy: 노이즈 추가 신호 배열
        title: 그래프 제목
    """
    fig, ax = plt.subplots(figsize=(8, 3))
    ax.plot(x, y_noisy, color="tomato", linewidth=1.0, alpha=0.7, label="Noisy")
    ax.plot(x, y_clean, color="steelblue", linewidth=2.0, label="Clean")
    ax.set_title(title)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()
```

---

## 마크다운 문서 작성

### MyST Markdown 개요

Jupyter Book 은 MyST (Markedly Structured Text) Markdown 을 사용합니다.
일반 Markdown 문법에 수식, callout, 크로스 레퍼런스 등이 추가된 확장 문법입니다.

### 제목 / 본문

```markdown
# 제목 1
## 제목 2
### 제목 3

일반 본문 텍스트입니다.
**굵게**, *기울임*, `인라인 코드`
```

### 수식

인라인 수식:

```markdown
사인파는 $y = \sin(2\pi f t)$ 로 표현됩니다.
```

블록 수식:

```markdown
$$
y = \sin(2\pi f t) + \cos(2\pi f t)
$$
```

### 코드 블록

````markdown
```python
import numpy as np
x = np.linspace(0, 1, 100)
```
````

### callout

```markdown
:::{note}
참고 사항입니다.
:::

:::{warning}
주의 사항입니다.
:::

:::{tip}
유용한 팁입니다.
:::
```

### 크로스 레퍼런스

다른 문서로 링크:

```markdown
{doc}`doc-01-setup` 을 참고하세요.
```

특정 섹션으로 링크:

```markdown
(section-label)=
## 섹션 제목

{ref}`section-label` 을 참고하세요.
```

### 예제 doc1.md 전체

`docs/contents/doc-01-setup.md` 는 {doc}`doc-01-setup` 을 참고하세요.

### 예제 doc2.md 전체

추가 문서가 필요한 경우 `docs/contents/` 아래에 동일한 방식으로 작성합니다.

---

## Jupyter 노트북 작성

### 노트북 파일 위치

```
docs/contents/notebooks/nb-01-signals.ipynb
```

VSCode 에서 해당 경로에 새 파일을 생성합니다.

### src 코드 import 방법

노트북은 `docs/contents/notebooks/` 안에 있으므로
레포 루트의 `src/` 를 찾으려면 경로 설정이 필요합니다.

`setup.py` 로 editable 설치한 경우 경로 설정 없이 바로 import 가능합니다.

```python
# pip install -e . 로 설치한 경우
from src.signals import generate_sine
```

editable 설치가 되어 있지 않은 경우 sys.path 를 사용합니다.

```python
import sys, os
sys.path.insert(0, os.path.abspath("../../../"))
from src.signals import generate_sine
```

### execute_notebooks 설정

`_config.yml` 에서 `execute_notebooks: "off"` 로 설정하면
빌드 시 노트북을 재실행하지 않고 저장된 출력을 그대로 표시합니다.

노트북은 VSCode 에서 실행 후 출력이 포함된 상태로 저장합니다.

```
Shift+Enter    현재 셀 실행
Ctrl+S         저장 (출력 포함)
```

### 노트북 셀 구성

`docs/contents/notebooks/nb-01-signals.ipynb` 를 VSCode 에서 열고
아래 셀 내용을 순서대로 입력합니다.

---

**[markdown 셀]**

```
# [예제] 신호 생성 및 시각화

`src.signals` 와 `src.plotter` 를 import 하여
사인파, 코사인파, 노이즈, 합성파를 생성하고 시각화합니다.
```

---

**[code 셀] - 경로 설정 (첫 번째 코드 셀) — `remove-cell` 태그 적용**

```python
import os
import sys

ROOT_DIR = os.path.normpath(os.path.join(os.getcwd(), "..", "..", ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)
```

이 셀은 노트북 실행 시에만 필요하고 문서에는 표시되지 않아야 하므로 `remove-cell` 태그를 적용합니다.

**VSCode 에서 태그 추가 방법:**

1. VSCode 에서 노트북 열기
2. 경로 설정 셀 우측 상단 `...` 클릭
3. **Add Cell Tag** 클릭
4. `remove-cell` 입력 후 Enter
5. `Ctrl+S` 저장

태그 종류와 효과:

| 태그 | 코드 | 출력 | 용도 |
|------|------|------|------|
| `remove-input` | 숨김 | 표시 | 출력 결과는 보여주고 코드만 숨길 때 |
| `remove-output` | 표시 | 숨김 | 코드는 보여주고 출력만 숨길 때 |
| `remove-cell` | 숨김 | 숨김 | 셀 전체를 완전히 숨길 때 |

태그 적용 후 재빌드:

```bash
jupyter-book clean docs/
jupyter-book build docs/
```

---

**[code 셀]**

```python
from src.signals import generate_sine, generate_cosine
from src.signals import add_noise, generate_composite
from src.plotter import plot_signal, plot_multiple, plot_with_noise
```

---

**[markdown 셀]**

```
## 사인파 / 코사인파 생성

`generate_sine()` 과 `generate_cosine()` 으로 기본 신호를 생성합니다.

$$
y_{\sin} = \sin(2\pi f t), \quad y_{\cos} = \cos(2\pi f t)
$$
```

---

**[code 셀]**

```python
x, y_sin = generate_sine(freq=2.0, samples=200, duration=1.0)
plot_signal(x, y_sin, title="Sine Wave (freq=2Hz)")
```

---

**[code 셀]**

```python
x, y_cos = generate_cosine(freq=2.0, samples=200, duration=1.0)
plot_signal(x, y_cos, title="Cosine Wave (freq=2Hz)")
```

---

**[markdown 셀]**

```
## 노이즈 추가

`add_noise()` 로 가우시안 노이즈를 추가하고 원본과 비교합니다.
```

---

**[code 셀]**

```python
y_noisy = add_noise(y_sin, std=0.2)
plot_with_noise(x, y_sin, y_noisy, title="Sine Wave with Noise (std=0.2)")
```

---

**[markdown 셀]**

```
## 합성파

`generate_composite()` 로 사인파와 코사인파를 합성합니다.

$$
y = \sin(2\pi f_1 t) + \cos(2\pi f_2 t)
$$
```

---

**[code 셀]**

```python
x, y_comp = generate_composite(freq1=1.0, freq2=3.0, samples=200, duration=1.0)
x, y_sin1 = generate_sine(freq=1.0, samples=200, duration=1.0)
x, y_cos3 = generate_cosine(freq=3.0, samples=200, duration=1.0)

plot_multiple(
    x,
    signals=[y_sin1, y_cos3, y_comp],
    labels=["sin (1Hz)", "cos (3Hz)", "composite"],
    title="Composite Signal"
)
```

---

**[markdown 셀]**

```
## 정리

| 함수 | 설명 |
|------|------|
| `generate_sine()` | 사인파 생성 |
| `generate_cosine()` | 코사인파 생성 |
| `add_noise()` | 가우시안 노이즈 추가 |
| `generate_composite()` | 합성파 생성 |
| `plot_signal()` | 단일 신호 플롯 |
| `plot_multiple()` | 여러 신호 비교 플롯 |
| `plot_with_noise()` | 원본 vs 노이즈 비교 플롯 |
```

---

## 로컬 빌드 및 확인

### 빌드 명령어

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

### 빌드 오류 시 대처

```bash
# 캐시 삭제 후 재빌드
jupyter-book clean docs/
jupyter-book build docs/

# 상세 오류 확인
jupyter-book build docs/ --verbose
```

> **v2 설치 오류:** `EISDIR: illegal operation on a directory` 오류가 발생하면 v2 가 설치된 것입니다.
> 아래 명령으로 v1 으로 재설치합니다.
> ```bash
> pip uninstall jupyter-book -y
> pip install jupyter-book==1.0.4
> ```

---

## GitHub push 및 배포 확인

### push 명령어

```bash
git add .
git commit -m "add section tutorial"
git push origin main
```

### GitHub Actions 확인

- GitHub 레포 → Actions 탭
- `Deploy Jupyter Book` 워크플로우 실행 상태 확인
- 초록색 체크 표시가 되면 배포 완료

> **Actions 권한 오류:** `Permission denied` 오류가 발생하면 `deploy.yml` 에 `permissions: contents: write` 가 있는지 확인합니다.

### GitHub Pages 설정 (최초 1회)

Actions 가 성공한 후 GitHub Pages 를 수동으로 활성화해야 합니다.

1. GitHub 레포 → **Settings** 탭
2. 왼쪽 사이드바 → **Pages**
3. Source: `Deploy from a branch` 선택
4. Branch: **`gh-pages`** / **`/ (root)`** 선택
5. **Save** 클릭

### GitHub Pages URL 확인

```
https://<username>.github.io/myrepo/
```

> Save 후 1~2분 기다리면 URL 에서 확인 가능합니다.