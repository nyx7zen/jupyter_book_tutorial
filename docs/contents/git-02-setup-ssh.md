# GitHub 연동 - SSH 방식

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

# 설정 확인
git config --list --global
```

---

## 3. 기존 SSH 키 확인

### Windows

```bash
# Git Bash 에서 확인
# 실제 경로: C:\Users\<사용자명>\.ssh\
ls -al ~/.ssh

# 아래 파일이 있으면 기존 키 존재
# id_ed25519      (개인키)
# id_ed25519.pub  (공개키)

# 로컬 키 fingerprint 확인
ssh-add -l -E sha256
```

- GitHub 등록 키 확인: GitHub 로그인 → Settings → SSH and GPG keys

### WSL

```bash
# WSL 터미널에서 확인
# 실제 경로: /home/<사용자명>/.ssh/
ls -al ~/.ssh

# 아래 파일이 있으면 기존 키 존재
# id_ed25519      (개인키)
# id_ed25519.pub  (공개키)

# 로컬 키 fingerprint 확인
ssh-add -l -E sha256
```

- GitHub 등록 키 확인: GitHub 로그인 → Settings → SSH and GPG keys

> Windows 와 WSL 의 `.ssh` 폴더는 별개입니다. 각 환경에서 SSH 키를 각각 생성해야 합니다.

---

## 4. SSH 키 생성

### Windows

```bash
# account1 SSH 키 생성 (Git Bash)
ssh-keygen -t ed25519 -C "<account1 이메일>" -f ~/.ssh/id_ed25519_account1_win

# account2 SSH 키 생성 (Git Bash)
ssh-keygen -t ed25519 -C "<account2 이메일>" -f ~/.ssh/id_ed25519_account2_win

# 생성된 키 확인
ls -al ~/.ssh

# 각 공개키 내용 확인 (GitHub 에 등록할 내용)
cat ~/.ssh/id_ed25519_account1_win.pub
cat ~/.ssh/id_ed25519_account2_win.pub
```

### WSL

```bash
# account1 SSH 키 생성
ssh-keygen -t ed25519 -C "<account1 이메일>" -f ~/.ssh/id_ed25519_account1_wsl

# account2 SSH 키 생성
ssh-keygen -t ed25519 -C "<account2 이메일>" -f ~/.ssh/id_ed25519_account2_wsl

# 생성된 키 확인
ls -al ~/.ssh

# 각 공개키 내용 확인 (GitHub 에 등록할 내용)
cat ~/.ssh/id_ed25519_account1_wsl.pub
cat ~/.ssh/id_ed25519_account2_wsl.pub
```

---

## 5. GitHub 에 공개키 등록

### Windows

**account1 공개키 등록**
- account1 GitHub 로그인 → Settings → SSH and GPG keys
- New SSH key 클릭
- Title: `account1-windows` 입력
- Key: `cat ~/.ssh/id_ed25519_account1_win.pub` 내용 붙여넣기
- Add SSH key 클릭

**account2 공개키 등록**
- account2 GitHub 로그인 → Settings → SSH and GPG keys
- New SSH key 클릭
- Title: `account2-windows` 입력
- Key: `cat ~/.ssh/id_ed25519_account2_win.pub` 내용 붙여넣기
- Add SSH key 클릭

### WSL

**account1 공개키 등록**
- account1 GitHub 로그인 → Settings → SSH and GPG keys
- New SSH key 클릭
- Title: `account1-wsl` 입력
- Key: `cat ~/.ssh/id_ed25519_account1_wsl.pub` 내용 붙여넣기
- Add SSH key 클릭

**account2 공개키 등록**
- account2 GitHub 로그인 → Settings → SSH and GPG keys
- New SSH key 클릭
- Title: `account2-wsl` 입력
- Key: `cat ~/.ssh/id_ed25519_account2_wsl.pub` 내용 붙여넣기
- Add SSH key 클릭

---

## 6. ~/.ssh/config 파일 작성

### Windows (Git Bash)

```bash
# C:\Users\<사용자명>\.ssh\config 파일 작성
Host github-account1
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_account1_win

Host github-account2
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_account2_win
```

### WSL

```bash
# ~/.ssh/config 파일 작성
Host github-account1
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_account1_wsl

Host github-account2
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_account2_wsl
```

---

## 7. 연결 확인

```bash
# account1 연결 확인
ssh -T git@github-account1
# Hi account1! You've successfully authenticated.

# account2 연결 확인
ssh -T git@github-account2
# Hi account2! You've successfully authenticated.
```

---

## 8. account1 repo 연결

```bash
# account1 repo remote 연결
git remote add origin git@github-account1:<account1>/<repo>.git

# 해당 repo 폴더 안에서 사용자 정보 설정
git config user.name "<account1 사용자명>"
git config user.email "<account1 이메일>"

# 설정 확인
git config --list --local
```

---

## 9. account2 로 전환 (account2 repo 작업 시)

```bash
# account2 repo remote 연결
git remote add origin git@github-account2:<account2>/<repo>.git

# 해당 repo 폴더 안에서 사용자 정보 설정
git config user.name "<account2 사용자명>"
git config user.email "<account2 이메일>"

# 설정 확인
git config --list --local
```

---

## 10. account1 으로 전환 (account1 repo 작업 시)

```bash
# account1 repo remote 연결
git remote add origin git@github-account1:<account1>/<repo>.git

# 해당 repo 폴더 안에서 사용자 정보 설정
git config user.name "<account1 사용자명>"
git config user.email "<account1 이메일>"

# 설정 확인
git config --list --local
```
