#!/usr/bin/env ruby
# ruby script that uses repetition token in regex
puts ARGV[0].scan(/hbt{2,5}n/).join
