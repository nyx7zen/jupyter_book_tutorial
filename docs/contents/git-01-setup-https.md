# git-01. GitHub 연동 - HTTPS + PAT 방식

## 1. Git 설치

### Windows

- https://git-scm.com/download/win 접속
- 다운로드 및 설치 (기본 옵션으로 진행)

```bash
# 설치 확인
git --version
```

### WSL

```bash
# WSL 에서 Git 설치
sudo apt update
sudo apt install git

# 설치 확인
git --version
```

---

## 2. Git 전역 설정 (최초 1회)

### Windows

```bash
# 사용자 정보 (account1 기본)
git config --global user.name "<account1 사용자명>"
git config --global user.email "<account1 이메일>"

# 기본 브랜치
git config --global init.defaultBranch main

# 줄바꿈 처리 (Windows)
git config --global core.autocrlf true

# 기본 에디터 (VSCode)
git config --global core.editor "code --wait"

# 자격증명 관리자
git config --global credential.helper manager

# 설정 확인
git config --list --global
```

### WSL

```bash
# 사용자 정보 (account1 기본)
git config --global user.name "<account1 사용자명>"
git config --global user.email "<account1 이메일>"

# 기본 브랜치
git config --global init.defaultBranch main

# 줄바꿈 처리 (WSL)
git config --global core.autocrlf input

# 기본 에디터 (VSCode)
git config --global core.editor "code --wait"

# 자격증명 관리자 (Windows 자격증명 관리자 연동)
git config --global credential.helper "/mnt/c/Program\ Files/Git/mingw64/bin/git-credential-manager.exe"

# 설정 확인
git config --list --global
```

> WSL 에서 Windows 자격증명 관리자를 연동하면 Windows 와 WSL 이 동일한 자격증명을 공유합니다.
> 계정 전환 시 Windows 자격증명 관리자에서 한 번만 변경하면 Windows / WSL 양쪽 모두 적용됩니다.

---

## 3. 기존 자격증명 확인 및 제거

```bash
# 자격증명 관리자 바로 실행 (Win + R)
control /name Microsoft.CredentialManager
```

- Windows 자격증명 탭 클릭
- `git:https://github.com` 항목 확인
- 항목 클릭 → 제거

```bash
# 명령어로 자격증명 제거
git credential-manager reject https://github.com
```

---

## 4. PAT 발급

### account1 PAT 발급

- account1 GitHub 로그인 → Settings → Developer settings
- Personal access tokens → Tokens (classic) → Generate new token
- Note: `account1-pat` 입력
- Expiration: No expiration 선택
- repo 권한 체크 → Generate token → 토큰 복사 후 저장

### account2 PAT 발급

- account2 GitHub 로그인 → Settings → Developer settings
- Personal access tokens → Tokens (classic) → Generate new token
- Note: `account2-pat` 입력
- Expiration: No expiration 선택
- repo 권한 체크 → Generate token → 토큰 복사 후 저장

> PAT은 발급 시 한 번만 표시되므로 반드시 메모장 등에 저장

---

## 5. account1 으로 등록

```bash
# 자격증명 관리자 바로 실행 (Win + R)
control /name Microsoft.CredentialManager
```

- Windows 자격증명 탭 클릭
- Windows 자격증명 추가 클릭
- 인터넷 또는 네트워크 주소: `git:https://github.com`
- 사용자 이름: `<account1 사용자명>`
- 암호: `<account1 PAT>`
- 확인 클릭

```bash
# 연결 확인
git ls-remote https://github.com/<account1>/<repo>.git
```

---

## 6. account2 로 전환

```bash
# 자격증명 관리자 바로 실행 (Win + R)
control /name Microsoft.CredentialManager
```

- Windows 자격증명 탭 클릭
- `git:https://github.com` 항목 클릭 → 편집
- 사용자 이름: `<account2 사용자명>`
- 암호: `<account2 PAT>`
- 저장 클릭

```bash
# 해당 repo 폴더 안에서 사용자 정보 변경
git config user.name "<account2 사용자명>"
git config user.email "<account2 이메일>"

# 설정 확인
git config --list --local
```

---

## 7. account1 으로 전환

```bash
# 자격증명 관리자 바로 실행 (Win + R)
control /name Microsoft.CredentialManager
```

- Windows 자격증명 탭 클릭
- `git:https://github.com` 항목 클릭 → 편집
- 사용자 이름: `<account1 사용자명>`
- 암호: `<account1 PAT>`
- 저장 클릭

```bash
# 해당 repo 폴더 안에서 사용자 정보 변경
git config user.name "<account1 사용자명>"
git config user.email "<account1 이메일>"

# 설정 확인
git config --list --local
```
