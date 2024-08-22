# A puppet file that resets the ulimit of a request

# Modify ULIMT of server default's file
exec{'fix-ulimit':
  # Updating the ulimit value
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',

  # Path to sed executable for sed command
  path    => '/usr/local/bin/:/bin'
}

# Restart nginx
exec{'restart-nginx':
  # Restart nginx server
  command => '/etc/init.d/nginx restart',

  # Path to config file.
  path    => '/etc/init.d/'
}