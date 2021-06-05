# Checkpoint_No_hit_rule_usingAPI
Scripts are used to find all the no hit rules and save the information in the CSV file

Steps to run the script:
1. Copy the bash script "no-hit-rule.sh" on the checkpoint management server. Run the script with below command
            >> dos2unix no-hit-rule.sh
            >> chmod 777 no-hit-rule.sh
            >> ./no-hit-rule.sh
 
2. The script will create some JSON files based on the number of rules you have in your rule base (jsonfile1.json, jsonfile2.json)
3. Copy all the JSON files from the management server to your machine, path should be /opt/tmp. Your machine should have python installed.
4. Run python script from your machine.
              >> python ExtractJson.py
5. Python script will ask for the total number of json files you have
6. The script will create outputfile.csv in /opt/tmp/ folder 

Note: This script consider MDS setup. I you dont have domain in your checkpoint setup, you need to modify the script little to remove "-d" key value pair from the api call under no-hit-rule.sh

For more information connect me on: ekta@qostechnology.in
