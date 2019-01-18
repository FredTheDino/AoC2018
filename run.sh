python $(date | awk '{split($0,a," "); b="aoc"; c=".py"; print b a[2] c}')

