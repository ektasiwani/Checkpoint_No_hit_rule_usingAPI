#!/bin/sh
echo "Please enter number of rules:"
read rule_count
echo "Please enter domain name"
read domain_name
echo "Please enter fw name:"
read firewall
echo "Please enter layer name"
read layer
echo "Please enter recent date (yyyy-mm-dd)"
read recent_date

echo "Please enter end date (yyyy-mm-dd)"
read last_date

count_num=1
offset_count=0

while [  $rule_count -gt 0 ]
do 
output=$(mgmt_cli show access-rulebase -u "admin" -p "q1w2e3" -d "$domain_name" limit 500 offset $offset_count name "$layer" details-level "standard" use-object-dictionary false show-hits true hits-settings.from-date "$last_date" hits-settings.to-date "$recent_date" hits-settings.target "$firewall" --format json )
echo $output > jsonfile"$count_num".json

count_num=$(($count_num + 1))
rule_count=$(($rule_count - 500))
offset_count=$(($offset_count + 500))
done
