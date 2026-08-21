# Grandia III 한국어화 — 아이템 세션

## 범위

```text
아이템 이름
아이템 설명
아이템 효과/도움말 등 관련 텍스트
```

## 기존 분석 재사용

아이템 테이블은 이미 상당 부분 분석되어 있다.

기준:

```text
Item table base = 0xD80
Record size     = 0x20

+0x04 = relative name pointer
+0x08 = name byte length
+0x10 = relative description pointer
```

기존 추출 기준:

```text
437 records
이름 약 435/437 decode
설명 437/437 decode
```

Reference Pack의 기존 item CSV/JSON/codebook을 먼저 사용한다.

처음부터 재추출하지 않는다.

## ID 규칙

```text
ITEM_0000_NAME
ITEM_0000_DESC
ITEM_0000_EFFECT
```

예:

```text
ITEM_0107_NAME
ITEM_0107_DESC
```

## 출력

```text
exports/items_standard.csv
exports/items_required_glyphs.txt
```

## 번역

기존 일문은 보존한다.

한국어 번역은 별도 kr_text에 기록한다.

## 한글 code

아이템 세션이 독자적으로 글리프 슬롯을 확정하지 않는다.

중앙 map이 있으면 encode 가능.
중앙 map에 없는 글자는:

```text
UNASSIGNED
```

로 표시하고 required glyph 목록에 추가한다.

## 완료 기준

- 기존 item 데이터 표준 schema로 변환
- 이름/설명 한국어 번역
- required glyph 목록 생성
- 중앙 세션에 제출

> **Workspace storage rule:** Treat `legacy/` as read-only reference/history. Do not create or modify active work products there. Save current work and generated outputs under the project root, such as `build/`, `data/`, `exports/`, or `tools/`.
