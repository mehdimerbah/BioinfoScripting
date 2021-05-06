#!/bin/bash

FILENAME="$1.pl"

touch $FILENAME

printf "#!/usr/bin/env perl\n" >> $FILENAME
printf "use strict;\nuse warnings;\n" >> $FILENAME 



chmod u+x $FILENAME




