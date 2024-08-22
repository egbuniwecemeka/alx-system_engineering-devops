# A puppet file that resets the ulimit of a request

# Modify ULIMT of server default's file
exec{'fix-ulimit':
  # Updating the ulimit value
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',

  # Path to config file containing ulimit value
  path    => '/usr/local/bin/:/bin'
}


