head=$(git rev-parse HEAD)
hash=$(git log --pretty=%H --merges | sed -n 2p)
git reset --hard $hash
find . -name '*.pyc' | xargs -n 1 rm
fab --list --short
fab --list --short > ~/tasks_before
git reset --hard $head
find . -name '*.pyc' | xargs -n 1 rm
fab --list --short
fab --list --short > ~/tasks_after

echo "New tasks to run:"
comm -13 --nocheck-order ~/tasks_before ~/tasks_after

compare=$(comm -13 --nocheck-order ~/tasks_before ~/tasks_after)

echo "$compare"

IFS='
'

for x in $compare; do
   fab install -R desktops "$x"
done