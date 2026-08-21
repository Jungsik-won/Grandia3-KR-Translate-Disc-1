# Grandia III 한글 폰트 / Glyph 재활용 전략

## 핵심 전략

처음부터 새로운 한글 font page를 확장하지 않는다.

가장 우선하는 방식:

```text
기존 일본어 font code/glyph 중
게임 실제 원문에서 사용되지 않는 슬롯
→ 한글 음절로 재활용
```

## 장점

```text
GR3.MDT 크기 증가 최소화
MDZ 구조 변경 최소화
glyph count 유지
renderer 수정 최소화
descriptor/table 확장 최소화
ISO/LBA 영향 최소화
```

폰트 영역 확장은 unused glyph slot이 부족한 경우에만 검토한다.

## 일본어 미사용 슬롯 찾기

게임 전체 일본어 문자열을 대상으로 각 custom code 사용 횟수를 계산한다.

필수 출력:

```text
data/gr3/japanese_glyph_usage.csv
data/gr3/free_glyph_slots.csv
```

분류:

```text
usage_count = 0 → FREE
usage_count = 1 → LOW_USAGE
usage_count = 2 → LOW_USAGE
usage_count > 2 → KEEP
```

우선 FREE만 사용한다.

## 한글 매핑 관리

초기에는 필요한 음절만 provisional mapping으로 추가한다.

```text
약 → unused Japanese code A
초 → unused Japanese code B
회 → unused Japanese code C
복 → unused Japanese code D
```

source of truth:

```text
data/gr3/hangul_code_map.csv
```

권장 컬럼:

```text
korean_char
encoded_hex
original_japanese_char
original_usage_count
glyph_slot
status
notes
```

상태:

```text
PROVISIONAL
GAME_VERIFIED
FINAL
```

## 최종 glyph 집합 확정

시스템/상태/아이템/전투/시나리오의 전체 한국어 번역이 준비된 뒤:

```text
모든 한국어 번역문
→ unique Hangul syllable set
```

을 계산한다.

필요 글자만 최종 폰트에 만든다.

## 폰트 디자인 적용 시점

폰트 구조와 폰트 디자인을 분리한다.

초기에는 단순 테스트 bitmap으로 code → glyph → screen 경로만 증명한다.

최종 PHASE에서 Neo둥근모 등 최종 폰트를 실제 사용 음절에 한해 rasterize한다.

폰트 디자인 때문에 encoding이나 code mapping을 다시 바꾸지 않는다.

## Neo둥근모 사용

Codex가 필요하면 공식/신뢰 가능한 배포처에서 확보하되:

```text
라이선스 확인
배포 가능 여부 확인
저장소 포함 여부 확인
```

을 먼저 한다.

프로젝트의 핵심은 폰트 원본 자체보다:

```text
필요 glyph rasterize
→ 게임 포맷 변환
→ 재활용 glyph slot 삽입
```

파이프라인이다.

## 금지 사항

```text
아무 일본어 glyph나 덮어쓰기
사용 여부 확인 없이 한자 재활용
lookup 값 = glyph ordinal이라고 가정
atlas index % width 방식 무검증 사용
실패한 font 후보 위에 patch 누적
```

모든 destructive test는 CLEAN 원본에서 단일 변경으로 수행한다.

> **Workspace storage rule:** Treat `legacy/` as read-only reference/history. Do not create or modify active work products there. Save current work and generated outputs under the project root, such as `build/`, `data/`, `exports/`, or `tools/`.
