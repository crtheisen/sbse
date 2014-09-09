a2ps --center-title="csc710sbse: $1:Theisen" -qr2gc -MLetter -l 90 -o ./$1/$1.ps ./$1/files/*
ps2pdf ./$1/$1.ps ./$1/$1.pdf