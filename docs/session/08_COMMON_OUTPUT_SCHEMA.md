# Grandia III 한국어화 — 공통 출력 Schema / ID 규칙

모든 작업 세션은 이 규격을 따른다.

## 공통 CSV 컬럼

권장 전체 schema:

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
control_codes

status
game_verified

translator_note
review_note
```

## 최소 필수

```text
id
category
source_file
jp_text
kr_text
status
```

가능한 경우 반드시:
- original_offset
- pointer_offset
- jp_raw_hex
- record_id / scene_id

도 보존한다.

## ID 원칙

ID는 변하지 않아야 한다.

hex offset을 ID로 사용하지 않는다.

예:

```text
SYS_MENU_0001
STATUS_PARAM_0001
ITEM_0107_NAME
ITEM_0107_DESC
BATTLE_CMD_0012
SKILL_0034_NAME
SCN_D0123_0042
```

## category 권장값

```text
SYSTEM
STATUS
EQUIPMENT
ITEM
SKILL
MAGIC
BATTLE
SCENARIO
OTHER
```

## status 권장값

```text
UNTRANSLATED
TRANSLATED
REVIEW_1
FINAL_REVIEW
INSERTED
GAME_VERIFIED
NEEDS_FIX
```

## kr_encoded_hex

중앙 `hangul_code_map`이 아직 없는 글자가 포함되면:

```text
UNASSIGNED
```

로 둔다.

세션이 임의로 code를 만들지 않는다.

## required_glyphs.txt

각 세션은 자기 번역의 실제 한글 완성형 음절 unique set을 출력한다.

예:

```text
가
각
간
공
격
약
초
회
복
```

정렬 기준은 코드포인트 순 또는 최초 등장 순 중 하나로 프로젝트 전체에서 통일한다.

## 중앙 제출 전 검사

각 세션은 제출 전에:

```text
ID 중복 없음
빈 jp_text 확인
빈 kr_text 확인
offset 형식 확인
required glyph 재계산
CSV UTF-8
```

검사를 수행한다.

> **Workspace storage rule:** Treat `legacy/` as read-only reference/history. Do not create or modify active work products there. Save current work and generated outputs under the project root, such as `build/`, `data/`, `exports/`, or `tools/`.
