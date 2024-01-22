# Adding a Configuration line for `ssh_config` file.
file {'configuring /etc/ssh/ssh_config':
    path => '/etc/ssh/ssh_config',
    content => 'IdentityFile ~/.ssh/school',
}
