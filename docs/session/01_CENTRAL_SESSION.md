# Grandia III 한국어화 — 중앙 관리 세션

## 역할

이 세션은 실제 리버싱을 모든 영역에서 직접 수행하는 세션이 아니다.

주요 역할은:
- 공통 데이터 규격 관리
- Translation Manager 관리
- 각 세션 결과 merge
- ID 충돌 검사
- 용어집 관리
- 전체 한글 사용 문자 집계
- 미사용 일본어 glyph slot 관리
- 최종 한글 code/glyph table 관리
- 최종 폰트 bitmap 생성
- 최종 build pipeline 관리

이다.

## 금지

중앙 세션이 직접:
- FIELD.BIN 전체 재분석
- BATTLE.BIN 전체 재분석
- 시나리오 구조 전체 재발견
- 각 영역별 번역을 중복 수행

하지 않는다.

## 입력

각 세션에서 다음을 받는다.

```text
system_standard.csv
status_standard.csv
items_standard.csv
battle_standard.csv
scenario_standard.csv

system_required_glyphs.txt
status_required_glyphs.txt
items_required_glyphs.txt
battle_required_glyphs.txt
scenario_required_glyphs.txt
```

## 중앙 DB

Source of Truth:

```text
translation.db
```

개별 CSV는 import/export용이다.

## 중앙 관리 파일

```text
data/master/glossary.csv
data/master/japanese_glyph_usage.csv
data/master/free_glyph_slots.csv
data/master/hangul_code_map.csv
data/master/hangul_glyph_map.csv
data/master/korean_required_glyphs.txt
```

## 폰트 배정 규칙

각 세션은 한글 code를 직접 배정하지 않는다.

중앙 세션만:

```text
한국어 음절
↔ 기존 일본어 custom code
↔ glyph slot
```

을 결정한다.

우선순위:

```text
usage_count == 0
→ 사용하지 않는 일본어 glyph slot

부족하면
usage_count == 1~2
→ 해당 일본어 원문이 모두 번역되어 더 이상 필요 없을 때만 사용
```

## 기존 매핑 보존

한 번 GAME_VERIFIED 또는 FINAL로 확정된 한글 코드는 변경하지 않는다.

신규 글자는 기존 매핑 뒤에 추가한다.

## Translation Manager

Python GUI + SQLite 기반으로 관리한다.

탭:

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

목록:

```text
ID | 일문 | 번역문 | 상태 | 인게임확인
```

상세:
- source_file
- inner_file
- record/scene
- original_offset
- pointer_offset
- jp_raw_hex
- kr_encoded_hex
- note
- review status

## 수정 요청

GUI에:

```text
[수정 요청 복사]
```

기능을 둔다.

예:

```text
ID: SCN_D0142_0021
구분: 시나리오
일문: ...
현재 번역: ...
수정 요청:
```

## 전체 문자 집계

각 세션 번역이 모이면:

```text
모든 kr_text
→ unique Hangul syllables
```

을 계산한다.

이 결과로만 최종 폰트 테이블을 만든다.

## 최종 빌드

```text
translation.db
→ custom encode
→ font glyph generation
→ BIN/MDT patch
→ MDZ pack
→ ISO target-file replacement
→ reverse extraction verification
```

## 보고 형식

```text
MERGED
CONFLICTS
NEW GLYPHS REQUIRED
MAP UPDATED
BUILD STATUS
NEXT
```

> **Workspace storage rule:** Treat `legacy/` as read-only reference/history. Do not create or modify active work products there. Save current work and generated outputs under the project root, such as `build/`, `data/`, `exports/`, or `tools/`.
