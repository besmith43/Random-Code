#!/usr/bin/env pwsh

Param (
	[Parameter(Position=0)]
	[string[]]$Remotes = $(git remote show)
)

foreach($remote in $Remotes)
{
	git pull $remote
}
