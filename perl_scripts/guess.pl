#!/usr/bin/env perl

use strict;
use warnings;


my $rand_num = int rand(99) + 1;
print "Enter your guess:\t";
my $guess = int <STDIN>;
my $diff = $rand_num - $guess;

if ($guess == $rand_num){
	print "You guessed correctly!\n";
}

elsif($guess > $rand_num){
	print "Your guess is higher than the actual number by ".(-$diff)."\n";
}
else{
	print "Your guess is lower than the actual number by ".$diff."\n";
}

