compile:
	copy fasta.hipe-2.hipe fasta.erl
	erlc fasta.erl
measure:
	cmd /C start /B cmd /C "cmd /C start /B scaphandre json -n 100000 -f fasta-main-25000000.json >NUL 2>NUL"
	timeout /T 5 /NOBREAK > NUL
	erl -smp enable -noshell -run  fasta main 25000000
	timeout /T 5 /NOBREAK > NUL
	taskkill /F /IM scaphandre.exe
run:
	erl -smp enable -noshell -run  fasta main 25000000
clean:
	del /Q *.json *.beam *.erl *.dump