#!/bin/bash

module load vaspkit/1.4.0

for dir in u_*_N_*
do
    if [ -d "$dir" ]; then
        echo "Processing $dir"
        cd "$dir"

        vaspkit <<EOF
21
211
EOF

        cd ..
    fi
done

