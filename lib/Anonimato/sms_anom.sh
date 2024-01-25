setterm -foreground green
echo "
 __    __    __  ___   __          __    
/ _\  /__\/\ \ \/   \ / _\  /\/\  / _\   
\ \  /_\ /  \/ / /\ / \ \  /    \ \ \    
_\ \//__/ /\  / /_//  _\ \/ /\/\ \_\ \   
\__/\__/\_\ \/___,'   \__/\/    \/\__/                                 
"
setterm -foreground cyan
echo -n "ingrese el numero de telefono: "
read number
echo -n "ingrese el texto que quieres que reciba: "
read sms
echo "enviando sms..."
sleep 1


curl -X POST https://textbelt.com/text \
       --data-urlencode phone="{$number}" \
       --data-urlencode message="{$sms}" \
       -d key=textbelt