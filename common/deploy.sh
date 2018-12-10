head=$(git rev-parse HEAD)
hash=$(git log --pretty=%H --merges | sed -n 3p)
git reset --hard $hash
find . -name '*.pyc' -delete
fab --list --short
fab --list --short > ~/tasks_before
git reset --hard $head
find . -name '*.pyc' -delete
fab --list --short
fab --list --short > ~/tasks_after


compare=$(comm -13 --nocheck-order ~/tasks_before ~/tasks_after)

echo "New tasks to run:"
echo "$compare"

IFS='
'

# Wake up the machines
./wakeup.sh

#for x in $compare; do
#   fab -R desktops "$x" -u root
#done
