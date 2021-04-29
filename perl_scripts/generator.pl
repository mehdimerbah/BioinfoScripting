#!usr/bin/env perl
use strict;
use warnings;


my $num1=int rand(9) + 1;
my $num2=int rand(9) + 1;
my $num3=int rand(9) + 1;

$sum = $num1+$num2+$num3;

if ($sum < 15){ 
	print "The sum is less than 15\n";
}

elsif ($sum > 15){
	print "The sum is greater than 15\n";
}

else {
	print "The sum is 15\n";
}

if ($sum%2 == 0) {
	print "The number is even\n";
	}

else {
	print "The sum is an odd number\n"; 
	}
