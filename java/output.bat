@echo off
set resPath=%~f1%\src
set mainResPath=%resPath%\main
set outputPath=%~f1%\out
set mainOutPath=%outputPath%\main

rem bibを出力用のパスにコピー, auxが参照できるようにする
call copy %mainResPath%.bib %mainOutPath%.bib 
rem aux作成
call platex -output-directory=%outputPath% -synctex=1 -jobname=main -kanji=utf8 -guess-input-enc %mainResPath%
rem auxを参照してpbibtexがbbl(blg)を作成
call pbibtex main -kanji=utf8
rem auxとbblを紐付け
call platex -output-directory=%outputPath% -synctex=1 -jobname=main -kanji=utf8 -guess-input-enc %mainResPath%
rem 上記の紐付けを参照にしてpdf作成
call platex -output-directory=%outputPath% -synctex=1 -jobname=main -kanji=utf8 -guess-input-enc %mainResPath% && dvipdfmx %mainOutPath%
rem コピーしたbibは邪魔なので消す
call del main.bib
rem pdfを開く
start %mainOutPath%.pdf
exit 0