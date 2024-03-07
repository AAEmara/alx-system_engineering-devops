# This is a puppet manifest
exec {'fixing_wordpress':
        command  => 'sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
        provider => 'shell',
}
