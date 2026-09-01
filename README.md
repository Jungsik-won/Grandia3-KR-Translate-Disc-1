<div align="center">

<img src="docs/assets/grandia3-korean-banner.svg" alt="Grandia III Korean Translation Project" width="100%" />

# Grandia3-Translate

### Grandia III 한국어화 프로젝트

텍스트를 추출하고, 번역하고, 실제 게임에 다시 적용하기 위한
**PlayStation 2 일본판 『그란디아 III』 비공식 한국어화 프로젝트**입니다.

<a href="https://github.com/Jungsik-won/Grandia3-Translate/releases/tag/v0.1.1-test"><img src="https://img.shields.io/badge/Release-v0.1.1--test-7c3aed?style=for-the-badge" alt="Release v0.1.1-test" /></a>
<a href="https://github.com/Jungsik-won/Grandia3-Translate/releases/download/v0.1.1-test/Grandia3_KR_Disc1_Korean_b4f69d38_full.xdelta"><img src="https://img.shields.io/badge/⬇%20XDELTA%20%ED%8C%A8%EC%B9%98%20%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C-eab308?style=for-the-badge&logo=github&logoColor=white" alt="Download xdelta patch" /></a>

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

### 최신 시험 배포판

<div align="center">

<a href="https://github.com/Jungsik-won/Grandia3-Translate/releases/download/v0.1.1-test/Grandia3_KR_Disc1_Korean_b4f69d38_full.xdelta"><img src="https://img.shields.io/badge/⬇%20패치%20다운로드-XDELTA%202.13GB-16a34a?style=for-the-badge" alt="xdelta 패치 다운로드" /></a>

<br />
<sub>버튼을 누르면 패치 파일을 바로 다운로드합니다. 저장소가 비공개인 동안에는 GitHub 로그인과 저장소 접근 권한이 필요합니다.</sub>

</div>

→ [Release 페이지 열기](https://github.com/Jungsik-won/Grandia3-Translate/releases/tag/v0.1.1-test)

### 적용 방법

1. 합법적으로 보유한 정확한 일본판 Disc 1 ISO를 준비합니다.
2. Release에서 `xdelta` 패치와 자신의 운영체제용 적용 스크립트를 다운로드합니다.
3. 원본 ISO의 SHA-256이 아래 값과 일치하는지 확인합니다.
4. macOS/Linux에서는 `apply_in_place_ko.sh`, Windows에서는 `apply_in_place_ko.ps1`를 실행합니다.
5. 적용이 끝난 결과 ISO의 SHA-256이 목표값과 일치하는지 확인합니다.

```text
원본 Disc 1 SHA-256
c588a7dada3bf7175bfe97b238b0ab4c77df6401a58d766829aec9d92f3596e8

패치 적용 후 SHA-256
b4f69d384ca92bbaf02f1b4ba363eb4f42e0a41b5f67ff864b5ad163a2c5f955
```

패치 파일은 원본 ISO를 포함하지 않는 차등 패치이며, 적용 스크립트는 출력 검증이 끝난 뒤에만
원본 경로를 교체합니다. 자세한 사용법과 checksum은 [Release의 README 및 manifest](https://github.com/Jungsik-won/Grandia3-Translate/releases/tag/v0.1.1-test)를 확인하세요.

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

<a href="https://github.com/Jungsik-won/Grandia3-Translate/releases/download/v0.1.1-test/Grandia3_KR_Disc1_Korean_b4f69d38_full.xdelta"><img src="https://img.shields.io/badge/⬇%20DOWNLOAD%20XDELTA%20PATCH-2.13GB-16a34a?style=for-the-badge" alt="Download xdelta patch" /></a>

→ [Open the v0.1.1-test Release](https://github.com/Jungsik-won/Grandia3-Translate/releases/tag/v0.1.1-test)

You must own the exact Japanese Disc 1 source ISO. The source SHA-256 must be
`c588a7dada3bf7175bfe97b238b0ab4c77df6401a58d766829aec9d92f3596e8`; the patched output must be
`b4f69d384ca92bbaf02f1b4ba363eb4f42e0a41b5f67ff864b5ad163a2c5f955`.

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

<a href="https://github.com/Jungsik-won/Grandia3-Translate/releases/download/v0.1.1-test/Grandia3_KR_Disc1_Korean_b4f69d38_full.xdelta"><img src="https://img.shields.io/badge/⬇%20XDELTA%20%E3%83%91%E3%83%83%E3%83%81%E3%82%92%E3%83%80%E3%82%A6%E3%83%B3%E3%83%AD%E3%83%BC%E3%83%89-2.13GB-16a34a?style=for-the-badge" alt="xdeltaパッチをダウンロード" /></a>

→ [v0.1.1-test Releaseを開く](https://github.com/Jungsik-won/Grandia3-Translate/releases/tag/v0.1.1-test)

正確な日本版 Disc 1 のISOを所有している必要があります。元ISOのSHA-256は
`c588a7dada3bf7175bfe97b238b0ab4c77df6401a58d766829aec9d92f3596e8`、パッチ適用後のSHA-256は
`b4f69d384ca92bbaf02f1b4ba363eb4f42e0a41b5f67ff864b5ad163a2c5f955` でなければなりません。

### 免責事項

本プロジェクトは非公式・非営利のファン翻訳/研究プロジェクトであり、権利者とは関係ありません。
オリジナルISOやパッチ済みISOは配布していません。合法的に所有している元ISOにのみ適用してください。
データ損失や互換性について保証しません。

<div align="center">

<sub>Grandia3-Translate · v0.1.1-test · Korean fan translation research project</sub>

</div>
