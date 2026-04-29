#!/bin/bash

read -r INPUT_JSON

ACTION=$(echo "$INPUT_JSON" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('command',''))")
IP=$(echo "$INPUT_JSON" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('parameters',{}).get('alert',{}).get('data',{}).get('srcip',''))")
RULEID=$(echo "$INPUT_JSON" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('parameters',{}).get('alert',{}).get('rule',{}).get('id',''))")

LOG_FILE="/var/ossec/logs/active-responses.log"

case $ACTION in
  add)
    [ -z "$IP" ] && exit 0
    echo "$(date) BLOCK: IP=$IP RULE=$RULEID" >> $LOG_FILE
    iptables -I INPUT -s $IP -j DROP
    echo "{\"blocked_ip\":\"$IP\",\"rule\":\"$RULEID\"}" >> /var/ossec/logs/blocked_ips.json
    ;;
  delete)
    [ -z "$IP" ] && exit 0
    echo "$(date) UNBLOCK: IP=$IP RULE=$RULEID" >> $LOG_FILE
    iptables -D INPUT -s $IP -j DROP 2>/dev/null
    ;;
esac

exit 0
