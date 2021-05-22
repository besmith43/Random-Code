#!/usr/bin/env pwsh

Param(
	[Parameter(Position=0)]
	[string]$UpdatedFiles = "*",
	[Parameter(Mandatory=$True,Position=1)]
	[string]$commit_string,
	[Parameter(Position=2)]
	[string[]]$Remotes = $(git remote show),
	[Parameter(Position=3)]
	[string]$Branch = "master"
)

git add $UpdatedFiles
git commit -m $commit_string
git pull
foreach($remote in $Remotes)
{
	git push $remote $Branch
}
