#!/usr/bin/perl

$string = "Hello World";
if($string =~ /match/){
print "Match found\n";
}

else{
print "It is not matching\n "
}

$string = "matchstick";
if($string =~ /match/){
print "Match found\n";
}

else{
print "It is not matching\n";
}
