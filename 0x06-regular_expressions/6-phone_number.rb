#!/usr/bin/env ruby
# phone number \d
puts ARGV[0].scan(/^\d{10,10}$/).join
