#!/bin/bash

echo "===================="
echo "Enterprise Warehouse System Check"
echo "===================="

echo ""
echo "Current user:"
whoami

echo ""
echo "HOSTNAME:"
hostname

echo ""
echo "SYSTEM UPTIME:"
uptime

echo ""
echo "MEMORY USAGE:"
free -h

echo ""
echo "DISK USAGE"
df -h /

echo ""
echo "ACTIVE PROCESSES:"
ps aux --sort=-%cpu | head -6

echo ""
echo "SYSTEM CHECK COMPLETED"
