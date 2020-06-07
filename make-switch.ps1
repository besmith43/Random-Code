param (
	[Parameter(Mandatory=$true)]
	[string]$infile,
	[Parameter(Mandatory=$true)]
	[string]$outfile
)


"switch () {" | Out-File $outfile -force
& 'C:\Program Files\Git\usr\bin\awk.exe' '{ print \"\tcase \",$1,\":\n\t\tbreak;\" }' $infile | & 'C:\Program Files\Git\usr\bin\head.exe' -n -2 | & 'C:\Program Files\Git\usr\bin\tail.exe' -n+3 | Out-File $outfile -append
"`tdefault:`n`t`tbreak;`n}" | Out-File $outfile -append
