#!/bin/bash

slidedecks=(
    "e.205-mapping-investigations-and-cases-in-misp"
    "e.206-from-evidences-to-actionable-information"
    "e.303-lab2-encoding-information-and-sharing-it"
    "e.304-lab3-encoding-information-and-sharing-it-2"
)

mkdir -p output
mkdir -p output/handout

export TEXINPUTS=::`pwd`/themes/

for slide in ${slidedecks[@]}; do
    if test -f "${slide}/slides/slide.tex"; then
        echo "---- Building     ${slide}"
        cd ${slide}/slides
        pdflatex slide.tex
        pdflatex slide.tex
        rm *.aux *.toc *.snm *.log *.out *.nav *.vrb *.log 2> /dev/null
        sed '12 i \\\\usepackage{pgfpages}\n\\setbeameroption{show notes on second screen=right}' slide.tex >slide_handout.tex
        pdflatex slide_handout.tex
        pdflatex slide_handout.tex
        rm *.aux *.toc *.snm *.log *.out *.nav *.vrb *.log 2> /dev/null
        cp slide.pdf ../../output/${slide}.pdf
        cp slide_handout.pdf ../../output/handout/${slide}_handout.pdf
        rm slide.pdf
        rm slide_handout.pdf
        rm slide_handout.tex
    else
         echo "---- Not found    ${slide}"
    fi
    cd ../..
done

pushd e.0-mandatory-eLearning-materials
pandoc eLearning.md --pdf-engine=xelatex -o ../output/0_eLearning.pdf
popd
