# Puppet manifest to kill the `killmenow` process.
exec {'pkill killmenow':
    command  => 'pkill killmenow',
    provider => 'shell',
}
