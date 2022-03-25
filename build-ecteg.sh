#!/bin/bash

slidedecks=(
    "e.101-practical-information-sharing-between-law-enforcement-and-csirt-communities-using-misp"
    "e.102-data-mining-tor-social-networks-osint-with-ail-project"
    "e.103-managing-information-sharing-communities-cerebrate-introduction"
    "e.104-csirts-network-notification-and-sharing-scenarios"
    "e.205-mapping-investigations-and-cases-in-misp"
    "e.206-from-evidences-to-actionable-information"
    "e.303-lab2-encoding-information-and-sharing-it"
    "e.304-lab3-encoding-information-and-sharing-it-2"
)

mkdir -p output-ecteg
mkdir -p output-ecteg/handout

export TEXINPUTS=::`pwd`/themes/ecteg
export TAG=`git describe --tags --abbrev=0`

for slide in ${slidedecks[@]}; do
    if test -f "${slide}/slides/slide.tex"; then
        echo "---- Building     ${slide}"
        cd ${slide}/slides
        cp ../../themes/ecteg/logo.pdf misplogo.pdf
        pdflatex slide.tex
        pdflatex slide.tex
        rm *.aux *.toc *.snm *.log *.out *.nav *.vrb *.log 2> /dev/null
        sed '12 i \\\\usepackage{pgfpages}\n\\setbeameroption{show notes on second screen=right}' slide.tex >slide_handout.tex
        pdflatex slide_handout.tex
        pdflatex slide_handout.tex
        rm *.aux *.toc *.snm *.log *.out *.nav *.vrb *.log 2> /dev/null
        cp slide.pdf ../../output-ecteg/${slide}.pdf
        cp slide_handout.pdf ../../output-ecteg/handout/${slide}_handout.pdf
        rm slide.pdf
        rm slide_handout.pdf
        rm slide_handout.tex
        cp ../../themes/misplogo.pdf misplogo.pdf
    else
         echo "---- Not found    ${slide}"
    fi
    cd ../..
done

#pushd e.0-mandatory-eLearning-materials
#pandoc eLearning.md --pdf-engine=xelatex -V colorlinks=true \
#-V geometry="top=1cm, bottom=1cm, left=1cm, right=1cm" \
#-V linkcolor=blue \
#-V urlcolor=red \
#-V toccolor=gray -o ../output/0_eLearning.pdf
#popd
