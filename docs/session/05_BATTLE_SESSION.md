# Grandia III 한국어화 — 전투 세션

## 범위

```text
전투 메뉴
전투 command
스킬
마법
전투 시스템 메시지
전투 도움말/설명
```

전투 음성은 이 세션 범위에서 제외한다.

## 기존 분석 우선

Reference Pack의:
- BATTLE.BIN
- GR3 action/skill
- battle UI
관련 기존 CSV/MD를 먼저 읽는다.

## ID 예

```text
BATTLE_CMD_0001
BATTLE_MSG_0001
SKILL_0001_NAME
SKILL_0001_DESC
MAGIC_0001_NAME
MAGIC_0001_DESC
```

## 출력

```text
exports/battle_standard.csv
exports/battle_required_glyphs.txt
```

## 용어 통일

아이템/시스템과 겹치는 용어는 중앙 glossary를 따른다.

예:

```text
HP
MP
회복
공격
방어
필살기
마법
```

## 한글 관련 규칙

필요 글자만 추출한다.

신규 code/glyph slot은 중앙 세션에서 배정한다.

## 완료 기준

- 전투 관련 텍스트 분류
- 표준 ID 부여
- 한국어 번역
- required glyph 목록 생성
- 중앙 세션 제출

> **Workspace storage rule:** Treat `legacy/` as read-only reference/history. Do not create or modify active work products there. Save current work and generated outputs under the project root, such as `build/`, `data/`, `exports/`, or `tools/`.
