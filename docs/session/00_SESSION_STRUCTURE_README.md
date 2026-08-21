# Grandia III 한국어화 — 세션별 작업 구조

이 문서는 여러 Codex 세션을 병렬로 운용할 때 작업이 꼬이지 않도록 역할을 분리하기 위한 기준이다.

## 핵심 원칙

각 작업 세션은:
- 자기 영역의 일본어 원문 정리
- 한국어 번역
- 고유 ID 부여
- 필요한 한글 음절 목록 생성
- source file / offset / pointer 등 메타데이터 정리

까지만 책임진다.

각 작업 세션이 독자적으로:
- 한글 code를 새로 배정
- 일본어 glyph slot을 선택
- 최종 폰트 테이블 수정
- 최종 GR3.MDT 폰트 bitmap을 누적 수정

하는 것은 금지한다.

최종 폰트/코드표/글리프 배정은 중앙 세션에서만 관리한다.

## 세션 구성

- `01_CENTRAL_SESSION.md` — 중앙 관리 / Translation Manager / 폰트 테이블 / 통합 빌드
- `02_SYSTEM_SESSION.md` — 시스템 메뉴 및 시스템 메시지
- `03_STATUS_SESSION.md` — 상태창 / 장비창
- `04_ITEM_SESSION.md` — 아이템 이름 / 설명
- `05_BATTLE_SESSION.md` — 전투 UI / 스킬 / 마법 / 전투 메시지
- `06_SCENARIO_SESSION.md` — 시나리오 대사 추출 / 전문 번역
- `07_FONT_PROOF_SESSION.md` — 초기 한글 출력 구조 실증 전용
- `08_COMMON_OUTPUT_SCHEMA.md` — 모든 세션이 따라야 할 공통 CSV/ID 규칙

## 작업 흐름

```text
각 세션
→ 표준 CSV
→ required_glyphs.txt
→ 중앙 세션

중앙 세션
→ 통합 translation.db
→ 전체 필요 한글 집계
→ 일본어 미사용 glyph 분석
→ 최종 hangul_code_map
→ 최종 hangul_glyph_map
→ 폰트 bitmap 일괄 생성
→ 대상 바이너리 encode/patch
→ MDZ pack
→ ISO patch
→ QA
```


## Git / GitHub

모든 세션은 `13_GIT_GITHUB_WORKFLOW.md`와 루트 `AGENTS.md`의 Git 규칙을 따른다.

> **Workspace storage rule:** Treat `legacy/` as read-only reference/history. Do not create or modify active work products there. Save current work and generated outputs under the project root, such as `build/`, `data/`, `exports/`, or `tools/`.
