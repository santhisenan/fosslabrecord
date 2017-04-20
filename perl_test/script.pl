#!/usr/bin/perl
print "Hello 
        
        World! \n";
$a = 10;
$var = <<"eof";
this could well bw another 
multiline comment.
I misspelt a be in the above sentence 
That was a mistake 
I am not tyring to explain , but ...
just want to  print the a=$a
eof

print "$var";

=begin comment
This is a multiline comment 
this is ignored be the perl compiler
=cut
