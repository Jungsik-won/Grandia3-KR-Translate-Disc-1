# Grandia III 한국어화 — 시스템 세션

## 범위

이 세션은 다음만 담당한다.

```text
메인 시스템 메뉴
저장 / 불러오기
설정
확인 / 취소
공통 시스템 메시지
기타 고정 UI
```

## 기존 분석 우선

Reference Pack의:
- FIELD.BIN
- SLPM
- system UI
- save/load
관련 기존 분석을 먼저 읽는다.

이미 찾은 구조를 재발견하지 않는다.

## 목표

각 문자열에 고유 ID를 부여하고 표준 CSV로 만든다.

예:

```text
SYS_MENU_0001
SYS_SAVE_0001
SYS_LOAD_0001
SYS_MSG_0012
```

## 출력

```text
exports/system_standard.csv
exports/system_required_glyphs.txt
```

## 필수 컬럼

`08_COMMON_OUTPUT_SCHEMA.md`를 따른다.

최소:

```text
id
category
sub_category
source_file
inner_file
original_offset
pointer_offset
jp_raw_hex
jp_text
kr_text
status
game_verified
```

## 한글 관련 규칙

이 세션은:
- 필요한 한글 글자를 추출한다.
- 중앙 `hangul_code_map.csv`가 이미 있으면 기존 매핑을 사용한다.
- 없는 한글은 `UNASSIGNED`로 표시한다.

독자적으로 신규 한글 code/glyph slot을 배정하지 않는다.

## 완료 기준

- 시스템 원문 목록 정리
- 한국어 번역
- source/offset 메타데이터 확보
- required glyph 목록 생성
- 중앙 세션에 제출

> **Workspace storage rule:** Treat `legacy/` as read-only reference/history. Do not create or modify active work products there. Save current work and generated outputs under the project root, such as `build/`, `data/`, `exports/`, or `tools/`.
