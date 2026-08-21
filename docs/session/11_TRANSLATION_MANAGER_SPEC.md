# Grandia III Translation Manager — Python GUI / SQLite 사양

## 목적

한국어화가 진행될수록 수천 개의 문자열을:

```text
시스템
상태/장비
아이템
스킬/마법
전투
시나리오
기타
```

별로 관리하고, 나중에 검수/수정 요청을 쉽게 하기 위한 중앙 관리 프로그램을 만든다.

단순 CSV 뷰어가 아니라 **번역 DB를 프로젝트의 Source of Truth**로 한다.

## 권장 기술

```text
Python
PySide6 또는 CustomTkinter
SQLite
```

DB:

```text
translation.db
```

CSV import/export도 지원한다.

## GUI 탭

```text
시스템
상태/장비
아이템
스킬/마법
전투
시나리오
기타
전체검색
```

## 기본 목록 화면

최소 표시:

```text
코드/ID
일문
번역문
```

권장 추가:

```text
상태
인게임확인
파일
```

예:

```text
ITEM_0107_NAME | やくそう | 약초 | 번역완료 | YES
ITEM_0107_DESC | 怪我や傷... | 상처를... | 1차검수 | NO
```

## 고유 ID 규칙

offset 자체를 ID로 쓰지 않는다.

권장:

```text
SYS_SAVE_0001
STATUS_PARAM_0003
ITEM_0107_NAME
ITEM_0107_DESC
SKILL_0034_NAME
BATTLE_CMD_0012
SCN_D0123_0042
```

물리적 위치는 별도 metadata로 보존한다.

## DB 권장 컬럼

```text
id
category
sub_category

source_file
inner_file
record_id
scene_id
string_index

original_offset
pointer_offset

jp_raw_hex
jp_text

kr_text
kr_encoded_hex

speaker

status
game_verified

translator_note
review_note

created_at
updated_at
```

## 상태값

```text
UNTRANSLATED
TRANSLATED
REVIEW_1
FINAL_REVIEW
INSERTED
GAME_VERIFIED
NEEDS_FIX
```

## 상세 패널

선택 항목은 다음을 보여준다.

```text
ID
Category
Source file
Inner file
Record / Scene
Original offset
Pointer offset

JP Raw
JP Text

KR Text
KR Encoded

Status
Game Verified

Translator Note
Review Note
```

## 검색/필터

검색 대상:

```text
ID
일문
한국어
speaker
scene
note
```

필터:

```text
미번역
번역완료
수정필요
인게임 미확인
특정 파일
특정 scene
```

## 수정 요청 복사 버튼

```text
[수정 요청 복사]
```

클립보드 예:

```text
Grandia III 번역 수정 요청

ID: SCN_D0142_0021
구분: 시나리오
Source: DATA/xxxxxxxx.MDZ
일문: ここから先は危険だ
현재 번역: 이 앞은 위험해
현재 상태: GAME_VERIFIED
수정 요청:
```

사용자는 이 내용을 ChatGPT/Codex에 붙여넣고 해당 ID의 번역 수정만 요청할 수 있다.

## 소스 위치 복사

```text
[소스 위치 복사]
```

예:

```text
ID: ITEM_0107_DESC
Source: SYS/GR3.MDZ
Inner: GR3.MDT
Record: 107
Original offset: 0x....
Pointer offset: 0x....
```

Codex가 같은 문자열을 다시 검색할 필요가 없게 한다.

## 한글 사용 글자 추출

DB 전체 `kr_text`를 분석하여 unique Hangul syllables를 자동 추출한다.

```text
[필요 한글 글자 집계]
```

출력:

```text
korean_required_glyphs.txt
korean_required_glyphs.csv
```

## 빌드 연계

최종적으로:

```text
translation.db
→ category별 문자열 수집
→ Hangul custom encode
→ BIN/MDT patch
→ MDZ pack
→ ISO 대상 파일 replace
→ reverse extraction verify
```

까지 자동화할 수 있게 설계한다.

초기 버전은 DB/검수/수정/검색 기능부터 안정화한다.

## Source of Truth

실제 번역문의 기준은:

```text
translation.db
```

이다.

CSV는 import/export 용도로만 사용한다.

## 백업

DB 변경 시:

```text
backup/translation_YYYYMMDD_HHMMSS.db
```

형태의 자동 백업을 권장한다.

대량 import 직전에도 반드시 백업한다.

> **Workspace storage rule:** Treat `legacy/` as read-only reference/history. Do not create or modify active work products there. Save current work and generated outputs under the project root, such as `build/`, `data/`, `exports/`, or `tools/`.
