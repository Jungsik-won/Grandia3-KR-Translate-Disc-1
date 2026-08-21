# Grandia III 한국어화 — 권장 작업 순서

## PHASE 0 — 한글 출력 기반 실증

목표:

```text
やくそう → 약초
```

전체 한글 폰트를 만들기 전에 한 글자라도 실제 게임에서 출력되는 경로를 증명한다.

```text
やくそう
→ 家くそう
→ 家 glyph source destructive proof
→ 약くそう
→ 약초
```

실패한 후보에 다음 패치를 누적하지 않는다.

## PHASE 0.5 — Translation Manager 기반 구축

시스템/아이템/시나리오를 따로 관리하기 전에 중앙 번역 DB와 GUI를 만든다.

세부 사양은 `04_TRANSLATION_MANAGER_SPEC.md`를 따른다.

## PHASE 1 — 시스템 메뉴 한국어화

대상:

```text
저장
불러오기
설정
메인 메뉴
기본 시스템 메시지
확인/취소
기타 공통 UI
```

FIELD.BIN / SLPM / common resources의 기존 분석을 우선 재사용한다.

## PHASE 2 — 상태/장비 화면 한국어화

대상:

```text
능력치 명칭
상태창 label
장비 슬롯
장비 도움말
캐릭터 관련 고정 UI
```

동적 GR3 문자열과 고정 UI 문자열을 구분한다.

## PHASE 3 — 아이템 이름/설명 한국어화

기존 추출 결과를 재사용한다.

```text
437 records
이름 약 435/437 decode
설명 437/437 decode
```

기존 decoded CSV/JSON을 Translation Manager로 import한다.

고유 ID 예:

```text
ITEM_0107_NAME
ITEM_0107_DESC
```

## PHASE 4 — 전투 관련 한국어화

대상:

```text
battle menu
command
skill
spell
combat system message
battle help/description
```

전투 음성은 현재 범위에서 제외한다.

## PHASE 5 — 시나리오 전체 전문 번역

DATA/*.MDZ 계열의 시나리오 구조를 확정하고 전체 텍스트를 export한다.

```text
추출
→ 전체 전문 번역
→ 문맥 검수
→ 용어 통일
```

까지 먼저 한다.

게임에 한 줄씩 바로 삽입하지 않는다.

## PHASE 6 — 실제 사용 한글 음절 집계

다음 전체 한국어 번역문을 합친다.

```text
시스템
상태/장비
아이템
전투
시나리오
기타
```

그리고 실제 사용된 완성형 한글 음절 unique set만 추출한다.

```text
data/gr3/korean_required_glyphs.txt
data/gr3/korean_required_glyphs.csv
```

## PHASE 7 — 최종 code/glyph table 고정

일본어 원문 전체에서 custom code 사용 빈도를 계산한다.

```text
usage_count == 0 → FREE_GLYPH_SLOT
```

을 가장 먼저 재활용한다.

부족하면 usage_count 1~2의 글자를 검토하되, 해당 일본어 문장이 모두 번역되어 원 글리프가 더 이상 필요 없는 경우에만 쓴다.

최종:

```text
hangul_code_map_final.csv
```

을 고정한다.

## PHASE 8 — 시나리오 전체 삽입

최종 code/glyph table이 고정된 후 전체 시나리오를 encode하여 DATA/*.MDZ에 삽입한다.

## PHASE 9 — 최종 폰트 디자인 및 전체 QA

초기 테스트 비트맵 대신 최종 폰트를 적용한다.

후보:

```text
Neo둥근모
```

이 단계에서는:

```text
code mapping 유지
glyph slot 유지
문자열 유지
bitmap만 교체
```

한다.

최종 검수:

```text
오탈자
문맥
줄바꿈
UI overflow
폰트 깨짐
제어코드
전투 표시
시나리오 전체
```

> **Workspace storage rule:** Treat `legacy/` as read-only reference/history. Do not create or modify active work products there. Save current work and generated outputs under the project root, such as `build/`, `data/`, `exports/`, or `tools/`.
