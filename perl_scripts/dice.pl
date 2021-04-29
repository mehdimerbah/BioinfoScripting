#!/usr/bin/env perl

use strict;
use warnings;


my $die1 = int rand(5) + 1;
my $die2 = int rand(5) + 1;
my $die3 = int rand(5) + 1;
my $die4 = int rand(5) + 1;
my $die5 = int rand(5) + 1;

my $sum = $die1 + $die2 + $die3 + $die4 + $die5;

print "The value of die1 is: ".$die1."\n";
print "The value of die2 is: ".$die2."\n";
print "The value of die3 is: ".$die3."\n";
print "The value of die4 is: ".$die4."\n";
print "The value of die5 is: ".$die5."\n";

print "The sum of all dice is ".$sum."\n";

