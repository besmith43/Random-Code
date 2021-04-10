#!/usr/bin/env pwsh

param(
	[ValidateSet("gaming","nas","web","media","compute")]
	[Parameter(Position=0)]
	[string]$serverName = "compute",
	[string]$IP,
	[string]$Port,
	[string]$username
)

switch ($serverName)
{
	"gaming" {
		$IP = "besmith.synology.me"
		$Port = "8002"
		$username = "blake"
	}
	"nas" {
		$IP = "besmith.synology.me"
		$Port = "22"
		$username = "besmith"
	}
	"web" {
		$IP = "besmith.tech"
		$Port = "22"
		$username = "besmith"
	}
	"media" {
		$IP = "besmith.synology.me"
		$Port = "8003"
		$username = "besmith"
	}
	"compute" {
		$IP = "besmith.synology.me"
		$Port = "8005"
		$username = "besmith"
	}
}

ssh $IP -p $Port -l $username
