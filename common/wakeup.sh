echo  "Send WOL packets"
ether-wake -i eno1 '7c:05:07:0c:c5:e5'
ether-wake -i eno1 '7c:05:07:10:6b:37'
ether-wake -i eno1 '7c:05:07:0d:5b:fb'
echo  "Waiting for desktops to start"
until nc -vzw 2 fs-desktop-01.freeside.co.uk 22; do sleep 2; done
until nc -vzw 2 fs-desktop-02.freeside.co.uk 22; do sleep 2; done
until nc -vzw 2 fs-desktop-03.freeside.co.uk 22; do sleep 2; done
echo  "Desktops started"
