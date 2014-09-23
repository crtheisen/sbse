a2ps --center-title="csc710sbse: $1:Theisen" -qr2gc -MLetter -l 90 -o ./$1/$1.ps ./$1/files/* ./$1/files/searchers/* ./$1/files/models/*
ps2pdf ./$1/$1.ps ./$1/$1.pdf