Import-Module WebAdministration
set-Location IIS:\Sites
$Site = dir
foreach ($item in $Site)
{
$Site = $item.Name
$SiteStatus = $item.state
Write-Host "$Site -> $SiteStatus"

if($SiteStatus -ne "Started")
{
Write-Host "-----> $Site found stopped."
Start-Website -Name $Site
Write-Host "-----> $Site started."
}
}