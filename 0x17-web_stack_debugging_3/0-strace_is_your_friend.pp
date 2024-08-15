# A puppet script that fixes a faulty "phpp" extension to "php"

exec{'wordpress-fix':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ['/usr/local/bin/', '/bin/']
}
