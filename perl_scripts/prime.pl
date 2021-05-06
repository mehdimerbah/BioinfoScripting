#!/usr/bin/env perl

#use strict;
use warnings;


OUTER: for (my $i = 3; $i <= 1000; $i++) {
	$flag = 1;	
	
	INNER: for (my $j = 2; $j <= sqrt($i); $j++) {
		
		if($i % $j == 0){
			$flag = 0;
			next (OUTER);
		}
	}

	if($flag == 1){
		print $i;
		print "\n";
	}
}