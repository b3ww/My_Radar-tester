# My_Radar-tester
Python short script to generate a script like . rdr for the my_radar Epitech project

Use:
python3 radar.py [-flags] [arguments]

Flags:
  -e: executes . /my_radar with the path of a file passed as argument, example: -e scripts/test.rdr
 
  -c: create script in . rdr in the file passed as an argument with the number of planes and towers also as an argument,
      example: -c scripts 10 10
      
  -ce or -ec: creates and executes a script
  
  -rm: removes the file passed as argument and if you add -all before this removes all . rdr files from the directory passed as argument,
        example: rm scrpits/test.rdr
                 rm -all scripts
