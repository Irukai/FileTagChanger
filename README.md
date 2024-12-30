# FileTagChanger (FTG)

FTG는 특정 디렉토리에 존재하는 모든 폴더의 폴더명에 태그를 넣을 때, 일괄적으로 생성, 삭제, 수정 할 수 있는 프로그램입니다.

⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ 
# ${\textsf{\color{red} 본 프로그램은 아직 개발 도중 단계입니다. 본 프로그램을 사용해서 발생하는 모든 결과에 대한 책임은 이용자 본인에게 있습니다.}}$
# ${\textsf{\color{red} 아직 되돌리기 기능이 존재하지 않습니다. 주의해서 사용해주세요.}}$

## 주요 기능

- **태그 생성**: 지정된 디렉토리 내 모든 폴더 이름 앞에 원하는 태그를 추가합니다.
- **태그 제거**: 폴더 이름에서 기존 태그를 제거합니다. 지원되는 태그 형식은 `[]` 및 `()`입니다.
- **태그 수정**: 기존 태그를 새로운 태그로 변경합니다.
- **충돌 처리**: 태그 제거 후 이름 충돌이 발생하면 자동으로 고유한 이름을 생성합니다.

## 사용 방법

1. FileTagChanger.exe 파일을 다운받아서 실행합니다.

### 메뉴 옵션
스크립트를 실행하면 다음과 같은 메뉴를 볼 수 있습니다:

1. **태그 생성**: 폴더 이름 앞에 추가할 태그를 입력받아 적용합니다 (예: `[tag]`).
2. **태그 제거**: 폴더 이름에서 기존 태그를 제거합니다.
3. **태그 수정**: 기존 태그를 새로운 태그로 교체합니다.
4. **종료**: 프로그램을 종료합니다.

### 예시

1. 태그 추가:
   - 대상 디렉토리 경로를 입력합니다.
   - 옵션 `1`을 선택합니다.
   - 추가할 태그를 입력합니다 (예: `[Project]`).

   **결과**: `Folder1`이라는 폴더가 `[Project]Folder1`으로 이름이 변경됩니다.

2. 태그 제거:
   - 대상 디렉토리 경로를 입력합니다.
   - 옵션 `2`를 선택합니다.

   **결과**: `[Project]Folder1`이라는 폴더가 `Folder1`으로 이름이 변경됩니다.

3. 태그 수정:
   - 대상 디렉토리 경로를 입력합니다.
   - 옵션 `3`을 선택합니다.
   - 기존 태그 (예: `[Project]`)와 새로운 태그 (예: `[Updated]`)를 입력합니다.

   **결과**: `[Project]Folder1`이라는 폴더가 `[Updated]Folder1`으로 이름이 변경됩니다.

### 오류 처리

- 태그 제거 후 이름 충돌이 발생하면 숫자 접미사를 추가하여 고유한 이름을 생성합니다 (예: `Folder1 (1)`).
- 지정된 디렉토리가 유효하지 않은 경우, 오류 메시지가 표시됩니다.

## 라이선스

이 스크립트는 오픈 소스이며 자유롭게 사용할 수 있습니다.

