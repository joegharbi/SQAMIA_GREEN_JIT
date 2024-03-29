compile:
	copy revcomp.hipe revcomp.erl
	erlc revcomp.erl
measure:
	cmd /C start /B cmd /C "scaphandre json -n 100000 -f revcomp-main-0.json >NUL 2>NUL"
	timeout /T 5 /NOBREAK > NUL
	erl -smp enable -noshell -run  revcomp main 0 < ../../revcomp-input25000000.txt
	timeout /T 5 /NOBREAK > NUL
	taskkill /F /IM scaphandre.exe
run:
	erl -smp enable -noshell -run  revcomp main 0 < ../../revcomp-input25000000.txt
clean:
	del /Q *.json *.beam *.erl *.dump