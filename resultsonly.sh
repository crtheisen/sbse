a2ps --center-title="csc710sbse: $1:Theisen" -qr2gc -MLetter -l 110 -o ./$1/results.ps ./$1/files/results/*
ps2pdf ./$1/results.ps ./$1/results.pdf