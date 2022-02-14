my $datetime = "2016-04-11 20:59:03";
my ($date, $time) = $datetime =~ /(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2})/;
print "data: $date\n","time: $time\n";