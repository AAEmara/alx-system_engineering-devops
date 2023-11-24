# Killing a process named `killmenow`.
exec { 'pkill -f ./killmenow':
    command  => 'pkill -f ./killmenow',
    provider => shell
}
