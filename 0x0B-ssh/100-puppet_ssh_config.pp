# Adding a Configuration line for `ssh_config` file.
file_line {'configuring /etc/ssh/ssh_config':
    path => '/etc/ssh/ssh_config',
    line => 'IdentityFile ~/.ssh/school',
}
