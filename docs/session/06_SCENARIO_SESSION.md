# Grandia III 한국어화 — 시나리오 세션

## 범위

```text
스토리 대사
NPC 대사
이벤트 대사
scene/event text
화자 정보
제어코드
```

## 위치 가설

기존 분석과 선행연구상:

```text
DATA/*.MDZ
```

가 주요 시나리오/scene resource 후보이다.

단, 실제 파일/구조는 기존 분석과 바이너리로 검증한다.

## 중요 원칙

시나리오는:

```text
추출
→ 전체 전문 번역
→ 문맥 검수
→ 용어 통일
```

을 먼저 수행한다.

게임에 한 줄씩 바로 삽입하지 않는다.

목적은 전체 번역 완료 후 필요한 한글 음절을 한 번에 집계하기 위해서다.

## ID 규칙

가능하면 scene/file과 문자열 순번이 고정적으로 드러나는 ID를 사용한다.

예:

```text
SCN_D0123_0001
SCN_D0123_0002
SCN_D0456_0037
```

speaker가 있으면 별도 컬럼에 보관한다.

## 출력

```text
exports/scenario_standard.csv
exports/scenario_required_glyphs.txt
```

## CSV 권장 항목

```text
id
scene_id
source_file
inner_file
string_index
original_offset
pointer_offset
speaker
jp_raw_hex
jp_text
kr_text
control_codes
status
review_note
```

## 번역 품질

직역보다 전체 문맥을 우선한다.

중앙 glossary를 따른다.

시나리오 전문 번역이 끝날 때까지:
- 최종 한글 code table 확정 금지
- 폰트 전체 확장 금지

## 완료 기준

- 전체 시나리오 원문 export
- 전문 번역
- 검수 상태 관리
- 전체 required glyph 목록 생성
- 중앙 세션 제출

> **Workspace storage rule:** Treat `legacy/` as read-only reference/history. Do not create or modify active work products there. Save current work and generated outputs under the project root, such as `build/`, `data/`, `exports/`, or `tools/`.
