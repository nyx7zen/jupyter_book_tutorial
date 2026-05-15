# 소개

이 튜토리얼은 **Jupyter Book v1** 을 이용하여
마크다운 문서와 Jupyter 노트북을 GitHub Pages 에 배포하는 방법을 설명합니다.

## 대상 환경

| 환경 | 구성 |
|------|------|
| Windows | WinPython |
| Linux | WSL + Anaconda |

## 주요 내용

- `_config.yml` / `_toc.yml` 설정
- 섹션 구조 문서 작성 (`jb-article`)
- 챕터 + 섹션 구조 문서 작성 (`jb-book`)
- GitHub Actions 를 이용한 자동 배포
- 새 프로젝트 시작 방법

## 문서 구성

| 문서 | 내용 |
|------|------|
| 환경 설정 및 프로젝트 생성 | 설치, 폴더 구조, GitHub 연동 |
| 문서 튜토리얼 (섹션 구조) | `jb-article` 기반 문서 작성 |
| 북 튜토리얼 (챕터와 섹션 구조) | `jb-book` 기반 문서 작성 |
| 새 Jupyter Book 프로젝트 생성 | 튜토리얼 구조를 복사하여 새 프로젝트 시작 |
| [예제] 신호 생성 및 시각화 | NumPy / Matplotlib 예제 노트북 |

## 환경

| 항목 | 내용 |
|------|------|
| Jupyter Book | v1.0.4 |
| Python | 3.11 |
| GitHub Actions | 자동 빌드 및 배포 |