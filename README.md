# Custom Keyboard Glyphs

A personal font and custom alphabet system for rendering ordinary text using user-designed glyphs.

The project is designed around a real installable font rather than a text-encoding system. Normal Latin characters remain unchanged in the underlying text while the custom font controls how those characters are visually rendered.

## Project Goals

* Create a fully custom A–Z alphabet.
* Use user-designed vector artwork for each glyph.
* Render uppercase and lowercase Latin letters using a single alphabet design.
* Preserve normal spaces, punctuation, and digits by default.
* Generate an installable TTF or OTF font.
* Keep glyph artwork, configuration, and font generation separate.
* Support independent personal and public alphabet configurations.
* Make the font reproducibly buildable as the alphabet evolves.

## Architecture

The project separates the alphabet artwork from the font-generation system:
```
Glyph Artwork
     +
Configuration
     ↓
Font Builder
     ↓
TTF / OTF
     ↓
Install Font
     ↓
Type Normally
     ↓
Custom Glyphs
```
The glyph artwork is the source of truth for the visual alphabet. Generated font files are build artifacts and are not treated as source files.

Personal glyph artwork and personal configurations may be kept outside this repository. The repository contains the reusable font-building system and shareable example material.

## Repository Structure
```
custom-keyboard-glyphs/
│
├── .gitignore
├── LICENSE
├── README.md
│
├── configs/
│   └── example.yaml
│
├── glyphs/
│   └── example/
│
├── scripts/
│
├── font/
│   └── source/
│
└── tests/
```
## Version 1 Scope

Version 1 focuses on:

1. A custom A–Z alphabet.
2. Vector glyph artwork.
3. Unicode mapping from ordinary Latin characters to custom glyphs.
4. Normal spaces, punctuation, and digits.
5. Consistent typography, spacing, and alignment.
6. A reproducible font-generation process.
7. Installation and use on macOS.

The initial implementation will prove the complete pipeline with a single experimental glyph before expanding to the full alphabet.

## Font Transformation vs. Text Encoding

This project primarily uses font transformation:
```
HELLO
  ↓
Custom Font
  ↓
Custom visual glyphs

The underlying text remains:

HELLO

This is distinct from text encoding:

HELLO
  ↓
Character Mapping
  ↓
Encoded Text
```
An optional encoding or decoding layer may be considered in a future version, but it is not part of Version 1.

## Development Philosophy

The project is intentionally developed incrementally.

The priorities are:

1. Understandable architecture.
2. Small, focused changes.
3. Reproducible builds.
4. Clear separation of source artwork and generated output.
5. Minimal tooling and dependencies.
6. Easy modification of the alphabet without rewriting the build system.

The project should remain simple enough that the font-generation process can be understood and modified directly by its creator.

## Status

### Early development — Version 1

The initial repository structure has been established. The next milestone is to create one experimental glyph and prove the complete SVG → font → macOS installation pipeline.