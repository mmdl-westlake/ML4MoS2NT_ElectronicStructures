#!/bin/bash

module load vaspkit/1.4.0

# Iterate over all directories matching the pattern u_*_N_*
for dir in u_*_N_*
do
    if [ -d "$dir" ]; then
        echo "Processing $dir"
        cd "$dir"

        # Run vaspkit and send the commands 21 and 211
        vaspkit <<EOF
21
211
EOF

        cd ..
    fi
done

