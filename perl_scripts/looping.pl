#!/usr/bin/env perl

use strict;
use warnings;

my $sum = 0;
#my $curr = 0

while(1){
	print "Enter a number:\t";
	my $curr = int <STDIN>;
	if ($curr == 13) {
	print "The total sum is ".$sum."\n";
	 exit; }
	
	elsif($curr == 18 or $curr == 9) { next; }
	
	else{ $sum += $curr;	}
}

