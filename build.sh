#!/bin/sh

./create_syntax.sh

pandoc \
  --self-contained \
  --filter pandoc-crossref \
  --css Style/Arcana.css \
  --css Style/Buttondown.css \
  --from=markdown \
  --to=html5 \
  -T "Programming Arcana" \
  Metadata.yaml \
  Text.en/*.md \
  -o bin/ProgrammingArcana.html

pandoc \
  --self-contained \
  --filter pandoc-crossref \
  --epub-stylesheet Style/ebook.css \
  --from=markdown \
  --to=epub3 \
  -T "Programming Arcana" \
  Metadata.yaml \
  Text.en/*.md \
  -o bin/ProgrammingArcana.epub

open bin/ProgrammingArcana.html
