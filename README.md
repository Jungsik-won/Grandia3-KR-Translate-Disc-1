<div align="center">

<img src="docs/assets/grandia3-korean-banner.svg" alt="Grandia III Korean Translation Project" width="100%" />

# Grandia3-Translate

### Grandia III 한국어화 프로젝트

텍스트를 추출하고, 번역하고, 실제 게임에 다시 적용하기 위한
**PlayStation 2 일본판 『그란디아 III』 비공식 한국어화 프로젝트**입니다.

<a href="https://github.com/Jungsik-won/Grandia3-Translate/releases/tag/v0.1.2-test"><img src="https://img.shields.io/badge/Release-v0.1.2--test-7c3aed?style=for-the-badge" alt="Release v0.1.2-test" /></a>
<a href="https://github.com/Jungsik-won/Grandia3-Translate/releases/download/v0.1.2-test/Grandia3_KR_Disc1_Korean_8ab14274_full.xdelta"><img src="https://img.shields.io/badge/⬇%20XDELTA%20%ED%8C%A8%EC%B9%98%20%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C-eab308?style=for-the-badge&logo=github&logoColor=white" alt="Download xdelta patch" /></a>

</div>

<p align="center">
  <a href="#korean">🇰🇷 한국어</a> ·
  <a href="#english">🇺🇸 English</a> ·
  <a href="#japanese">🇯🇵 日本語</a>
</p>

<a id="korean"></a>

## 🇰🇷 한국어

### 프로젝트 소개

그란디아 III 일본판의 게임 텍스트 구조를 분석하고, 추출된 원문을 번역 데이터로 관리한 뒤,
검증 가능한 방식으로 한국어 패치를 만드는 프로젝트입니다.

현재 저장소에는 다음 작업물이 정리되어 있습니다.

- 시스템·상태·아이템·전투·시나리오 텍스트 추출 결과
- 한국어 번역 CSV와 중앙 `translation.db`
- 글리프/codebook 및 한글 출력 검증 자료
- 추출·변환·검증용 Python/Rust 도구
- 실제 원본 ISO에 재적용 가능한 xdelta 시험 패치

### 현재 저장소 소스 상태

현재 `main`에는 `v0.1` 한글화 추출 완료 작업과 `v0.1.2-test` 시험 배포를 위한 문서·검증 도구가
반영되어 있습니다. 최종 배포 ISO에 포함된 영상·이미지·원본 게임 데이터는 저작권 보호와 파일
크기 문제로 Git 저장소에 넣지 않으며, Release의 차등 패치로만 제공합니다.

### 1. 패치 대상 원본

아래 조건과 정확히 일치하는 일본판 Disc 1 원본만 지원합니다.

| 항목 | 값 |
| --- | --- |
| 게임 | `Grandia III (Japan) (Disc 1)` |
| 지역/플랫폼 | 일본판 / PlayStation 2 |
| ISO 크기 | `4,598,890,496 bytes` |
| 원본 SHA-256 | `c588a7dada3bf7175bfe97b238b0ab4c77df6401a58d766829aec9d92f3596e8` |

다른 지역, 다른 리비전, 이미 수정된 ISO에는 적용하지 마세요. 적용 전 원본 ISO를 별도로
백업하는 것을 권장합니다.

### 최신 시험 배포판

<div align="center">

<a href="https://github.com/Jungsik-won/Grandia3-Translate/releases/download/v0.1.2-test/Grandia3_KR_Disc1_Korean_8ab14274_full.xdelta"><img src="https://img.shields.io/badge/⬇%20패치%20다운로드-XDELTA%202.13GB-16a34a?style=for-the-badge" alt="xdelta 패치 다운로드" /></a>

<br />
<sub>버튼을 누르면 패치 파일을 바로 다운로드합니다. 저장소가 비공개인 동안에는 GitHub 로그인과 저장소 접근 권한이 필요합니다.</sub>

</div>

→ [Release 페이지 열기](https://github.com/Jungsik-won/Grandia3-Translate/releases/tag/v0.1.2-test)

| 항목 | 값 |
| --- | --- |
| 패치 버전 | `v0.1.2-test` |
| 패치 형식 | `xdelta3 3.2.0 / VCDIFF` |
| 패치 파일 | `Grandia3_KR_Disc1_Korean_8ab14274_full.xdelta` |
| 패치 크기 | `2,127,140,711 bytes` |
| 패치 SHA-256 | `d20350bfa6eb169c08bad40eb7a86952c6f595e9030b36b630979ac6e1277d34` |

### 2. 패치 적용 방법

일반 사용자는 소스 코드를 빌드할 필요가 없습니다. Release에서 패치 파일과 운영체제에 맞는
적용 스크립트를 받으면 됩니다.

1. 합법적으로 보유한 정확한 일본판 Disc 1 ISO를 준비합니다.
2. Release에서 `xdelta` 패치와 자신의 운영체제용 적용 스크립트를 다운로드합니다.
3. 원본 ISO의 SHA-256이 아래 값과 일치하는지 확인합니다.
4. macOS/Linux에서는 `apply_in_place_ko.sh`, Windows에서는 `apply_in_place_ko.ps1`를 실행합니다.
5. 적용이 끝난 결과 ISO의 SHA-256이 목표값과 일치하는지 확인합니다.

```text
원본 Disc 1 SHA-256
c588a7dada3bf7175bfe97b238b0ab4c77df6401a58d766829aec9d92f3596e8

패치 적용 후 SHA-256
8ab14274af27ed97b51f78775682e27be284489b5071f571d40b374ca5eb122d
```

패치 파일은 원본 ISO를 포함하지 않는 차등 패치이며, 적용 스크립트는 출력 검증이 끝난 뒤에만
원본 경로를 교체합니다. 자세한 사용법과 checksum은 [Release의 README 및 manifest](https://github.com/Jungsik-won/Grandia3-Translate/releases/tag/v0.1.2-test)를 확인하세요.

> **결과 ISO가 5GB를 넘는 이유**
>
> xdelta 패치는 변경분만 담은 파일이지만, 적용이 끝나면 전체 디스크 이미지가 새로 생성됩니다.
> 이번 시험판은 한국어 텍스트와 하드서브 영상·이미지 데이터를 반영하는 과정에서 원본의 파일 배치와
> 디스크 이미지 크기가 확장되어, 원본 `4,598,890,496 bytes`에서 결과 `5,757,884,416 bytes`가
> 됩니다. 이는 패치 파일이 원본 ISO를 포함해서 커진 것이 아니며, 적용 시 결과 ISO를 저장할 수 있는
> 여유 공간을 별도로 확보해야 한다는 뜻입니다.

### 패치 적용 후 결과 ISO

| 항목 | 값 |
| --- | --- |
| 결과 ISO 크기 | `5,757,884,416 bytes` |
| 결과 ISO SHA-256 | `8ab14274af27ed97b51f78775682e27be284489b5071f571d40b374ca5eb122d` |
| 검증 | 원본 재적용 후 목표 ISO와 전체 byte 비교 통과 |

### 3. v0.1.2-test 반영 범위

| 영역 | 상태 |
| --- | --- |
| 누적 한국어 텍스트 | 반영 |
| 한국어 하드서브 영상 | 반영 |
| 0x9B 비올레타·코넬 장면 자막 | 반영 |
| P1WIN~P7WIN 결과 화면 텍스처 | 반영 |
| `bt_parts00` 최신 사용자 텍스처 | 반영 |
| 전투 작전·방어 글리프 수정 | 반영 |
| 첫 전투 튜토리얼 도움말 인덱스 복구(EN074C 원본 유지) | 반영 |
| 몬스터명 자연화 및 행동 주소 보존 | 반영 |
| 0x63 slot0 자막 트리거 수정 / 0x62 안전 제외 | 반영 |
| GRM13 자막 30큐 발화 단위 재분할 | 반영 |

이 시험판은 완성판이 아니라 실제 게임에서의 추가 검수가 필요한 누적 테스트 빌드이며, runtime test가
아직 대기 중입니다.
장면별 말투, 글리프 누락, 화면 배치, 영상 자막 타이밍 문제를 발견할 수 있습니다.

### 4. 저장소 구성

| 경로 | 역할 |
| --- | --- |
| `data/` | 번역 원문·번역문·글리프·codebook 데이터 |
| `exports/` | 세션별 표준 CSV와 검토용 export |
| `tools/` | 추출·변환·검증 도구 |
| `docs/` | 세션 지침·분석 기록·릴리스 문서 |
| `translation.db` | 중앙 Translation Manager 데이터베이스 |

`legacy/`는 읽기 전용 참고 영역으로 취급하며, 활성 작업이나 배포 범위에 포함하지 않습니다.
최종 ISO, 원본 게임 파일, 추출된 영상·음성·이미지·MDZ/MDT/DAT/BIN, 메모리 덤프와 빌드
캐시는 저장소와 Release에 넣지 않습니다.

### 5. 품질 검증 및 제보

패치는 지원 원본의 SHA-256을 먼저 확인하고, 적용 결과 SHA-256을 다시 확인합니다. 이번 시험판은
지정 원본에 재적용한 결과와 정본 ISO가 byte-exact임을 검증했습니다.

문제를 발견하면 GitHub Issues에 다음 정보를 함께 남겨 주세요.

- 실행 환경(PCSX2 버전 또는 실제 기기)
- Disc 1 원본 SHA-256
- 문제가 발생한 장면·메뉴·전투 상황
- 가능하면 화면 캡처와 세이브 위치

### 작업 원칙

- 원본 ISO, 패치된 ISO, 추출된 게임 자산은 저장소와 Release에 넣지 않습니다.
- `legacy/`는 읽기 전용 참고 영역이며, 활성 작업 범위에 포함하지 않습니다.
- 재현 가능한 도구와 번역 데이터 중심으로 결과를 남깁니다.
- 중요한 결과는 원본 해시, 출력 해시, byte 비교로 검증합니다.

### 저작권 및 면책

Grandia III와 관련된 게임명, 로고, 캐릭터 및 게임 데이터의 권리는 각 권리자에게 있습니다.
이 프로젝트는 비공식 팬 번역·연구 프로젝트이며 권리자와 제휴하거나 승인을 받은 프로젝트가
아닙니다. 원본 게임 ISO는 제공하지 않으며, 사용자는 자신이 합법적으로 보유한 원본에만
패치를 적용해야 합니다. 개인적·비상업적 연구 목적의 배포이며, 사용으로 발생하는 데이터
손실이나 호환성 문제를 보증하지 않습니다.

<a id="english"></a>

## 🇺🇸 English

### About

Grandia3-Translate is an unofficial Korean translation and research project for the Japanese
PlayStation 2 release of *Grandia III*. It extracts game text, organizes translations as
reproducible data, and builds verifiable patches for real-hardware/emulator testing.

The repository contains extracted text tables, Korean translation CSVs, the central
`translation.db`, glyph/codebook research, and tools for extraction, conversion, and verification.

### Download the test patch

<a href="https://github.com/Jungsik-won/Grandia3-Translate/releases/download/v0.1.2-test/Grandia3_KR_Disc1_Korean_8ab14274_full.xdelta"><img src="https://img.shields.io/badge/⬇%20DOWNLOAD%20XDELTA%20PATCH-2.13GB-16a34a?style=for-the-badge" alt="Download xdelta patch" /></a>

→ [Open the v0.1.2-test Release](https://github.com/Jungsik-won/Grandia3-Translate/releases/tag/v0.1.2-test)

You must own the exact Japanese Disc 1 source ISO. The source SHA-256 must be
`c588a7dada3bf7175bfe97b238b0ab4c77df6401a58d766829aec9d92f3596e8`; the patched output must be
`8ab14274af27ed97b51f78775682e27be284489b5071f571d40b374ca5eb122d`.

The xdelta file contains only differences, but applying it creates a complete new disc image.
For this test build, adding the Korean text, hard-subbed movies, and image data expands the disc
layout from `4,598,890,496 bytes` to `5,757,884,416 bytes`. The larger output is therefore not
because the patch contains the original ISO; make sure you have enough free space for the result ISO.

### Disclaimer

This is an unofficial, non-commercial fan translation/research project and is not affiliated with
or endorsed by the rights holders. No original or patched game ISO is distributed. Apply the patch
only to a legally owned source dump. The project provides no warranty for data loss or compatibility.

<a id="japanese"></a>

## 🇯🇵 日本語

### プロジェクトについて

Grandia3-Translate は、PlayStation 2版『グランディアIII』日本版を対象とした非公式の
韓国語化・研究プロジェクトです。ゲーム内テキストを抽出し、翻訳データとして整理した上で、
再現可能なパッチを作成・検証しています。

リポジトリには、抽出したテキスト、韓国語訳CSV、中央データベース `translation.db`、
グリフ/codebook資料、抽出・変換・検証用ツールを収録しています。

### 試験パッチのダウンロード

<a href="https://github.com/Jungsik-won/Grandia3-Translate/releases/download/v0.1.2-test/Grandia3_KR_Disc1_Korean_8ab14274_full.xdelta"><img src="https://img.shields.io/badge/⬇%20XDELTA%20%E3%83%91%E3%83%83%E3%83%81%E3%82%92%E3%83%80%E3%82%A6%E3%83%B3%E3%83%AD%E3%83%BC%E3%83%89-2.13GB-16a34a?style=for-the-badge" alt="xdeltaパッチをダウンロード" /></a>

→ [v0.1.2-test Releaseを開く](https://github.com/Jungsik-won/Grandia3-Translate/releases/tag/v0.1.2-test)

正確な日本版 Disc 1 のISOを所有している必要があります。元ISOのSHA-256は
`c588a7dada3bf7175bfe97b238b0ab4c77df6401a58d766829aec9d92f3596e8`、パッチ適用後のSHA-256は
`8ab14274af27ed97b51f78775682e27be284489b5071f571d40b374ca5eb122d` でなければなりません。

xdeltaファイルは差分のみを含みますが、適用後は完全なディスクイメージが生成されます。
この試験版では韓国語テキスト、字幕付き動画、画像データの反映によりディスク配置が拡張され、
元の `4,598,890,496 bytes` から `5,757,884,416 bytes` になります。パッチにオリジナルISOが
含まれているためではありません。適用前に結果ISOを保存できる空き容量を確保してください。

### 免責事項

本プロジェクトは非公式・非営利のファン翻訳/研究プロジェクトであり、権利者とは関係ありません。
オリジナルISOやパッチ済みISOは配布していません。合法的に所有している元ISOにのみ適用してください。
データ損失や互換性について保証しません。

<div align="center">

<sub>Grandia3-Translate · v0.1.2-test · Korean fan translation research project</sub>

</div>
