Import-Module WebAdministration
set-Location IIS:\AppPools
$ApplicationPools = dir
foreach ($item in $ApplicationPools)
{
$ApplicationPoolName = $item.Name
$ApplicationPoolStatus = $item.state
Write-Host "$ApplicationPoolName -> $ApplicationPoolStatus"

if($ApplicationPoolStatus -ne "Started")
{
Write-Host "-----> $ApplicationPoolName found stopped."
Start-WebSite -Name $ApplicationPoolName
Write-Host "-----> $ApplicationPoolName started."
}
}