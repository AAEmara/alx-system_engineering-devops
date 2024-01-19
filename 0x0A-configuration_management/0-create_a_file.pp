# Puppet manifest to create a `/tmp/school` file
# with `0744` permission, File's owner and group is `www-data`;
# with content that says "I love Puppet".
file { '/tmp/school':
    path    => '/tmp/school',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet',
}
