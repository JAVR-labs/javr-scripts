#!/bin/bash

RED='\033[0;31m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color
save_location="./network-log"

ping_patterns=(
    "bytes from"
    "from.*icmp_seq"
    "Destination.*[Uu]nreachable" 
    "Network.*unreachable"
    "No route"
    "timeout"
    "unknown host"
    "not known"
    "failure in name resolution"
    "Network is down"
    "not permitted"
    "Time.*exceeded"
    "Packet filtered"
)

IFS='|'
ping_regex="(${ping_patterns[*]})"
IFS=' '

print_color() {
    printf "${1}%s${NC}\n" "$2" >&2
}

if [[ -n "$1" ]]; then
  ip_address="$1"
else
  read -p "Address to ping: " ip_address
fi

echo "pinging address $ip_address"

touch "$save_location"

while true; do
    ping_result=$(ping -c1 "$ip_address" 2>&1)
    ping_filtered=$(echo "$ping_result" | grep -E "$ping_regex")
    date="$(date '+%Y-%m-%d %H:%M:%S') | "
    
    # Check if ping was successful
    if [[ $ping_result == *"bytes from"* ]]; then
        message="$date$ping_filtered"
        print_color "$GREEN" "$message"
    elif [[ $ping_result == *"nreachable"* ]] || [[ $ping_result == *"timeout"* ]] || [[ $ping_result == *"unknown host"* ]]; then
        message="$date$ping_result"
    else
        message="$date Unknown error: $ping_result"
        print_color "$YELLOW" "$message"
    fi
    
    echo "$message" >> "$save_location"
    
    sleep 1
done

